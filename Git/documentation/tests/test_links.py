#!/usr/bin/env python3
"""
Tests de validation des liens dans la documentation
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


class LinkValidator:
    """Validateur de liens pour la documentation."""

    def __init__(self, base_path: Path):
        self.base_path = base_path.resolve()
        self.errors = []
        self.warnings = []
        
    def validate_markdown_file(self, file_path: Path) -> Dict:
        """Valide tous les liens dans un fichier Markdown."""
        results = {
            "file": str(file_path),
            "internal_links": {"valid": [], "broken": []},
            "external_links": {"valid": [], "broken": [], "warnings": []},
            "anchor_links": {"valid": [], "broken": []}
        }
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extraire tous les liens
            links = self._extract_links(content)
            
            # Valider chaque type de lien
            for link in links:
                if link["type"] == "internal":
                    self._validate_internal_link(link, file_path, results)
                elif link["type"] == "external":
                    self._validate_external_link(link, results)
                elif link["type"] == "anchor":
                    self._validate_anchor_link(link, content, results)
        
        except Exception as e:
            results["error"] = str(e)
            self.errors.append(f"Erreur lecture {file_path}: {e}")
        
        return results
    
    def _extract_links(self, content: str) -> List[Dict]:
        """Extrait tous les liens du contenu Markdown."""
        links = []
        
        # Liens Markdown: [text](url)
        markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in markdown_links:
            links.append({
                "text": text,
                "url": url,
                "type": self._classify_link(url)
            })
        
        # Liens référence: [text][ref]
        ref_links = re.findall(r'\[([^\]]+)\]\[([^\]]+)\]', content)
        for text, ref in ref_links:
            # TODO: résoudre les références
            pass
        
        return links
    
    def _classify_link(self, url: str) -> str:
        """Classifie le type de lien."""
        if url.startswith('http://') or url.startswith('https://'):
            return "external"
        elif url.startswith('#'):
            return "anchor"
        else:
            return "internal"
    
    def _validate_internal_link(self, link: Dict, file_path: Path, results: Dict):
        """Valide un lien interne."""
        url = link["url"]
        
        # Résoudre le chemin relatif
        if url.startswith('/'):
            # Chemin absolu depuis la racine du projet
            target_path = self.base_path / url.lstrip('/')
        else:
            # Chemin relatif depuis le fichier courant
            target_path = file_path.parent / url
        
        # Gérer les ancres dans les fichiers internes
        if '#' in url:
            file_part, anchor = url.split('#', 1)
            if file_part:
                target_path = file_path.parent / file_part
            else:
                target_path = file_path
        
        # Vérifier si le fichier existe
        if target_path.exists():
            results["internal_links"]["valid"].append(link)
        else:
            link["target"] = str(target_path)
            results["internal_links"]["broken"].append(link)
            self.errors.append(f"Lien interne cassé dans {file_path}: {url} -> {target_path}")
    
    def _validate_external_link(self, link: Dict, results: Dict):
        """Valide un lien externe."""
        url = link["url"]
        
        try:
            # Créer une requête avec user-agent
            request = Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (compatible; DocLinkChecker/1.0)'}
            )
            
            # Faire la requête avec timeout
            with urlopen(request, timeout=10) as response:
                status = response.getcode()
                
                if 200 <= status < 400:
                    results["external_links"]["valid"].append(link)
                else:
                    link["status"] = status
                    results["external_links"]["broken"].append(link)
                    self.errors.append(f"Lien externe cassé: {url} (HTTP {status})")
        
        except HTTPError as e:
            link["status"] = e.code
            results["external_links"]["broken"].append(link)
            self.errors.append(f"Lien externe cassé: {url} (HTTP {e.code})")
        
        except URLError as e:
            link["error"] = str(e)
            results["external_links"]["broken"].append(link)
            self.errors.append(f"Lien externe cassé: {url} ({e})")
        
        except Exception as e:
            link["error"] = str(e)
            results["external_links"]["warnings"].append(link)
            self.warnings.append(f"Impossible de vérifier le lien externe: {url} ({e})")
    
    def _validate_anchor_link(self, link: Dict, content: str, results: Dict):
        """Valide un lien d'ancre dans le même fichier."""
        anchor = link["url"][1:]  # Enlever le #
        
        # Normaliser l'ancre (GitHub style)
        normalized_anchor = anchor.lower().replace(' ', '-').replace('_', '-')
        normalized_anchor = re.sub(r'[^\w\-]', '', normalized_anchor)
        
        # Chercher les headers dans le contenu
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        
        found = False
        for header in headers:
            header_anchor = header.lower().replace(' ', '-').replace('_', '-')
            header_anchor = re.sub(r'[^\w\-]', '', header_anchor)
            
            if header_anchor == normalized_anchor:
                found = True
                break
        
        if found:
            results["anchor_links"]["valid"].append(link)
        else:
            results["anchor_links"]["broken"].append(link)
            self.errors.append(f"Ancre introuvable: {anchor}")
    
    def validate_directory(self, directory: Path) -> Dict:
        """Valide tous les fichiers Markdown dans un répertoire."""
        all_results = {
            "summary": {
                "total_files": 0,
                "files_with_errors": 0,
                "total_errors": 0,
                "total_warnings": 0
            },
            "files": {}
        }
        
        # Trouver tous les fichiers Markdown
        md_files = list(directory.rglob("*.md"))
        
        for md_file in md_files:
            if any(skip in str(md_file) for skip in [".git", "__pycache__", "venv"]):
                continue
            
            all_results["summary"]["total_files"] += 1
            
            # Valider le fichier
            results = self.validate_markdown_file(md_file)
            all_results["files"][str(md_file)] = results
            
            # Compter les erreurs
            file_errors = (
                len(results["internal_links"]["broken"]) +
                len(results["external_links"]["broken"]) +
                len(results["anchor_links"]["broken"])
            )
            
            file_warnings = len(results["external_links"]["warnings"])
            
            if file_errors > 0:
                all_results["summary"]["files_with_errors"] += 1
                all_results["summary"]["total_errors"] += file_errors
            
            all_results["summary"]["total_warnings"] += file_warnings
        
        return all_results
    
    def generate_report(self, results: Dict) -> str:
        """Génère un rapport lisible."""
        report = "# 📗 Rapport de validation des liens\n\n"
        
        # Résumé
        summary = results["summary"]
        report += "## 📊 Résumé\n\n"
        report += f"- **Fichiers analysés**: {summary['total_files']}\n"
        report += f"- **Fichiers avec erreurs**: {summary['files_with_errors']}\n"
        report += f"- **Erreurs totales**: {summary['total_errors']}\n"
        report += f"- **Avertissements**: {summary['total_warnings']}\n\n"
        
        # Détails par fichier
        if summary["total_errors"] > 0:
            report += "## ❌ Erreurs détectées\n\n"
            
            for file_path, file_results in results["files"].items():
                file_errors = (
                    len(file_results["internal_links"]["broken"]) +
                    len(file_results["external_links"]["broken"]) +
                    len(file_results["anchor_links"]["broken"])
                )
                
                if file_errors > 0:
                    report += f"### {file_path}\n\n"
                    
                    # Liens internes cassés
                    if file_results["internal_links"]["broken"]:
                        report += "#### Liens internes cassés\n\n"
                        for link in file_results["internal_links"]["broken"]:
                            report += f"- `{link['text']}` -> `{link['url']}` (cible: `{link.get('target', 'inconnue')}`)\n"
                        report += "\n"
                    
                    # Liens externes cassés
                    if file_results["external_links"]["broken"]:
                        report += "#### Liens externes cassés\n\n"
                        for link in file_results["external_links"]["broken"]:
                            status = link.get("status", link.get("error", "inconnu"))
                            report += f"- `{link['text']}` -> `{link['url']}` ({status})\n"
                        report += "\n"
                    
                    # Ancres cassées
                    if file_results["anchor_links"]["broken"]:
                        report += "#### Ancres cassées\n\n"
                        for link in file_results["anchor_links"]["broken"]:
                            report += f"- `{link['text']}` -> `{link['url']}`\n"
                        report += "\n"
        
        # Avertissements
        if summary["total_warnings"] > 0:
            report += "## ⚠️ Avertissements\n\n"
            
            for file_path, file_results in results["files"].items():
                if file_results["external_links"]["warnings"]:
                    report += f"### {file_path}\n\n"
                    for link in file_results["external_links"]["warnings"]:
                        report += f"- `{link['text']}` -> `{link['url']}` ({link.get('error', 'inconnu')})\n"
                    report += "\n"
        
        # Statut final
        if summary["total_errors"] == 0:
            report += "## ✅ Tous les liens sont valides !\n\n"
        else:
            report += f"## ❌ {summary['total_errors']} liens à corriger\n\n"
        
        return report


def main():
    """Point d'entrée principal."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validateur de liens de documentation")
    parser.add_argument("path", nargs="?", default="documentation/src",
                       help="Chemin à analyser (défaut: documentation/src)")
    parser.add_argument("--output", "-o", default="link-validation-report.md",
                       help="Fichier de sortie du rapport")
    parser.add_argument("--json", action="store_true",
                       help="Sortie JSON au lieu de Markdown")
    parser.add_argument("--quiet", "-q", action="store_true",
                       help="Mode silencieux")
    
    args = parser.parse_args()
    
    try:
        base_path = Path(args.path).resolve()
        validator = LinkValidator(base_path)
        
        if not args.quiet:
            print(f"🔍 Validation des liens dans: {base_path}")
        
        # Valider le répertoire
        results = validator.validate_directory(base_path)
        
        # Afficher le résumé
        if not args.quiet:
            summary = results["summary"]
            print(f"\n📊 {summary['total_files']} fichiers analysés")
            print(f"❌ {summary['total_errors']} erreurs")
            print(f"⚠️  {summary['total_warnings']} avertissements")
        
        # Générer le rapport
        if args.json:
            output_path = Path(args.output)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
        else:
            report = validator.generate_report(results)
            output_path = Path(args.output)
            output_path.write_text(report, encoding="utf-8")
        
        if not args.quiet:
            print(f"📄 Rapport sauvegardé: {output_path}")
        
        # Code de sortie
        if results["summary"]["total_errors"] > 0:
            sys.exit(1)
        
    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

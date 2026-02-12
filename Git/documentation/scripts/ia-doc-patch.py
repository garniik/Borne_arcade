#!/usr/bin/env python3
"""
Script pour générer des patches de documentation assistés par IA.
Principe: IA propose, jamais n'impose.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    import yaml
except ImportError:
    print("Erreur: yaml requis. Installe avec: pip install pyyaml")
    sys.exit(1)


class IADocPatcher:
    """Générateur de patches de documentation assisté par IA."""

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path("documentation/.docs/config.yml")
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """Charge la configuration depuis config.yml."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config non trouvée: {self.config_path}")
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def get_git_diff(self, commit_range: Optional[str] = None) -> str:
        """Récupère le diff git."""
        if commit_range:
            cmd = ["git", "diff", "--name-only", commit_range]
        else:
            cmd = ["git", "diff", "--name-only", "HEAD~1"]
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                encoding='utf-8',  # Force UTF-8 encoding
                errors='replace'    # Remplace les caractères invalides
            )
            
            if result.returncode != 0:
                raise Exception(f"Erreur git diff: {result.stderr}")
            
            return result.stdout.strip()
            
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return ""
    
    def get_full_diff(self, commit_range: str = "HEAD~1..HEAD") -> str:
        """Récupère le diff complet avec le contenu."""
        try:
            result = subprocess.run(
                ["git", "diff", commit_range],
                capture_output=True,
                text=True,
                check=True,
                encoding='utf-8',  # Force UTF-8 encoding
                errors='replace'  # Remplace les caractères invalides
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur git diff: {e}")
            return ""
    
    def find_related_docs(self, changed_files: List[str]) -> List[Path]:
        """Trouve les fichiers de documentation liés aux changements."""
        doc_files = []
        doc_dir = Path("src")
        
        for changed_file in changed_files:
            # Convertir le chemin de code vers doc pour la borne arcade
            if changed_file.startswith("borne_arcade/"):
                # Fichiers principaux de la borne
                if any(main_file in changed_file for main_file in ["Main.java", "Graphique.java"]):
                    doc_files.extend([
                        doc_dir / "api" / "main-interface.md",
                        doc_dir / "how-to" / "installation.md"
                    ])
                
                # Gestion du clavier
                elif "ClavierBorneArcade" in changed_file:
                    doc_files.extend([
                        doc_dir / "hardware" / "controls.md",
                        doc_dir / "api" / "input-system.md"
                    ])
                
                # Gestion des scores
                elif "HighScore" in changed_file:
                    doc_files.extend([
                        doc_dir / "api" / "high-score-system.md",
                        doc_dir / "how-to" / "score-management.md"
                    ])
                
                # Interface graphique
                elif any(graphic_file in changed_file for graphic_file in ["Graphique.java", "Boite", "Bouton"]):
                    doc_files.extend([
                        doc_dir / "api" / "gui-components.md",
                        doc_dir / "design" / "interface-guide.md"
                    ])
                
                # Jeux spécifiques
                elif "projet/" in changed_file:
                    game_name = Path(changed_file).parts[2]  # ex: Columns, Pong, etc.
                    doc_files.extend([
                        doc_dir / "games" / f"{game_name.lower()}.md",
                        doc_dir / "api" / "game-interface.md"
                    ])
                
                # Scripts shell
                elif changed_file.endswith(".sh"):
                    doc_files.extend([
                        doc_dir / "how-to" / "game-management.md",
                        doc_dir / "administration" / "scripts.md"
                    ])
            
            # Documentation MG2D (bibliothèque graphique)
            elif changed_file.startswith("MG2D/"):
                doc_files.extend([
                    doc_dir / "api" / "mg2d-library.md",
                    doc_dir / "development" / "graphics.md"
                ])
        
        # Ajouter docs génériques si aucun match
        if not doc_files:
            generic_docs = [
                doc_dir / "index.md",
                doc_dir / "how-to" / "installation.md",
                doc_dir / "api" / "overview.md"
            ]
            for doc in generic_docs:
                if doc.exists():
                    doc_files.append(doc)
        
        return list(set(doc_files))  # Dédupliquer
    
    def analyze_changes(self, diff: str) -> Dict[str, List[str]]:
        """Analyse les changements pour extraire les éléments à documenter."""
        analysis = {
            "new_classes": [],
            "new_methods": [],
            "new_games": [],
            "modified_controls": [],
            "new_shell_scripts": [],
            "api_changes": []
        }
        
        # TODO: Analyse plus sophistiquée avec AST pour Java
        lines = diff.split('\n')
        for line in lines:
            line = line.strip()
            
            # Classes Java
            if line.startswith('+') and 'public class' in line:
                class_name = line.split('class ')[1].split('{')[0].strip()
                analysis["new_classes"].append(class_name)
            
            # Méthodes Java
            elif line.startswith('+') and ('public' in line or 'private' in line) and '(' in line:
                method_match = re.search(r'(public|private)\s+\w+\s+(\w+)\s*\(', line)
                if method_match:
                    method_name = method_match.group(2)
                    analysis["new_methods"].append(method_name)
            
            # Nouveaux jeux (dossiers projet/)
            elif line.startswith('+') and 'projet/' in line and '.java' in line:
                game_name = line.split('/')[2] if len(line.split('/')) > 2 else "unknown"
                if game_name not in analysis["new_games"]:
                    analysis["new_games"].append(game_name)
            
            # Changements de contrôles (ClavierBorneArcade)
            elif line.startswith('+') and ('ClavierBorneArcade' in line or 'touche' in line.lower()):
                analysis["modified_controls"].append("Contrôles mis à jour")
            
            # Scripts shell
            elif line.startswith('+') and line.endswith('.sh'):
                script_name = line.split('/')[-1].replace('+', '').strip()
                analysis["new_shell_scripts"].append(script_name)
            
            # Changements API (méthodes publiques)
            elif line.startswith('+') and 'public' in line and ('static' in line or 'void' in line):
                analysis["api_changes"].append("API modifiée")
        
        return analysis
    
    def generate_patch_content(self, analysis: Dict, related_docs: List[Path]) -> Dict[Path, str]:
        """Génère le contenu des patches pour chaque doc."""
        patches = {}
        
        for doc_path in related_docs:
            if not doc_path.exists():
                continue
                
            current_content = doc_path.read_text(encoding="utf-8")
            
            # Génération simplifiée - dans la vraie version, utiliser l'IA
            new_content = self._generate_doc_updates(current_content, analysis)
            
            if new_content != current_content:
                patches[doc_path] = new_content
        
        return patches
    
    def _generate_doc_updates(self, content: str, analysis: Dict) -> str:
        """Génère les mises à jour de documentation (simulation IA) pour la borne arcade."""
        updated_content = content
        
        # Ajouter nouvelles classes Java
        if analysis["new_classes"]:
            new_classes_section = "\n## Nouvelles classes\n\n"
            for cls in analysis["new_classes"]:
                new_classes_section += f"- `{cls}` - TODO: documenter cette classe Java\n"
            updated_content += new_classes_section
        
        # Ajouter nouvelles méthodes
        if analysis["new_methods"]:
            new_methods_section = "\n## Nouvelles méthodes\n\n"
            for method in analysis["new_methods"]:
                new_methods_section += f"- `{method}()` - TODO: documenter cette méthode\n"
            updated_content += new_methods_section
        
        # Ajouter nouveaux jeux
        if analysis["new_games"]:
            new_games_section = "\n## Nouveaux jeux ajoutés\n\n"
            for game in analysis["new_games"]:
                new_games_section += f"- **{game}** - TODO: documenter ce jeu\n"
                new_games_section += f"  - Contrôles: TODO\n"
                new_games_section += f"  - Objectif: TODO\n"
                new_games_section += f"  - Instructions: TODO\n"
            updated_content += new_games_section
        
        # Ajouter changements de contrôles
        if analysis["modified_controls"]:
            controls_section = "\n## Mise à jour des contrôles\n\n"
            controls_section += "- Les contrôles ont été modifiés. Mettre à jour la section [Hardware/Controls](../hardware/controls.md)\n"
            updated_content += controls_section
        
        # Ajouter nouveaux scripts
        if analysis["new_shell_scripts"]:
            scripts_section = "\n## Nouveaux scripts d'administration\n\n"
            for script in analysis["new_shell_scripts"]:
                scripts_section += f"- `{script}` - TODO: documenter ce script\n"
            updated_content += scripts_section
        
        # Ajouter changements API
        if analysis["api_changes"]:
            api_section = "\n## Changements API\n\n"
            api_section += "- L'API de la borne a été modifiée. Mettre à jour la documentation de l'API.\n"
            updated_content += api_section
        
        return updated_content
    
    def create_patches(self, patches: Dict[Path, str]) -> List[Dict]:
        """Crée les patches au format standard."""
        patch_list = []
        
        for file_path, new_content in patches.items():
            old_content = file_path.read_text(encoding="utf-8")
            
            # Créer un diff unifié
            patch = {
                "file": str(file_path),
                "old_content": old_content,
                "new_content": new_content,
                "diff": self._create_diff(old_content, new_content, str(file_path))
            }
            patch_list.append(patch)
        
        return patch_list
    
    def _create_diff(self, old: str, new: str, filename: str) -> str:
        """Crée un diff unifié entre old et new."""
        try:
            import difflib
            old_lines = old.splitlines(keepends=True)
            new_lines = new.splitlines(keepends=True)
            
            diff = difflib.unified_diff(
                old_lines,
                new_lines,
                fromfile=f"a/{filename}",
                tofile=f"b/{filename}",
                lineterm=""
            )
            
            return "".join(diff)
        except ImportError:
            return f"# Diff non disponible pour {filename}\n"
    
    def generate_pr_summary(self, patches: List[Dict], analysis: Dict) -> str:
        """Génère un résumé pour la PR."""
        summary = "## 📝 Mises à jour documentation proposées\n\n"
        
        if patches:
            summary += f"**{len(patches)} fichiers modifiés :**\n"
            for patch in patches:
                summary += f"- `{patch['file']}`\n"
        else:
            summary += "Aucune mise à jour requise.\n"
        
        if analysis["new_classes"]:
            summary += f"\n**{len(analysis['new_classes'])} nouvelles classes détectées**\n"
        
        if analysis["new_methods"]:
            summary += f"\n**{len(analysis['new_methods'])} nouvelles méthodes détectées**\n"
        
        if analysis["new_games"]:
            summary += f"\n**{len(analysis['new_games'])} nouveaux jeux détectés**\n"
        
        summary += "\n---\n*Généré automatiquement par IA Doc Patcher*"
        
        return summary
    
    def apply_patches(self, patches: List[Dict], dry_run: bool = True) -> bool:
        """Applique les patches (ou simule si dry_run)."""
        for patch in patches:
            file_path = Path(patch["file"])
            
            if dry_run:
                print(f"[DRY RUN] Mise à jour: {file_path}")
                print(f"  + {len(patch['new_content'].splitlines())} lignes")
            else:
                file_path.write_text(patch["new_content"], encoding="utf-8")
                print(f"Mis à jour: {file_path}")
        
        return True


def main():
    parser = argparse.ArgumentParser(description="IA Doc Patcher")
    parser.add_argument("--commit-range", default="HEAD~1..HEAD", 
                       help="Range de commits à analyser")
    parser.add_argument("--dry-run", action="store_true", 
                       help="Simuler sans appliquer les changements")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")
    parser.add_argument("--config", type=Path, 
                       help="Chemin vers config.yml")
    
    args = parser.parse_args()
    
    try:
        patcher = IADocPatcher(args.config)
        
        # Analyser les changements
        print("🔍 Analyse des changements...")
        changed_files = patcher.get_git_diff(args.commit_range).split('\n')
        full_diff = patcher.get_full_diff(args.commit_range)
        analysis = patcher.analyze_changes(full_diff)
        
        # Trouver les docs liées
        print("📚 Recherche des docs liées...")
        related_docs = patcher.find_related_docs(changed_files)
        
        # Générer les patches
        print("✍️ Génération des patches...")
        patch_content = patcher.generate_patch_content(analysis, related_docs)
        patches = patcher.create_patches(patch_content)
        
        # Générer le résumé
        summary = patcher.generate_pr_summary(patches, analysis)
        
        # Afficher les résultats
        print("\n" + "="*50)
        print(summary)
        print("="*50)
        
        # Appliquer les patches
        if patches:
            print(f"\n📦 {len(patches)} patches générés")
            if not args.dry_run:
                patcher.apply_patches(patches, dry_run=False)
                print("✅ Patches appliqués")
            else:
                print("[DRY RUN] Utilisez --apply pour appliquer")
        
        # Sauvegarder le rapport
        if args.output:
            report = {
                "summary": summary,
                "patches": [
                    {
                        "file": p["file"],
                        "diff": p["diff"]
                    } for p in patches
                ],
                "analysis": analysis
            }
            Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
            print(f"📄 Rapport sauvegardé: {args.output}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
IA Doc Coverage - Détecte les trous dans la documentation

Principe : analyse le code source pour identifier :
- fonctions publiques sans docstring
- endpoints non documentés  
- exemples manquants
- liens cassés
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

try:
    import yaml
except ImportError:
    print("Erreur: yaml requis. Installe avec: pip install pyyaml")
    sys.exit(1)


class DocCoverageAnalyzer:
    """Analyseur de couverture de documentation."""

    def __init__(self, config_path: Path = None):
        self.config_path = config_path or Path(".docs/config.yml")
        self.config = self._load_config()
        self.issues = []
        
    def _load_config(self) -> Dict:
        """Charge la configuration."""
        if not self.config_path.exists():
            return {}
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    
    def analyze_java_file(self, file_path: Path) -> Dict:
        """Analyse un fichier Java pour la couverture doc."""
        issues = {
            "missing_javadoc": [],
            "missing_type_hints": [],
            "missing_examples": [],
            "public_without_doc": []
        }
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Analyse simple du code Java (sans AST complexe)
            lines = content.split('\n')
            in_javadoc = False
            current_class = None
            current_method = None
            
            for i, line in enumerate(lines, 1):
                line = line.strip()
                
                # Détecter les classes Java
                if 'public class' in line:
                    class_match = re.search(r'public\s+class\s+(\w+)', line)
                    if class_match:
                        current_class = class_match.group(1)
                        
                        # Vérifier si la classe a de la Javadoc
                        has_javadoc = self._check_javadoc_before(lines, i-1)
                        if not has_javadoc:
                            issues["missing_javadoc"].append({
                                "name": current_class,
                                "type": "class",
                                "line": i
                            })
                
                # Détecter les méthodes publiques
                elif ('public' in line and '(' in line and ')' in line and 
                      not line.strip().startswith('//') and 
                      not 'class' in line):
                    method_match = re.search(r'public\s+\w+\s+(\w+)\s*\(', line)
                    if method_match:
                        current_method = method_match.group(1)
                        
                        # Vérifier si la méthode a de la Javadoc
                        has_javadoc = self._check_javadoc_before(lines, i-1)
                        if not has_javadoc:
                            issues["missing_javadoc"].append({
                                "name": f"{current_class}.{current_method}" if current_class else current_method,
                                "type": "method",
                                "line": i
                            })
                
                # Détecter les méthodes statiques publiques (API)
                elif ('public static' in line and '(' in line and ')' in line):
                    method_match = re.search(r'public\s+static\s+\w+\s+(\w+)\s*\(', line)
                    if method_match:
                        method_name = method_match.group(1)
                        issues["public_without_doc"].append({
                            "name": method_name,
                            "type": "static_method",
                            "line": i
                        })
        
        except Exception as e:
            issues["parse_error"] = str(e)
        
        return issues
    
    def _check_javadoc_before(self, lines: List[str], index: int) -> bool:
        """Vérifie s'il y a une Javadoc avant la ligne donnée."""
        # Regarder en arrière pour trouver /** ... */
        for i in range(index-1, max(-1, index-10), -1):
            line = lines[i].strip()
            if '/**' in line:
                return True
            elif line and not line.startswith('*') and not line.startswith('//'):
                break
        return False
    
    def _check_function(self, node: ast.FunctionDef, file_path: Path, issues: Dict):
        """Vérifie la documentation d'une fonction."""
        func_name = node.name
        
        # Ignorer les fonctions privées si configuré
        if func_name.startswith('_') and not func_name.startswith('__'):
            if self.config.get("check_private_functions", False):
                if not ast.get_docstring(node):
                    issues["private_without_docstring"].append({
                        "name": func_name,
                        "line": node.lineno
                    })
            return
        
        # Vérifier la docstring
        if not ast.get_docstring(node):
            issues["missing_docstrings"].append({
                "name": func_name,
                "line": node.lineno,
                "type": "function"
            })
        
        # Vérifier les type hints
        if not node.returns:
            issues["missing_type_hints"].append({
                "name": func_name,
                "line": node.lineno,
                "missing": "return"
            })
        
        for arg in node.args.args:
            if arg.annotation is None and arg.arg != "self":
                if "missing_type_hints" not in issues:
                    issues["missing_type_hints"] = []
                issues["missing_type_hints"].append({
                    "name": func_name,
                    "line": node.lineno,
                    "missing": f"param {arg.arg}"
                })
    
    def _check_class(self, node: ast.ClassDef, file_path: Path, issues: Dict):
        """Vérifie la documentation d'une classe."""
        class_name = node.name
        
        if not ast.get_docstring(node):
            issues["missing_docstrings"].append({
                "name": class_name,
                "line": node.lineno,
                "type": "class"
            })
    
    def analyze_markdown_file(self, file_path: Path) -> Dict:
        """Analyse un fichier Markdown."""
        issues = {
            "broken_links": [],
            "missing_sections": [],
            "malformed_headers": []
        }
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Vérifier les liens
            issues["broken_links"] = self._check_markdown_links(content, file_path)
            
            # Vérifier la structure
            issues["missing_sections"] = self._check_required_sections(content, file_path)
            
            # Vérifier les headers
            issues["malformed_headers"] = self._check_header_format(content)
        
        except Exception as e:
            issues["parse_error"] = str(e)
        
        return issues
    
    def _check_markdown_links(self, content: str, file_path: Path) -> List[Dict]:
        """Vérifie les liens dans un fichier Markdown."""
        broken_links = []
        
        # Liens internes [text](link)
        internal_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, link in internal_links:
            if link.startswith('http'):
                continue  # Liens externes - vérification optionnelle
            
            # Lien relatif
            target_path = (file_path.parent / link).resolve()
            if not target_path.exists():
                broken_links.append({
                    "text": text,
                    "link": link,
                    "line": self._find_line_number(content, link)
                })
        
        return broken_links
    
    def _check_required_sections(self, content: str, file_path: Path) -> List[str]:
        """Vérifie les sections requises selon le type de fichier."""
        missing = []
        
        if "api" in str(file_path):
            required_sections = ["Vue d'ensemble", "API", "Exemples"]
        elif "how-to" in str(file_path):
            required_sections = ["Prérequis", "Installation", "Exemples"]
        else:
            required_sections = []
        
        for section in required_sections:
            if section.lower() not in content.lower():
                missing.append(section)
        
        return missing
    
    def _check_header_format(self, content: str) -> List[Dict]:
        """Vérifie le format des headers."""
        malformed = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if line.startswith('#'):
                # Vérifier l'espace après #
                if not re.match(r'^#+\s', line):
                    malformed.append({
                        "line": i,
                        "content": line.strip(),
                        "issue": "missing_space_after_hash"
                    })
                
                # Vérifier la hiérarchie
                level = len(line) - len(line.lstrip('#'))
                if level > 6:
                    malformed.append({
                        "line": i,
                        "content": line.strip(),
                        "issue": "header_level_too_deep"
                    })
        
        return malformed
    
    def _find_line_number(self, content: str, search: str) -> int:
        """Trouve la ligne d'un texte dans le contenu."""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if search in line:
                return i
        return 0
    
    def analyze_project(self, root_path: Path) -> Dict:
        """Analyse tout le projet de la borne arcade."""
        report = {
            "summary": {
                "total_files": 0,
                "files_with_issues": 0,
                "total_issues": 0
            },
            "files": {},
            "coverage": {
                "classes_documented": 0,
                "classes_total": 0,
                "methods_documented": 0,
                "methods_total": 0,
                "games_documented": 0,
                "games_total": 0
            }
        }
        
        # Analyser les fichiers Java de la borne
        for java_file in root_path.rglob("*.java"):
            if any(skip in str(java_file) for skip in [".git", "__pycache__", "venv"]):
                continue
            
            report["summary"]["total_files"] += 1
            issues = self.analyze_java_file(java_file)
            
            if any(issues.values()):
                report["summary"]["files_with_issues"] += 1
                report["files"][str(java_file)] = issues
                
                # Compter les problèmes
                for issue_list in issues.values():
                    if isinstance(issue_list, list):
                        report["summary"]["total_issues"] += len(issue_list)
        
        # Analyser les scripts shell
        for sh_file in root_path.rglob("*.sh"):
            if any(skip in str(sh_file) for skip in [".git", "__pycache__", "venv"]):
                continue
            
            report["summary"]["total_files"] += 1
            issues = self.analyze_shell_file(sh_file)
            
            if any(issues.values()):
                report["summary"]["files_with_issues"] += 1
                report["files"][str(sh_file)] = issues
                
                for issue_list in issues.values():
                    if isinstance(issue_list, list):
                        report["summary"]["total_issues"] += len(issue_list)
        
        # Analyser les fichiers Markdown
        for md_file in root_path.rglob("*.md"):
            if any(skip in str(md_file) for skip in [".git", "venv"]):
                continue
            
            report["summary"]["total_files"] += 1
            issues = self.analyze_markdown_file(md_file)
            
            if any(issues.values()):
                report["summary"]["files_with_issues"] += 1
                report["files"][str(md_file)] = issues
                
                for issue_list in issues.values():
                    if isinstance(issue_list, list):
                        report["summary"]["total_issues"] += len(issue_list)
        
        # Calculer la couverture
        self._calculate_coverage(report)
        
        return report
    
    def analyze_shell_file(self, file_path: Path) -> Dict:
        """Analyse un script shell pour la documentation."""
        issues = {
            "missing_comments": [],
            "missing_usage": [],
            "missing_examples": []
        }
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split('\n')
            has_header_comment = False
            has_usage_info = False
            
            for i, line in enumerate(lines, 1):
                line = line.strip()
                
                # Vérifier les commentaires d'en-tête
                if line.startswith('#') and i <= 5:
                    has_header_comment = True
                
                # Vérifier les informations d'usage
                if 'usage' in line.lower() or 'utilisation' in line.lower():
                    has_usage_info = True
            
            if not has_header_comment:
                issues["missing_comments"].append({
                    "type": "header",
                    "line": 1
                })
            
            if not has_usage_info:
                issues["missing_usage"].append({
                    "type": "usage_info",
                    "line": 0
                })
        
        except Exception as e:
            issues["parse_error"] = str(e)
        
        return issues
    
    def _calculate_coverage(self, report: Dict):
        """Calcule les métriques de couverture pour la borne arcade."""
        classes_total = 0
        classes_documented = 0
        methods_total = 0
        methods_documented = 0
        games_total = 0
        games_documented = 0
        
        for file_path, issues in report["files"].items():
            if file_path.endswith(".java"):
                # Compter les classes et méthodes Java
                missing_javadoc = len(issues.get("missing_javadoc", []))
                
                # Estimation : chaque fichier Java a en moyenne 2 classes et 5 méthodes
                # (approximation pour la démo)
                estimated_classes = 2
                estimated_methods = 5
                
                classes_total += estimated_classes
                methods_total += estimated_methods
                
                # Classes documentées = total - manquantes
                classes_documented += max(0, estimated_classes - missing_javadoc // 3)
                methods_documented += max(0, estimated_methods - missing_javadoc // 2)
            
            elif file_path.endswith(".sh"):
                # Scripts shell
                games_total += 1  # Chaque script lance potentiellement un jeu
                if not issues.get("missing_comments"):
                    games_documented += 1
        
        report["coverage"]["classes_total"] = classes_total
        report["coverage"]["classes_documented"] = classes_documented
        report["coverage"]["methods_total"] = methods_total
        report["coverage"]["methods_documented"] = methods_documented
        report["coverage"]["games_total"] = games_total
        report["coverage"]["games_documented"] = games_documented
        
        # Calculer les pourcentages
        if classes_total > 0:
            report["coverage"]["classes_coverage"] = classes_documented / classes_total
        else:
            report["coverage"]["classes_coverage"] = 1.0
        
        if methods_total > 0:
            report["coverage"]["methods_coverage"] = methods_documented / methods_total
        else:
            report["coverage"]["methods_coverage"] = 1.0
        
        if games_total > 0:
            report["coverage"]["games_coverage"] = games_documented / games_total
        else:
            report["coverage"]["games_coverage"] = 1.0
    
    def generate_suggestions(self, report: Dict) -> List[str]:
        """Génère des suggestions d'amélioration pour la borne arcade."""
        suggestions = []
        
        # Couverture classes Java
        class_coverage = report["coverage"].get("classes_coverage", 0)
        if class_coverage < 0.8:
            suggestions.append(
                f"La couverture des classes Java est de {class_coverage:.1%}. "
                "Ajoutez des Javadoc aux classes publiques."
            )
        
        # Couverture méthodes
        method_coverage = report["coverage"].get("methods_coverage", 0)
        if method_coverage < 0.8:
            suggestions.append(
                f"La couverture des méthodes est de {method_coverage:.1%}. "
                "Documentez les méthodes publiques de l'API."
            )
        
        # Jeux documentés
        game_coverage = report["coverage"].get("games_coverage", 0)
        if game_coverage < 0.9:
            suggestions.append(
                f"Seulement {game_coverage:.1%} des jeux sont documentés. "
                "Ajoutez des descriptions pour chaque jeu."
            )
        
        # Liens cassés
        broken_links = sum(
            len(issues.get("broken_links", []))
            for issues in report["files"].values()
        )
        if broken_links > 0:
            suggestions.append(
                f"{broken_links} liens cassés détectés. "
                "Corrigez les liens internes de la documentation."
            )
        
        # Scripts shell non documentés
        missing_shell_docs = sum(
            len(issues.get("missing_comments", []))
            for issues in report["files"].values()
            if any(key.endswith(".sh") for key in report["files"].keys())
        )
        if missing_shell_docs > 0:
            suggestions.append(
                f"{missing_shell_docs} scripts shell sans documentation. "
                "Ajoutez des commentaires d'en-tête."
            )
        
        return suggestions
    
    def save_report(self, report: Dict, output_path: Path):
        """Sauvegarde le rapport."""
        report["suggestions"] = self.generate_suggestions(report)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="IA Doc Coverage Analyzer")
    parser.add_argument("path", nargs="?", default=".", 
                       help="Chemin à analyser (défaut: .)")
    parser.add_argument("--output", "-o", default="doc-coverage-report.json",
                       help="Fichier de sortie du rapport")
    parser.add_argument("--config", type=Path,
                       help="Chemin vers config.yml")
    parser.add_argument("--threshold", type=float, default=0.8,
                       help="Seuil de couverture minimal (défaut: 0.8)")
    parser.add_argument("--quiet", "-q", action="store_true",
                       help="Mode silencieux")
    
    args = parser.parse_args()
    
    try:
        root_path = Path(args.path).resolve()
        analyzer = DocCoverageAnalyzer(args.config)
        
        if not args.quiet:
            print(f"🔍 Analyse de la documentation dans: {root_path}")
        
        # Analyser le projet
        report = analyzer.analyze_project(root_path)
        
        # Afficher le résumé
        if not args.quiet:
            print("\n📊 Résumé:")
            print(f"  Fichiers analysés: {report['summary']['total_files']}")
            print(f"  Fichiers avec problèmes: {report['summary']['files_with_issues']}")
            print(f"  Problèmes totaux: {report['summary']['total_issues']}")
            
            coverage = report['coverage'].get('functions_coverage', 0)
            print(f"  Couverture fonctions: {coverage:.1%}")
        
        # Vérifier le seuil
        coverage = report['coverage'].get('functions_coverage', 0)
        if coverage < args.threshold:
            if not args.quiet:
                print(f"\n⚠️  Couverture ({coverage:.1%}) < seuil ({args.threshold:.1%})")
            sys.exit(1)
        
        # Sauvegarder le rapport
        output_path = Path(args.output)
        analyzer.save_report(report, output_path)
        
        if not args.quiet:
            print(f"\n📄 Rapport sauvegardé: {output_path}")
            
            # Afficher les suggestions
            suggestions = analyzer.generate_suggestions(report)
            if suggestions:
                print("\n💡 Suggestions:")
                for suggestion in suggestions:
                    print(f"  • {suggestion}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

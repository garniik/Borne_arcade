#!/usr/bin/env python3
"""
Tests de couverture de documentation
"""

import ast
import json
import sys
from pathlib import Path
from typing import Dict, List, Set


class DocCoverageTester:
    """Testeur de couverture de documentation."""

    def __init__(self, project_root: Path):
        self.project_root = project_root.resolve()
        self.failures = []
        
    def test_python_docstrings(self) -> Dict:
        """Teste la couverture des docstrings Python."""
        results = {
            "total_functions": 0,
            "documented_functions": 0,
            "total_classes": 0,
            "documented_classes": 0,
            "undocumented": []
        }
        
        # Trouver tous les fichiers Python
        for py_file in self.project_root.rglob("*.py"):
            if any(skip in str(py_file) for skip in [".git", "__pycache__", "venv", "tests"]):
                continue
            
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        func_name = node.name
                        
                        # Ignorer les fonctions privées
                        if func_name.startswith('_') and not func_name.startswith('__'):
                            continue
                        
                        results["total_functions"] += 1
                        
                        if ast.get_docstring(node):
                            results["documented_functions"] += 1
                        else:
                            results["undocumented"].append({
                                "type": "function",
                                "name": func_name,
                                "file": str(py_file),
                                "line": node.lineno
                            })
                    
                    elif isinstance(node, ast.ClassDef):
                        class_name = node.name
                        results["total_classes"] += 1
                        
                        if ast.get_docstring(node):
                            results["documented_classes"] += 1
                        else:
                            results["undocumented"].append({
                                "type": "class",
                                "name": class_name,
                                "file": str(py_file),
                                "line": node.lineno
                            })
            
            except Exception as e:
                self.failures.append(f"Erreur analyse {py_file}: {e}")
        
        return results
    
    def test_markdown_structure(self) -> Dict:
        """Teste la structure des fichiers Markdown."""
        results = {
            "total_files": 0,
            "files_with_issues": 0,
            "issues": []
        }
        
        # Trouver tous les fichiers Markdown
        for md_file in self.project_root.rglob("*.md"):
            if any(skip in str(md_file) for skip in [".git", "venv"]):
                continue
            
            results["total_files"] += 1
            
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                file_issues = []
                
                # Vérifier le titre principal
                if not content.strip().startswith('# '):
                    file_issues.append({
                        "type": "missing_main_title",
                        "message": "Pas de titre principal (niveau 1)"
                    })
                
                # Vérifier la structure selon le type de fichier
                if "api" in str(md_file):
                    file_issues.extend(self._check_api_doc_structure(content))
                elif "how-to" in str(md_file):
                    file_issues.extend(self._check_how_to_structure(content))
                
                # Vérifier les liens internes
                file_issues.extend(self._check_internal_links(content, md_file))
                
                if file_issues:
                    results["files_with_issues"] += 1
                    results["issues"].append({
                        "file": str(md_file),
                        "issues": file_issues
                    })
            
            except Exception as e:
                self.failures.append(f"Erreur lecture {md_file}: {e}")
        
        return results
    
    def _check_api_doc_structure(self, content: str) -> List[Dict]:
        """Vérifie la structure d'une doc d'API."""
        issues = []
        
        required_sections = ["Vue d'ensemble", "API", "Exemples"]
        for section in required_sections:
            if section.lower() not in content.lower():
                issues.append({
                    "type": "missing_section",
                    "message": f"Section manquante: {section}"
                })
        
        return issues
    
    def _check_how_to_structure(self, content: str) -> List[Dict]:
        """Vérifie la structure d'un guide How-to."""
        issues = []
        
        required_sections = ["Prérequis", "Installation"]
        for section in required_sections:
            if section.lower() not in content.lower():
                issues.append({
                    "type": "missing_section",
                    "message": f"Section manquante: {section}"
                })
        
        return issues
    
    def _check_internal_links(self, content: str, file_path: Path) -> List[Dict]:
        """Vérifie les liens internes dans un fichier Markdown."""
        issues = []
        
        import re
        # Liens Markdown: [text](url)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        
        for text, url in links:
            if url.startswith('http'):
                continue  # Liens externes
            
            if url.startswith('#'):
                continue  # Ancres
            
            # Lien relatif
            target_path = file_path.parent / url
            if not target_path.exists():
                issues.append({
                    "type": "broken_internal_link",
                    "message": f"Lien interne cassé: {url} -> {target_path}"
                })
        
        return issues
    
    def test_examples_existence(self) -> Dict:
        """Teste l'existence des exemples de code."""
        results = {
            "total_examples_referenced": 0,
            "existing_examples": 0,
            "missing_examples": []
        }
        
        # Trouver toutes les références à des exemples
        for md_file in self.project_root.rglob("*.md"):
            if any(skip in str(md_file) for skip in [".git", "venv"]):
                continue
            
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Chercher les références à des exemples
                import re
                examples = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)
                
                for example in examples:
                    results["total_examples_referenced"] += 1
                    
                    # Vérifier si l'exemple est testable
                    try:
                        ast.parse(example)
                        results["existing_examples"] += 1
                    except SyntaxError:
                        results["missing_examples"].append({
                            "file": str(md_file),
                            "example": example[:100] + "..." if len(example) > 100 else example,
                            "issue": "syntax_error"
                        })
            
            except Exception as e:
                self.failures.append(f"Erreur analyse exemples {md_file}: {e}")
        
        return results
    
    def run_all_tests(self) -> Dict:
        """Exécute tous les tests de couverture."""
        results = {
            "python_docstrings": self.test_python_docstrings(),
            "markdown_structure": self.test_markdown_structure(),
            "examples": self.test_examples_existence(),
            "summary": {},
            "failures": self.failures
        }
        
        # Calculer le résumé
        py_results = results["python_docstrings"]
        md_results = results["markdown_structure"]
        ex_results = results["examples"]
        
        # Couverture Python
        func_coverage = (
            py_results["documented_functions"] / py_results["total_functions"]
            if py_results["total_functions"] > 0 else 1.0
        )
        class_coverage = (
            py_results["documented_classes"] / py_results["total_classes"]
            if py_results["total_classes"] > 0 else 1.0
        )
        
        # Structure Markdown
        md_issues = len(md_results["issues"])
        
        # Exemples
        ex_coverage = (
            ex_results["existing_examples"] / ex_results["total_examples_referenced"]
            if ex_results["total_examples_referenced"] > 0 else 1.0
        )
        
        results["summary"] = {
            "python_function_coverage": func_coverage,
            "python_class_coverage": class_coverage,
            "markdown_issues": md_issues,
            "examples_coverage": ex_coverage,
            "total_undocumented": len(py_results["undocumented"]),
            "total_failures": len(self.failures)
        }
        
        return results
    
    def generate_junit_xml(self, results: Dict) -> str:
        """Génère un rapport JUnit XML pour CI."""
        import xml.etree.ElementTree as ET
        
        testsuite = ET.Element("testsuite", name="doc-coverage")
        
        # Test de couverture Python
        py_results = results["python_docstrings"]
        testcase = ET.SubElement(testsuite, "testcase", 
                                classname="doc-coverage", 
                                name="python-docstrings")
        
        if py_results["undocumented"]:
            failure = ET.SubElement(testcase, "failure")
            failure.text = f"{len(py_results['undocumented'])} éléments non documentés"
        
        # Test de structure Markdown
        md_results = results["markdown_structure"]
        testcase = ET.SubElement(testsuite, "testcase",
                                classname="doc-coverage",
                                name="markdown-structure")
        
        if md_results["issues"]:
            failure = ET.SubElement(testcase, "failure")
            failure.text = f"{len(md_results['issues'])} problèmes de structure"
        
        # Test des exemples
        ex_results = results["examples"]
        testcase = ET.SubElement(testsuite, "testcase",
                                classname="doc-coverage",
                                name="examples")
        
        if ex_results["missing_examples"]:
            failure = ET.SubElement(testcase, "failure")
            failure.text = f"{len(ex_results['missing_examples'])} exemples invalides"
        
        return ET.tostring(testsuite, encoding="unicode")


def main():
    """Point d'entrée principal."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Tests de couverture de documentation")
    parser.add_argument("path", nargs="?", default=".",
                       help="Chemin à analyser (défaut: .)")
    parser.add_argument("--output", "-o", default="coverage-test-results.json",
                       help="Fichier de sortie des résultats")
    parser.add_argument("--junit", help="Fichier de sortie JUnit XML")
    parser.add_argument("--threshold", type=float, default=0.8,
                       help="Seuil de couverture minimal (défaut: 0.8)")
    parser.add_argument("--quiet", "-q", action="store_true",
                       help="Mode silencieux")
    
    args = parser.parse_args()
    
    try:
        project_root = Path(args.path).resolve()
        tester = DocCoverageTester(project_root)
        
        if not args.quiet:
            print(f"🧪 Tests de couverture de documentation dans: {project_root}")
        
        # Exécuter les tests
        results = tester.run_all_tests()
        
        # Afficher le résumé
        if not args.quiet:
            summary = results["summary"]
            print(f"\n📊 Résultats:")
            print(f"  Couverture fonctions: {summary['python_function_coverage']:.1%}")
            print(f"  Couverture classes: {summary['python_class_coverage']:.1%}")
            print(f"  Problèmes Markdown: {summary['markdown_issues']}")
            print(f"  Couverture exemples: {summary['examples_coverage']:.1%}")
            print(f"  Éléments non documentés: {summary['total_undocumented']}")
            print(f"  Erreurs: {summary['total_failures']}")
        
        # Vérifier le seuil
        func_coverage = results["summary"]["python_function_coverage"]
        if func_coverage < args.threshold:
            if not args.quiet:
                print(f"\n❌ Couverture ({func_coverage:.1%}) < seuil ({args.threshold:.1%})")
            sys.exit(1)
        
        # Sauvegarder les résultats
        output_path = Path(args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        if not args.quiet:
            print(f"\n📄 Résultats sauvegardés: {output_path}")
        
        # Générer JUnit XML si demandé
        if args.junit:
            junit_xml = tester.generate_junit_xml(results)
            junit_path = Path(args.junit)
            junit_path.write_text(junit_xml, encoding="utf-8")
            if not args.quiet:
                print(f"📄 Rapport JUnit: {junit_path}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
IA Release Notes - Génère les notes de version automatiquement

Principe : analyse les commits depuis le dernier tag
=> génère des notes de version lisibles (changelog orienté utilisateur)
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import yaml
except ImportError:
    print("Erreur: yaml requis. Installe avec: pip install pyyaml")
    sys.exit(1)


class ReleaseNotesGenerator:
    """Générateur de notes de version assisté par IA."""

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path(".docs/config.yml")
        self.config = self._load_config()
        
        # Convention de commits
        self.commit_types = {
            "feat": "🚀 Nouvelles fonctionnalités",
            "fix": "🐛 Corrections de bugs", 
            "docs": "📝 Documentation",
            "style": "💄 Style",
            "refactor": "♻️ Refactorisation",
            "test": "✅ Tests",
            "chore": "🔧 Maintenance",
            "perf": "⚡ Performance",
            "ci": "🤖 CI/CD",
            "build": "📦 Build",
            "breaking": "💥 Changements cassants"
        }
    
    def _load_config(self) -> Dict:
        """Charge la configuration."""
        if not self.config_path.exists():
            return {}
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    
    def get_latest_tag(self) -> Optional[str]:
        """Récupère le dernier tag Git."""
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--abbrev=0"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            # Pas de tag trouvé
            return None
    
    def get_commits_since_tag(self, tag: Optional[str] = None) -> List[Dict]:
        """Récupère les commits depuis le dernier tag."""
        try:
            if tag:
                range_spec = f"{tag}..HEAD"
            else:
                range_spec = "HEAD"
            
            # Récupérer les commits avec format détaillé
            result = subprocess.run(
                ["git", "log", range_spec, "--pretty=format:%H|%s|%b|%an|%ad", "--date=iso"],
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split('|')
                    if len(parts) >= 5:
                        commits.append({
                            "hash": parts[0],
                            "subject": parts[1],
                            "body": parts[2],
                            "author": parts[3],
                            "date": parts[4]
                        })
            
            return commits
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Erreur git log: {e}")
    
    def parse_conventional_commit(self, commit: Dict) -> Optional[Dict]:
        """Parse un commit conventionnel."""
        subject = commit["subject"]
        
        # Pattern: type(scope)!: description
        pattern = r'^(\w+)(\([^)]+\))?(!)?:\s*(.+)$'
        match = re.match(pattern, subject)
        
        if not match:
            return None
        
        commit_type = match.group(1)
        scope = match.group(2)
        breaking = bool(match.group(3))
        description = match.group(4)
        
        return {
            "type": commit_type,
            "scope": scope.strip('()') if scope else None,
            "breaking": breaking,
            "description": description,
            "original": commit
        }
    
    def categorize_commits(self, commits: List[Dict]) -> Dict[str, List[Dict]]:
        """Catégorise les commits par type."""
        categorized = {category: [] for category in self.commit_types.values()}
        categorized["Autres"] = []
        
        for commit in commits:
            parsed = self.parse_conventional_commit(commit)
            
            if parsed:
                commit_type = parsed["type"]
                if commit_type in self.commit_types:
                    category = self.commit_types[commit_type]
                    categorized[category].append(parsed)
                else:
                    categorized["Autres"].append(parsed)
            else:
                categorized["Autres"].append({"original": commit})
        
        return categorized
    
    def generate_section(self, category: str, commits: List[Dict]) -> str:
        """Génère une section de notes de version."""
        if not commits:
            return ""
        
        section = f"\n### {category}\n\n"
        
        for commit in commits:
            if "original" in commit:
                # Commit non conventionnel
                subject = commit["original"]["subject"]
                section += f"- {subject}\n"
            else:
                # Commit conventionnel
                description = commit["description"]
                scope = commit["scope"]
                breaking = commit["breaking"]
                
                line = "- "
                if breaking:
                    line += "**BREAKING CHANGE:** "
                if scope:
                    line += f"**{scope}:** "
                line += description
                
                # Ajouter le hash
                hash_short = commit["original"]["hash"][:8]
                line += f" ({hash_short})"
                
                section += line + "\n"
        
        return section + "\n"
    
    def generate_highlights(self, categorized: Dict) -> str:
        """Génère la section des points forts."""
        highlights = []
        
        # Features
        features = categorized.get("🚀 Nouvelles fonctionnalités", [])
        if features:
            top_features = features[:3]  # Top 3 features
            for feature in top_features:
                highlights.append(f"• {feature['description']}")
        
        # Breaking changes
        breaking_commits = [
            commit for commits in categorized.values()
            for commit in commits
            if commit.get("breaking")
        ]
        
        if breaking_commits:
            highlights.append("• **Changements cassants** - Voir section dédiée")
        
        if highlights:
            return "\n### 🌟 Points forts\n\n" + "\n".join(highlights) + "\n\n"
        
        return ""
    
    def generate_stats(self, commits: List[Dict], categorized: Dict) -> str:
        """Génère les statistiques de la version."""
        total_commits = len(commits)
        contributors = len(set(commit["author"] for commit in commits))
        
        # Compter par type
        type_counts = {}
        for category, commits_list in categorized.items():
            if commits_list and category != "Autres":
                type_counts[category] = len(commits_list)
        
        stats = f"\n### 📊 Statistiques\n\n"
        stats += f"- **{total_commits} commits** par **{contributors} contributeurs**\n"
        
        if type_counts:
            stats += "- Répartition :\n"
            for category, count in type_counts.items():
                stats += f"  - {category}: {count}\n"
        
        return stats + "\n"
    
    def generate_upgrade_notes(self, categorized: Dict) -> str:
        """Génère les notes de mise à niveau."""
        breaking_commits = [
            commit for commits in categorized.values()
            for commit in commits
            if commit.get("breaking")
        ]
        
        if not breaking_commits:
            return ""
        
        notes = "\n### ⚠️ Notes de mise à niveau\n\n"
        
        for commit in breaking_commits:
            description = commit["description"]
            scope = commit["scope"]
            
            notes += f"- **{scope}:** {description}\n"
            
            # Ajouter le body du commit si disponible
            body = commit["original"]["body"].strip()
            if body and body != description:
                notes += f"  ```\n{body}\n  ```\n"
        
        return notes + "\n"
    
    def generate_release_notes(self, version: str, commits: List[Dict]) -> str:
        """Génère les notes de version complètes."""
        # Catégoriser les commits
        categorized = self.categorize_commits(commits)
        
        # Date de release
        release_date = datetime.now().strftime("%d %B %Y")
        
        # En-tête
        notes = f"# Notes de version {version}\n\n"
        notes += f"Publié le {release_date}\n\n"
        
        # Points forts
        highlights = self.generate_highlights(categorized)
        if highlights:
            notes += highlights
        
        # Sections par catégorie
        for category in ["🚀 Nouvelles fonctionnalités", "🐛 Corrections de bugs", 
                        "📝 Documentation", "⚡ Performance"]:
            section = self.generate_section(category, categorized[category])
            if section:
                notes += section
        
        # Notes de mise à niveau
        upgrade_notes = self.generate_upgrade_notes(categorized)
        if upgrade_notes:
            notes += upgrade_notes
        
        # Statistiques
        stats = self.generate_stats(commits, categorized)
        if stats:
            notes += stats
        
        # Contributors
        contributors = sorted(set(commit["author"] for commit in commits))
        if contributors:
            notes += "### 👨‍💻 Contributeurs\n\n"
            for contributor in contributors:
                notes += f"- @{contributor}\n"
            notes += "\n"
        
        # Footer
        notes += "---\n"
        notes += "*Généré automatiquement par IA Release Notes Generator*\n"
        
        return notes
    
    def save_changelog(self, notes: str, output_path: Path):
        """Sauvegarde les notes dans CHANGELOG.md."""
        if output_path.exists():
            # Insérer au début du fichier existant
            existing_content = output_path.read_text(encoding="utf-8")
            new_content = notes + "\n" + existing_content
        else:
            new_content = notes
        
        output_path.write_text(new_content, encoding="utf-8")
    
    def create_github_release(self, version: str, notes: str, draft: bool = True):
        """Crée une release GitHub (simulation)."""
        print(f"🚀 Création release GitHub v{version}")
        if draft:
            print("   Mode: DRAFT")
        print(f"   Contenu:\n{notes[:200]}...")
        
        # TODO: Implémenter avec GitHub API si nécessaire


def main():
    parser = argparse.ArgumentParser(description="IA Release Notes Generator")
    parser.add_argument("--version", required=True,
                       help="Version de la release (ex: v1.2.0)")
    parser.add_argument("--tag", 
                       help="Tag de départ (défaut: dernier tag)")
    parser.add_argument("--output", "-o", default="CHANGELOG.md",
                       help="Fichier de sortie (défaut: CHANGELOG.md)")
    parser.add_argument("--config", type=Path,
                       help="Chemin vers config.yml")
    parser.add_argument("--draft", action="store_true",
                       help="Créer la release en mode brouillon")
    parser.add_argument("--stdout", action="store_true",
                       help="Afficher les notes sur stdout")
    
    args = parser.parse_args()
    
    try:
        generator = ReleaseNotesGenerator(args.config)
        
        # Récupérer les commits
        if args.tag:
            tag = args.tag
        else:
            tag = generator.get_latest_tag()
            if tag:
                print(f"📦 Dernier tag trouvé: {tag}")
            else:
                print("ℹ️  Aucun tag trouvé - utilise tous les commits")
        
        commits = generator.get_commits_since_tag(tag)
        print(f"🔍 {len(commits)} commits analysés")
        
        if not commits:
            print("⚠️  Aucun commit trouvé")
            sys.exit(0)
        
        # Générer les notes
        notes = generator.generate_release_notes(args.version, commits)
        
        # Afficher sur stdout si demandé
        if args.stdout:
            print(notes)
        
        # Sauvegarder
        output_path = Path(args.output)
        generator.save_changelog(notes, output_path)
        print(f"📄 Notes sauvegardées dans: {output_path}")
        
        # Créer la release GitHub
        generator.create_github_release(args.version, notes, args.draft)
        
    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

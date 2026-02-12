# Documentation - Borne Arcade

> **Principe clé** : "Docs-as-Code" + IA qui propose, jamais qui impose  
> La documentation vit dans le dépôt Git, versionnée comme le code, revue via PR, publiée via CI/CD.

## 📁 Arborescence

```
documentation/
├── README.md                     # Ce fichier
├── .docs/                        # Config et outils Docs-as-Code
│   ├── .gitkeep
│   ├── config.yml                # Config globale (style, IA, CI)
│   ├── .gitignore                # Ignorer les builds/temp
│   └── .editorconfig             # Style d'écriture
├── src/                          # Sources de la doc (Markdown, etc.)
│   ├── index.md                  # Page d'accueil
│   ├── how-to/
│   │   ├── install.md            # How-to : installation
│   │   └── create-deploy-game.md # How-to : créer et déployer un jeu
│   ├── api/
│   │   └── ollama-wrapper.md     # Doc API wrapper Ollama
│   └── guides/
│       └── docs-as-code.md       # Guide Docs-as-Code
├── scripts/                      # Scripts d'automatisation (IA)
│   ├── ia-doc-patch.py           # IA : génère patches de doc sur PR
│   ├── ia-doc-coverage.py        # IA : détecte trous dans la doc
│   └── ia-release-notes.py       # IA : notes de version auto
├── .github/                      # CI/CD et workflows GitHub
│   └── workflows/
│       ├── docs-on-pr.yml        # PR : IA propose patches doc
│       ├── docs-publish.yml      # push main : publie la doc
│       └── docs-nightly.yml      # schedule : IA + lint + rapports
├── tests/                        # Tests de la documentation
│   ├── test_links.py             # Vérifie liens internes/externes
│   ├── test_coverage.py          # Vérifie couverture doc
│   └── fixtures/                 # Exemples pour tests
└── examples/                     # Exemples et snippets
    ├── ollama_wrapper_usage.py   # Exemple d'utilisation du wrapper
    └── templates/                # Templates PR, issues, etc.
        ├── pr_template.md        # Template PR avec checklist doc
        └── issue_template.md     # Template issue
```

## 🚀 Workflow Git

| Déclencheur | Action | Rôle de l'IA |
|-------------|--------|--------------|
| **PR** | Vérifie et propose mises à jour de doc | Patch sur docs/ + résumé changements |
| **push sur main** | Publie la doc | (optionnel) génère release notes |
| **schedule (nightly)** | IA + lint doc + rapports | Lint, couverture, suggestions |

## 🛡️ Garde-fous qualité

- **pre-commit / Husky** : empêche d'oublier la doc localement
- **PR template** avec checklist "doc mise à jour ?"
- **Approvals obligatoires** avant merge (GitHub rulesets)
- **Tests automatiques** sur la doc (liens, couverture, style)

## 📋 Règle d'or

> **Merge interdit tant que la doc n'est pas validée par tests + review (humain)**

---

## 📖 Comment contribuer

1. **Cloner** le dépôt
2. **Installer** les dépendances de doc (cf `how-to/install.md`)
3. **Configurer** le pre-commit (cf `src/guides/docs-as-code.md`)
4. **Créer une branche** et modifier la doc
5. **Ouvrir une PR** : l'IA proposera des améliorations automatiquement
6. **Faire reviewer** et merger une fois validé

---

## 🤖 Où l'IA intervient exactement

### Usage 1 — "Doc patch" sur une PR

- **Entrées IA** : git diff du code, fichiers de doc liés, style guide
- **Sortie IA** : patch sur docs/ + message PR (résumé + points à vérifier)
- **Action** : l'IA crée un commit dans la branche PR ou ouvre une PR dédiée "docs update"

### Usage 2 — "Doc coverage" (détection de trous)

- Repère : fonctions publiques sans docstring, endpoints non documentés, exemples manquants
- Génère : rapports et suggestions de remplissage

### Usage 3 — "Release notes" automatiques

- À chaque tag/version : compile les commits (conventionnels)
- L'IA reformule en notes lisibles (changelog orienté utilisateur)

---

## 📚 Liens utiles

- [Guide Docs-as-Code](src/guides/docs-as-code.md)
- [How-to : Installation](src/how-to/install.md)
- [How-to : Créer et déployer un jeu](src/how-to/create-deploy-game.md)
- [API Ollama Wrapper](src/api/ollama-wrapper.md)
- [Templates PR/Issues](examples/templates/)

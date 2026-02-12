# Borne Arcade - Documentation

Bienvenue dans la documentation de la Borne Arcade. Ce projet suit une approche **Docs-as-Code** avec assistance IA pour proposer des améliorations sans jamais imposer.

## 🚀 Démarrage rapide

- [**Installation**](how-to/install.md) - Mettre en place l'environnement
- [**Créer et déployer un jeu**](how-to/create-deploy-game.md) - Guide pas à pas
- [**API Ollama Wrapper**](api/ollama-wrapper.md) - Référence de l'API

## 📖 Guides

- [**Docs-as-Code**](guides/docs-as-code.md) - Principes et workflow

## 🤖 Fonctionnalités IA

L'IA assiste la documentation sans jamais remplacer l'humain :

- **Patches de doc** sur chaque PR (propositions de mise à jour)
- **Détection de trous** dans la documentation
- **Notes de version** automatiques

> **Règle d'or** : la documentation est versionnée, testée et reviewée comme le code.

---

## 📁 Structure

```
src/
├── how-to/          # Guides pratiques
├── api/             # Références d'API
└── guides/          # Concepts et workflow
```

---

## 🛡️ Qualité

- Tests automatiques (liens, couverture, style)
- PR template avec checklist documentation
- Approbations requises avant merge
- Lint et formatage automatiques

---

*Pour contribuer, voir le [guide Docs-as-Code](guides/docs-as-code.md).*

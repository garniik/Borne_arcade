# How-to : Installation

Guide d'installation complet pour la Borne Arcade.

## Prérequis

- **Python 3.11+**
- **Git**
- **Ollama** (pour l'IA locale)

## 🐋 Installation rapide

```bash
# Clone du dépôt
git clone https://github.com/garniik/Borne_arcade.git
cd Borne_arcade

# Installation Python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Installation Ollama (si non installé)
curl -fsSL https://ollama.ai/install.sh | sh
```

## ⚙️ Configuration

### 1. Ollama

```bash
# Démarrer le serveur Ollama
ollama serve

# Télécharger un modèle (exemple)
ollama pull gemma2:latest
```

### 2. Variables d'environnement

```bash
# Créer .env
cp .env.example .env
# Éditer .env avec tes configurations
```

### 3. Pre-commit (Docs-as-Code)

```bash
# Installation hooks
pre-commit install

# Test des hooks
pre-commit run --all-files
```

## ✅ Vérification

```python
# Test rapide
from documentation.src.ollama_wrapper_iut import OllamaWrapper

client = OllamaWrapper()
print("Server running?", client.is_server_running())
print("Version:", client.get_version())
```

## 📦 Dépendances principales

- **OllamaWrapper** - Client API Ollama
- **FastAPI** - Serveur web
- **Pydantic** - Validation données
- **MkDocs** - Génération documentation

---

## 🚯 Problèmes courants

| Problème | Solution |
|----------|----------|
| `ollama: command not found` | Ajouter Ollama au PATH ou réinstaller |
| `ModuleNotFoundError` | Activer venv et vérifier requirements.txt |
| Port 11434 occupé | Changer port dans config ou arrêter autre instance |

---

*Pour la suite, voir [Créer et déployer un jeu](create-deploy-game.md).*

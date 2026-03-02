# 🤖 Générateur de Documentation Automatique

Un système d'analyse et de génération automatique de documentation basé sur l'architecture **RAG (Retrieval-Augmented Generation)** pour le projet borne d'arcade.

## 📋 Vue d'ensemble

Ce système combine :
- **Analyse statique de code** : Scan et extraction des composants du projet
- **Recherche sémantique** : Utilisation d'embeddings pour trouver le code pertinent
- **Génération assistée par LLM** : Création de documentation structurée et contextuelle

## 🏗️ Architecture RAG

```
┌─────────────────────────────────────────────────────────────┐
│                     PROJET BORNE_ARCADE                      │
│  (fichiers .py, .c, .js, .json, .md, configs, etc.)        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              PHASE 1 : ANALYSE DU PROJET                     │
│                                                              │
│  ProjectAnalyzer:                                           │
│  - Scan récursif de l'arborescence                         │
│  - Identification des fichiers pertinents                   │
│  - Extraction des fragments de code (fonctions, classes)    │
│  - Classification par langage et type                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         PHASE 2 : INDEXATION SÉMANTIQUE (Retrieval)         │
│                                                              │
│  SemanticSearchEngine:                                      │
│  - Transformation des fragments en embeddings               │
│  - Stockage dans un index vectoriel                        │
│  - Cache persistant pour optimisation                       │
│                                                              │
│  Modèle: nomic-embed-text (ou équivalent)                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            PHASE 3 : GÉNÉRATION (Generation)                │
│                                                              │
│  DocumentationGenerator:                                    │
│  Pour chaque section de documentation:                      │
│    1. Requête sémantique → Top-K fragments pertinents      │
│    2. Construction du prompt RAG avec contexte             │
│    3. Génération par LLM (gemma2, llama, etc.)             │
│    4. Formatage markdown avec références                    │
│                                                              │
│  Modèle: gemma2:latest (ou équivalent)                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   OUTPUT : doc.md                           │
│                                                              │
│  Documentation complète avec :                              │
│  - Vue d'ensemble du projet                                │
│  - Structure et architecture                                │
│  - Guide d'installation et utilisation                     │
│  - Références aux fichiers sources                          │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Composants Principaux

### 1. **ProjectAnalyzer**
Responsable de l'analyse du projet :
- Scan récursif avec exclusion des dossiers inutiles (`.git`, `__pycache__`, etc.)
- Support multi-langages : Python, C/C++, JavaScript, JSON, Markdown, etc.
- Extraction intelligente des fragments (fonctions, classes, modules)

### 2. **SemanticSearchEngine**
Moteur de recherche sémantique :
- Calcul des embeddings via Ollama `/api/embed`
- Cache persistant en JSON pour éviter les recalculs
- Recherche par similarité cosinus
- Retourne les Top-K fragments les plus pertinents

### 3. **DocumentationGenerator**
Générateur de documentation :
- Stratégie de génération par sections thématiques
- Prompts RAG structurés avec contexte
- Génération via Ollama `/api/generate`
- Formatage markdown professionnel
- Traçabilité : références aux fichiers sources

## 📦 Installation

### Prérequis
- Python 3.8+
- Ollama installé et accessible
- Modèles Ollama téléchargés :
  ```bash
  ollama pull nomic-embed-text
  ollama pull gemma2:latest
  ```

### Structure des fichiers
```
Automatisation/
├── ollama/
│   ├── ollama_wrapper_iut.py  # Wrapper fourni
│   ├── doc_generator.py       # Système principal
│   ├── example_usage.py       # Exemple d'utilisation
│   └── doc.md                 # Documentation générée
```

## 🚀 Utilisation

### Mode ligne de commande

```bash
# Générer la documentation du projet borne_arcade
python doc_generator.py ../borne_arcade doc.md

# Avec un serveur Ollama personnalisé
python doc_generator.py ../borne_arcade doc.md --ollama-url http://localhost:11434
```

### Mode programmatique

```python
from doc_generator import generate_project_documentation

# Génération simple
output = generate_project_documentation(
    project_path="../borne_arcade",
    output_file="doc.md"
)

# Avec configuration personnalisée
output = generate_project_documentation(
    project_path="../borne_arcade",
    output_file="doc.md",
    ollama_url="http://10.22.28.190:11434"
)
```

### Analyse interactive

```python
from doc_generator import ProjectAnalyzer, SemanticSearchEngine, DocumentationGenerator
from ollama_wrapper_iut import OllamaWrapper

# Initialisation
wrapper = OllamaWrapper()
analyzer = ProjectAnalyzer("../borne_arcade")

# Analyse
files = analyzer.scan_project()
fragments = analyzer.extract_code_fragments()

# Recherche manuelle
search_engine = SemanticSearchEngine(wrapper, "nomic-embed-text:latest")
search_engine.index_fragments(fragments)

results = search_engine.search("Comment gérer l'affichage graphique?", fragments, top_k=3)
for fragment, score in results:
    print(f"[{score:.3f}] {fragment.file_path}")
```

## 📊 Exemple de sortie

La documentation générée contient :

```markdown
# Documentation du Projet - Borne d'Arcade

*Documentation générée automatiquement*

---

## Vue d'ensemble du projet

[Description générée par le LLM basée sur les fragments analysés]

### 📎 Fichiers de référence
- `main.py` (pertinence: 0.87)
- `config.json` (pertinence: 0.82)
- `README.md` (pertinence: 0.78)

## Structure des fichiers

[Analyse de l'organisation du projet]

### 📎 Fichiers de référence
- `src/core/engine.py` (pertinence: 0.91)
- `src/utils/loader.py` (pertinence: 0.85)

[... autres sections ...]
```

## 🎯 Avantages du RAG

### Par rapport à un LLM seul
- ✅ **Pas d'hallucinations** : Réponses basées uniquement sur le code réel
- ✅ **Contexte contrôlé** : Le LLM voit uniquement les parties pertinentes
- ✅ **Traçabilité** : Chaque information est reliée à son fichier source
- ✅ **À jour** : Analyse le code actuel, pas une version ancienne

### Par rapport à de la génération de doc classique
- ✅ **Compréhension sémantique** : Trouve les liens entre concepts
- ✅ **Rédaction naturelle** : Documentation rédigée en langage humain
- ✅ **Adaptabilité** : Génère différents types de sections
- ✅ **Intelligence contextuelle** : Comprend l'architecture globale

## ⚙️ Configuration

### Personnalisation des sections

Modifiez la liste `sections` dans `DocumentationGenerator.generate_documentation()` :

```python
sections = [
    ("Titre de la section", "Requête pour trouver le code pertinent"),
    ("Architecture réseau", "Comment le projet gère les communications réseau"),
    ("Gestion des périphériques", "Interaction avec les contrôleurs et boutons"),
]
```

### Ajustement des paramètres RAG

```python
# Nombre de fragments retournés par recherche
relevant_fragments = search_engine.search(query, fragments, top_k=5)

# Longueur maximale du contexte
# (modifier dans _build_rag_prompt pour limiter le nombre de fragments)
```

## 🔍 Analyse Critique

### Points forts
1. **Réduction des hallucinations** : Le LLM ne peut inventer que ce qui est dans le code
2. **Documentation toujours synchronisée** : Régénération facile à chaque modification
3. **Qualité des embeddings** : La recherche sémantique trouve des liens non évidents

### Limitations
1. **Qualité dépendante du code** :
   - Code mal commenté → documentation moins précise
   - Code spaghetti → difficulté à extraire la logique
   
2. **Limite de contexte du LLM** :
   - Ne peut pas voir tout le projet simultanément
   - Risque de manquer des dépendances complexes
   
3. **Interprétation parfois incorrecte** :
   - Le LLM peut mal interpréter du code complexe
   - Nécessite une relecture humaine

4. **Performance** :
   - Calcul des embeddings peut être long
   - Génération section par section prend du temps

### Améliorations possibles
- ✨ Ajout de scores de confiance sur les réponses
- ✨ Mode "pas de réponse" si aucun fragment pertinent
- ✨ Analyse des dépendances entre fichiers
- ✨ Génération de diagrammes UML automatiques
- ✨ Détection des fonctionnalités non documentées

## 📚 Cas d'usage

### 1. Documentation initiale
Générer une première version complète de documentation pour un projet existant.

### 2. Mise à jour continue
Régénérer automatiquement après chaque modification importante.

### 3. Onboarding
Créer des guides spécifiques pour les nouveaux développeurs.

### 4. Audit de code
Identifier les parties mal documentées ou incohérentes.

## 🐛 Dépannage

### Le serveur Ollama n'est pas accessible
```bash
# Vérifier qu'Ollama tourne
ollama list

# Démarrer le serveur
ollama serve
```

### Modèle non trouvé
```bash
# Lister les modèles installés
ollama list

# Télécharger un modèle
ollama pull gemma2:latest
ollama pull nomic-embed-text
```

### Erreur d'encodage
- Vérifier que tous les fichiers sources sont en UTF-8
- Les fichiers binaires sont automatiquement ignorés

### Documentation incomplète
- Augmenter `top_k` dans les recherches
- Améliorer les requêtes de recherche dans `sections`
- Vérifier que le code source contient assez d'information

## 📖 Références

- [Documentation Ollama](https://ollama.ai/docs)
- [Architecture RAG](https://www.anthropic.com/research/retrieval-augmented-generation)
- [TP4 - Cours BUT3 INFO](./tp_4.md)

## 👨‍💻 Auteur

Adapté des TPs Ollama - BUT 3 INFO, IUTLCO  
Rémi COZOT - remi.cozot@univ-littoral.fr

---

*Généré avec ❤️ et beaucoup d'embeddings*
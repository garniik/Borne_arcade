# API Ollama Wrapper

Documentation complète du wrapper Python pour l'API Ollama.

## 📖 Vue d'ensemble

`OllamaWrapper` est un client Python robuste et typé pour interagir avec l'API HTTP d'Ollama. Il supporte la génération de texte, les images, et les embeddings.

**Fichier** : `documentation/ollama_wrapper_iut.py`

## 🚀 Démarrage rapide

```python
from documentation.ollama_wrapper_iut import OllamaWrapper

# Initialisation
client = OllamaWrapper(base_url="http://localhost:11434")

# Vérifier le serveur
if client.is_server_running():
    print("Version:", client.get_version())
    
    # Génération de texte
    result = client.generate_text(
        model="gemma2:latest",
        prompt="Quel est le sens de la vie ?"
    )
    print(result.response)
```

## 🏗️ Architecture

### Exceptions
```python
OllamaError                 # Erreur générique
├── OllamaConnectionError   # Problèmes de connexion
├── OllamaResponseError     # Réponses invalides
└── OllamaServerStartError  # Démarrage serveur échoué
```

### Dataclasses
```python
@dataclass
class OllamaModelInfo:
    name: str
    modified_at: Optional[str]
    size: Optional[int]
    digest: Optional[str]
    details: Optional[OllamaModelDetails]

@dataclass
class OllamaGenerateResult:
    response: str
    model: Optional[str]
    done: Optional[bool]
    total_duration: Optional[int]
    # ... autres métriques
```

## 📋 API complète

### Constructeur

```python
OllamaWrapper(
    base_url: str = "http://10.22.28.190:11434",
    timeout_s: float = 120.0
) -> None
```

**Paramètres**
- `base_url` : URL du serveur Ollama
- `timeout_s` : Timeout réseau en secondes

---

### Méthodes système

#### `is_server_running() -> bool`
Vérifie si le serveur Ollama répond.

```python
if client.is_server_running():
    print("Serveur OK")
else:
    print("Serveur indisponible")
```

#### `start_server()` -> `subprocess.Popen`
Démarre le serveur Ollama localement.

```python
process = client.start_server(wait=True, wait_timeout_s=10.0)
# process contient le serveur en arrière-plan
```

---

### Information

#### `get_version() -> str`
Retourne la version du serveur Ollama.

```python
version = client.get_version()  # ex: "0.1.47"
```

#### `list_models() -> List[OllamaModelInfo]`
Liste les modèles installés.

```python
models = client.list_models()
for model in models:
    print(f"- {model.name} ({model.size} bytes)")
```

---

### Génération

#### `generate_text()` -> `OllamaGenerateResult`
Génère du texte (unimodal).

```python
result = client.generate_text(
    model="gemma2:latest",
    prompt="Explique la photosynthèse",
    system="Tu es un professeur de biologie",
    options={"temperature": 0.7}
)

print(result.response)
print(f"Durée: {result.total_duration}ns")
```

**Paramètres**
- `model` (str) : Nom du modèle
- `prompt` (str) : Prompt utilisateur
- `system` (str, optionnel) : Message système
- `options` (dict, optionnel) : Paramètres Ollama

#### `generate_with_image()` -> `OllamaGenerateResult`
Génère du texte avec image (multimodal).

```python
result = client.generate_with_image(
    model="llava:latest",
    prompt="Décris cette image",
    image="chemin/vers/image.jpg",
    system="Tu es un expert en analyse d'images"
)

print(result.response)
```

**Paramètres**
- `model` (str) : Modèle vision (llava, qwen2.5-vl, etc.)
- `prompt` (str) : Instruction texte
- `image` (str|Path|bytes) : Chemin ou bytes de l'image
- `image_mime_hint` (str, optionnel) : Hint MIME (debug)
- `system` (str, optionnel) : Message système
- `options` (dict, optionnel) : Paramètres

---

### Embeddings

#### `embed()` -> `List[float]`
Génère un embedding pour un texte.

```python
embedding = client.embed(
    model="nomic-embed-text:latest",
    text="Intelligence artificielle"
)

print(f"Dimension: {len(embedding)}")
```

---

## 🔧 Options avancées

### Paramètres de génération
```python
options = {
    "temperature": 0.7,      # Créativité (0.0-1.0)
    "top_p": 0.9,           # Nucleus sampling
    "top_k": 40,            # Top-k sampling
    "seed": 42,             # Reproductibilité
    "num_predict": 100,     # Max tokens à générer
}

result = client.generate_text(
    model="gemma2:latest",
    prompt="Continue cette histoire",
    options=options
)
```

### Timeout et erreurs
```python
try:
    result = client.generate_text(
        model="gemma2:latest",
        prompt="Question complexe",
        # timeout géré par le wrapper
    )
except OllamaConnectionError:
    print("Serveur injoignable")
except OllamaResponseError:
    print("Réponse invalide")
except OllamaError as e:
    print(f"Erreur Ollama: {e}")
```

## 🧪 Tests et exemples

### Test basique
```python
def test_basic_usage():
    client = OllamaWrapper()
    
    assert client.is_server_running()
    
    version = client.get_version()
    assert isinstance(version, str)
    
    models = client.list_models()
    assert isinstance(models, list)
```

### Génération avec options
```python
def test_generate_with_options():
    client = OllamaWrapper()
    
    result = client.generate_text(
        model="gemma2:latest",
        prompt="Test",
        options={"temperature": 0.0, "seed": 42}
    )
    
    assert isinstance(result.response, str)
    assert result.done is True
```

## 🚨 Limitations

- **HTTP uniquement** : pas de support WebSocket/streaming
- **Modèles locaux** : nécessite Ollama installé
- **Images base64** : encodage automatique géré

## 📚 Références

- [Documentation Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Code source](../ollama_wrapper_iut.py)

---

*Pour l'installation, voir [How-to : Installation](../how-to/install.md).*

# How-to : Créer et déployer un jeu

Guide complet pour créer et déployer un nouveau jeu sur la Borne Arcade.

## 🎮 Structure d'un jeu

```
games/
├── mon_jeu/
│   ├── main.py              # Entrée principale
│   ├── assets/              # Images, sons
│   ├── config.yml           # Configuration jeu
│   └── README.md            # Description jeu
```

## 🛠️ Création pas à pas

### 1. Initialiser le jeu

```bash
# Créer le dossier
mkdir games/mon_jeu
cd games/mon_jeu

# Créer les fichiers de base
touch main.py config.yml README.md
mkdir assets
```

### 2. Écrire le code principal

```python
# main.py
import pygame
from pathlib import Path

class MonJeu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

if __name__ == "__main__":
    game = MonJeu()
    game.run()
```

### 3. Configurer le jeu

```yaml
# config.yml
name: "Mon Jeu"
version: "1.0.0"
description: "Un jeu awesome pour la borne arcade"
author: "Ton Nom"
dependencies:
  - pygame>=2.0.0
assets:
  - assets/
entry_point: "main.py"
```

### 4. Documenter le jeu

```markdown
# Mon Jeu

## Description
Courte description du jeu.

## Contrôles
- Flèches : mouvement
- Espace : action

## Installation
```bash
pip install pygame
python main.py
```
```

## 🚀 Déploiement

### 1. Tester localement

```bash
# Depuis la racine du projet
python -m games.mon_jeu.main
```

### 2. Ajouter au système

```bash
# Enregistrer le jeu
python scripts/register_game.py --name "Mon Jeu" --path games/mon_jeu

# Vérifier l'enregistrement
python scripts/list_games.py
```

### 3. Déployer sur la borne

```bash
# Synchroniser avec la borne
rsync -av games/ user@borne:/opt/borne_arcade/games/

# Redémarrer le service
ssh user@borne "sudo systemctl restart borne-arcade"
```

## 🎨 Assets et ressources

### Images recommandées
- **Icone** : 64x64px, PNG
- **Screen** : 800x600px, PNG pour l'aperçu
- **Assets** : dans le dossier `assets/`

### Sons (optionnel)
- Format : WAV ou OGG
- Volume : normalisé

## 🧪 Tests

```python
# tests/test_mon_jeu.py
import unittest
from games.mon_jeu.main import MonJeu

class TestMonJeu(unittest.TestCase):
    def setUp(self):
        self.game = MonJeu()
    
    def test_initialization(self):
        self.assertIsNotNone(self.game.screen)
        self.assertTrue(self.game.running)

if __name__ == "__main__":
    unittest.main()
```

## 📦 Publication

### 1. Créer une PR

```bash
git add games/mon_jeu/
git commit -m "feat: add Mon Jeu"
git push origin feature/mon-jeu
```

### 2. Review et merge

- La PR doit inclure la documentation
- Les tests doivent passer
- L'IA proposera des améliorations de doc

### 3. Release

```bash
# Tagger la version
git tag -a v1.0.0 -m "Add Mon Jeu"
git push origin v1.0.0
```

## 🔧 Maintenance

- Mettre à jour `config.yml` si dépendances changent
- Garder `README.md` à jour
- Tests automatiques sur chaque PR

---

## 📚 Exemples

Voir les jeux existants dans `games/` pour des exemples complets.

---

*Pour l'installation de base, voir [Installation](install.md).*

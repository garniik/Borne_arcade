# ball-blast

## Décris le jeu ball-blast (objectif, principe, gameplay) en te basant sur le code.

# Documentation du jeu Ball Blast

## 1. Objectif du jeu
Détruire des boules ennemies en utilisant des balles de tir, tout en accumulant le meilleur score possible. Le jeu comporte des niveaux progressifs avec des mécaniques de gestion de ressources et de précision.

## 2. Principe de jeu
- **Contrôle des joueurs** :  
  - Joueur 1 : Joystick (flèches directionnelles) + touches (R, T, Y, F, G, H) pour déplacement et tir  
  - Joueur 2 : Joystick (touches O, L, K, M) + touches (A, Z, E, Q, S, D) pour déplacement et tir  
- **Mécanique de tir** :  
  - Les joueurs tirent des balles pour détruire des boules ennemies.  
  - Chaque type de balle a une valeur de score différente (ex: boule rouge = 40 points, boule verte = 33 points).  
  - Un système de cooldown (shootCD) limite les tirs successifs.  
- **Niveaux** :  
  - Le niveau détermine le nombre de boules à créer (BALL_EQUIVALENT).  
  - Des variantes de boules (couleurs) apparaissent selon le niveau.  

## 3. Gameplay technique
- **Structure du code** :  
  - Utilisation de Pygame (version 2.6.1) pour la gestion graphique, audio et input.  
  - Classes principales :  
    - `Game` : Gère la logique de jeu (création de balles, gestion des collisions, score).  
    - `Player` : Contrôle les mouvements et tirs des joueurs.  
    - `Ball` et `Bullet` : Gèrent les comportements physiques des entités.  
- **Assets** :  
  - Arrière-plan chargé depuis `assets/bg_pxl.jpg`.  
  - Sons (non activés dans le code) pour les effets sonores (bip, explosion, victoire).  
- **Gestion des états** :  
  - États principaux : menu, jeu en cours, pause, fin de partie.  
  - Possibilité de naviguer dans le menu via les touches (non complet dans le code).  

## 4. Interface et menus
- **Menu principal** :  
  - Options : Nouvelle partie / Crédits (partiellement implémenté).  
  - Affichage d'une texture de fond (bg_pxl.jpg).  
- **Pause** :  
  - Permet de suspendre le jeu et accéder à des options supplémentaires.  

## 5. Dépendances
- **Python** : Version 3.7 (via `requirements.txt`).  
- **Bibliothèque** : Pygame 2.6.1 pour la gestion graphique et audio.  

## 6. Notes techniques
- Le code est structuré en modules distincts (`game.py`, `menu.py`, `player.py`, etc.).  
- Le système de score utilise des équivalents de boules (BALL_EQUIVALENT) et des poids (BallEquivalents).  
- Le jeu intègre une gestion de fenêtre centrée via `SDL_VIDEO_CENTERED`.  

Ce projet montre une architecture modulaire avec des mécaniques de base de jeu (tir, collision, score) et une interface simple pour le menu.

## Quels sont les contrôles du jeu ball-blast sur la borne arcade (touches/boutons) ?

### Documentation des Contrôles du Jeu Ball Blast

#### **Contrôles des Joysticks**
- **Joystick J1**  
  - Fleches : Haut, Bas, Gauche, Droite  

- **Joystick J2**  
  - Boutons : **O**, **L**, **K**, **M**  

#### **Touches de Feu (Buttons)**
- **J1**  
  - Touches : **R**, **T**, **Y**, **F**, **G**, **H**  

- **J2**  
  - Touches : **A**, **Z**, **E**, **Q**, **S**, **D**  

#### **Notes**
- Les joysticks et touches sont associés aux actions de mouvement et de tir.  
- Les touches de feu (buttons) sont utilisées pour lancer des projectiles ou activer des actions spéciales.  
- Les contrôles sont définis dans le fichier `readme.md` et correspondent à la configuration des boutons de la borne arcade.

## Comment lancer et quitter le jeu ball-blast (scripts, classe main, commande) ?

### Documentation : Lancement et Quitte du Jeu Ball Blast

#### **1. Prérequis**
- **Installation des dépendances** :  
  ```bash
  pip install pygame==2.6.1
  ```

#### **2. Lancement du jeu**
- **Script principal** :  
  Exécutez le script `ball-blast.sh` pour lancer le jeu :  
  ```bash
  chmod +x ball-blast.sh
  ./ball-blast.sh
  ```  
  Ce script se charge de :  
  - Changer de répertoire vers le projet.  
  - Lancer le fichier Python principal via `src/__main__.py`.

- **Alternative (manuel)** :  
  Si le script n’est pas utilisé, lancez directement :  
  ```bash
  python3.7 src/__main__.py
  ```  
  Vérifiez que le répertoire `src` est dans le `PYTHONPATH`.

#### **3. Quitte du jeu**
- **Fermeture normale** :  
  Fermez la fenêtre du jeu via la croix (X) de la fenêtre. Cela déclenche :  
  ```python
  pygame.quit()
  ```  
  dans le `__main__.py`, terminant la boucle principale.

- **Quitter via menu** :  
  - Accédez au menu principal (via `showMenu` dans `menu.py`).  
  - Appuyez sur `ESC` ou `Q` (selon le code incomplet) pour quitter.

#### **4. Gestion des états**
- **Pause/Reprendre** :  
  Le jeu gère l’état de pause via la variable `pause` dans `__main__.py`.  
  - Appuyez sur `P` (ou autre touche configurée) pour activer/désactiver la pause.

- **Fin de partie** :  
  Si le joueur perd (`self.perdu: bool = True` dans `game.py`), le jeu passe en état `gameOver`, bloquant la boucle principale.

#### **5. Notes techniques**
- **Fichier principal** :  
  Le script `__main__.py` initialise Pygame, gère les états (`menu`, `game`, `pause`) et les événements clavier.  
- **Commandes clavier** :  
  Les touches de base (flèches, `Q`, `ESC`) sont gérées dans `menu.py` et `game.py` (code incomplet dans les fichiers fournis).

## Quelles sont les classes principales et leurs responsabilités dans ball-blast ?

### Documentation Technique : Ball Blast

#### **Classes Principales et Responsabilités**

1. **`Game`**  
   - **Responsabilités** :  
     - Gère l'état global du jeu (vies, score, niveau, cooldown de tir).  
     - Spawne des balles en fonction du niveau.  
     - Gère les collisions entre balles, tirs et joueurs.  
     - Met à jour le score et détecte la fin de partie (`perdu`).  
     - Charge et applique les textures d'arrière-plan.  
   - **Dépendances** :  
     - Utilise `Player`, `Ball`, et `Bullet` pour la logique de jeu.  

2. **`Menu`**  
   - **Responsabilités** :  
     - Affiche l'interface de menu (Nouvelle partie, Crédits).  
     - Gère la sélection des options via les touches du clavier.  
     - Transitions vers l'état de jeu ou les crédits.  
   - **Dépendances** :  
     - Utilise `pygame` pour le rendu et la gestion des événements.  

3. **`Player`**  
   - **Responsabilités** :  
     - Gère le mouvement des joueurs (J1 et J2) via les touches définies dans le `README.md`.  
     - Gère le tir de balles (cooldown, position des tirs).  
     - Interagit avec `Bullet` pour créer des tirs.  

4. **`Ball`**  
   - **Responsabilités** :  
     - Représente les balles à détruire (avec des comportements variés selon le niveau).  
     - Gère la logique de mouvement et de collision avec les tirs.  

5. **`Bullet`**  
   - **Responsabilités** :  
     - Gère le mouvement des tirs lancés par les joueurs.  
     - Détecte les collisions avec les balles et met à jour le score.  

---

#### **Structure Générale**
- **`__main__.py`** : Point d'entrée principal, initialise Pygame, gère les états (menu, jeu, fin de partie).  
- **`requirements.txt`** : Dépendances (pygame==2.6.1).  
- **`README.md`** : Description des contrôles et des touches.  

**Note** : Les classes `Ball` et `Bullet` sont implémentées dans des fichiers distincts (`ball.py`, `bullet.py`) mais sont intégrées dans le système de jeu via des imports.


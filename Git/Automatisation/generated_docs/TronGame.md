# TronGame

## Décris le jeu TronGame (objectif, principe, gameplay) en te basant sur le code.

# Documentation du Jeu TronGame

## Objectif du jeu
Le jeu TronGame est une implémentation du classique jeu "Tron" où les joueurs contrôlent des "Light Cycles" (cycles de lumière) qui laissent une traînée lumineuse derrière eux. L'objectif est de faire entrer l'adversaire en collision avec une traînée ou le bord de l'écran, tout en évitant soi-même les collisions.

## Principe de fonctionnement
Le jeu utilise un système de grilles (GRID_SIZE) pour représenter l'espace de jeu. Chaque joueur (ou IA) se déplace dans cette grille en suivant une direction (Direction). Les collisions sont détectées lors de l'intersection avec :
- Les bords de l'écran
- Les traînées laissées par les joueurs

## Gameplay
### Modes de jeu
1. **Mode solo** : Contre une IA avec 3 niveaux de difficulté (moyen, difficile, expert)
   - L'IA utilise des algorithmes de détection de collision avec paramètres ajustés selon la difficulté (look_ahead, update_interval)
   - Le joueur contrôlle un joueur via les touches du clavier

2. **Mode deux joueurs** : Joueur 1 (clavier) vs Joueur 2 (joystick ou clavier)

### Mécaniques de base
- **Déplacement** : Les joueurs se déplacent en diagonale ou en ligne droite (selon la configuration)
- **Traînée** : Chaque déplacement laisse une traînée lumineuse qui devient un obstacle
- **Pause** : Le jeu peut être mis en pause via un menu
- **Fin de partie** : Le jeu se termine lorsque l'un des joueurs entre en collision. Le vainqueur est déterminé par le dernier mouvement valide.

## Architecture technique
- **Système de menus** : 
  - Menu principal (choix du mode de jeu)
  - Menu options (ajustement des paramètres)
- **Synchronisation** : 
  - Utilisation de `move_delay` pour contrôler la vitesse de déplacement
  - Gestion des collisions via la vérification des positions des joueurs et des traînées
- **Rendu visuel** :
  - Effets néon (NEON_BLUE, NEON_PINK) pour les éléments du jeu
  - Animation de sélection des options du menu
  - Support pour l'affichage en plein écran

## Dépendances
- **Pygame** : Gestion de l'affichage, des entrées clavier/joystick, des sons
- **Fichiers de configuration** : Définissent les constantes (GRID_SIZE, MOVE_DELAY, couleurs, etc.)

## Caractéristiques techniques
- **Modularité** : 
  - Séparation des responsabilités (jeu, menus, IA, gestion des entrées)
  - Utilisation de classes pour les joueurs (Player), l'IA (AI), et les éléments du menu (MenuItem)
- **Performance** : 
  - Optimisation des collisions via la gestion de la grille
  - Gestion de la fréquence de mise à jour (ai_update_interval)

## Limites connues
- Le code incomplet (fichiers `test_game.py` et partie de `game_main.py`) suggère que certaines fonctionnalités (comme la gestion complète des collisions ou l'affichage des traînées) nécessitent des développements supplémentaires.

## Quels sont les contrôles du jeu TronGame sur la borne arcade (touches/boutons) ?

### Documentation : Contrôles du Jeu TronGame sur la Borne Arcade

#### **Contrôles des Joueurs**
Les contrôles sont optimisés pour une borne d'arcade avec des boutons physiques. Voici les mappings standards :

- **Joueur 1** :  
  - **Gauche** : Bouton **←**  
  - **Droite** : Bouton **→**  
  - **Haut** : Bouton **↑**  
  - **Bas** : Bouton **↓**  

- **Joueur 2** :  
  - **Gauche** : Bouton **R** (ou D-Pad gauche)  
  - **Droite** : Bouton **F** (ou D-Pad droit)  
  - **Haut** : Bouton **↑** (ou D-Pad haut)  
  - **Bas** : Bouton **↓** (ou D-Pad bas)  

#### **Notes Techniques**
- Les touches **R** et **F** sont utilisées pour le joueur 2, comme indiqué dans le fichier `options_main.py` (images des touches `key_r_img` et `key_f_img`).
- Les contrôles sont gérés via des événements de clavier ou des entrées physiques (joystick/D-Pad), selon la configuration de la borne.
- En mode solo, le joueur 1 contrôle le Light Cycle, et l'IA utilise des algorithmes de difficulté ajustés (voir `ai.py`).

#### **Configuration**
- Les paramètres de difficulté (facile/moyen/difficile) influencent le comportement de l'IA (voir `ai.py` et `config.py`).
- Les touches peuvent être personnalisées via le menu des options (fichier `options_main.py`).

## Comment lancer et quitter le jeu TronGame (scripts, classe main, commande) ?

### Documentation : Lancement et Quitte du Jeu TronGame

#### **1. Lancement du jeu**
- **Script principal** : Le jeu est lancé via le fichier `main.py`.
- **Commande** : Exécutez le script avec Python 3 :
  ```bash
  python main.py
  ```
- **Paramètres** :
  - Le jeu démarre en mode **fullscreen** si `FULLSCREEN = True` dans `config.py`.
  - Si `FULLSCREEN = False`, l'écran s'ouvre en fenêtre.

#### **2. Quitter le jeu**
- **Méthodes possibles** :
  1. **Fermer la fenêtre** : Cliquez sur la croix de fermeture de la fenêtre.
  2. **Touche de quitter** : Appuyez sur `ESC` pendant le jeu (géré par le cycle principal de Pygame).
  3. **Menu principal** : Si le jeu est en pause ou en menu, sélectionnez l'option "Quitter" (si disponible).

#### **3. Structure du code**
- **Classe principale** : La classe `TronGame` dans `main.py` gère l'initialisation et la boucle principale.
- **Fin de la boucle** : Le jeu s'arrête lorsque l'événement `QUIT` est détecté ou lorsque le joueur quitte via les touches.

#### **4. Notes supplémentaires**
- Le jeu utilise **Pygame** pour la gestion des événements et de l'affichage.
- Les options de difficulté et de mode de jeu (solo/2 joueurs) sont configurées dans `config.py` et gérées via le menu principal (`menu_main.py`).

## Quelles sont les classes principales et leurs responsabilités dans TronGame ?

### Documentation Technique : Classes Principales de TronGame

#### 1. **`Game`**  
**Responsabilités** :  
- Gère la logique centrale du jeu (collisions, déplacement, gestion des joueurs).  
- Initialise les joueurs (`Player` ou `AI`) en fonction du mode de jeu (solo/défi).  
- Met à jour l'état du jeu (vitesse, pause, fin de partie).  
- Traite les collisions avec les murs ou les traînées des joueurs.  
- Détermine le gagnant en cas de fin de partie.  

#### 2. **`TronGame`**  
**Responsabilités** :  
- Point d'entrée principal de l'application.  
- Gère l'initialisation de Pygame, la gestion de l'écran (plein écran ou fenêtré).  
- Contrôle la transition entre les menus (accueil, options) et le jeu.  
- Gère les événements globaux (quitter, redémarrer).  

#### 3. **`Menu`**  
**Responsabilités** :  
- Affiche et gère l'interface du menu principal.  
- Permet de naviguer entre les options (1 joueur, 2 joueurs, options).  
- Lance le jeu ou les sous-menus (ex: `Options`) en fonction de la sélection.  

#### 4. **`MenuItem`**  
**Responsabilités** :  
- Représente un élément du menu (ex: "1 JOUEUR", "OPTIONS").  
- Gère l'affichage du texte avec animation de sélection (effets néon).  
- Déclenche des actions (ex: lancer un mode de jeu) lors de la sélection.  

#### 5. **`Options`**  
**Responsabilités** :  
- Gère le sous-menu des paramètres (difficulté, contrôles, etc.).  
- Affiche des éléments visuels (ex: images des touches de la borne d'arcade).  
- Permet de modifier les paramètres du jeu et de les sauvegarder.  

#### 6. **`AI`**  
**Responsabilités** :  
- Contrôle le comportement de l'IA adverse.  
- Utilise des règles de difficulté (moyen, difficile) pour planifier des mouvements.  
- Évite les collisions et cherche à intercepter le joueur principal.  
- Utilise des algorithmes de recherche (look-ahead) pour anticiper les déplacements.  

#### 7. **`Player`**  
**Responsabilités** :  
- Gère le déplacement et la traînée des joueurs (humain ou IA).  
- Affiche les éléments visuels (couleurs néon, effets de lumière).  
- Traite les entrées utilisateur (touches du clavier ou joystick).  

---

### Structure Héritage et Collaboration  
- **`AI`** hérite de **`Player`** : Partage le code de déplacement et de rendu, avec des comportements spécifiques pour l'IA.  
- **`Game`** collabore avec **`Player`** et **`AI`** : Gère leur interaction et les règles du jeu.  
- **`TronGame`** orchestre **`Menu`** et **`Game`** : Contrôle le flux d'exécution du jeu.  
- **`MenuItem`** et **`Options`** collaborent pour afficher l'interface utilisateur.  

Cette architecture modulaire permet une évolutivité facile (ex: ajouter de nouveaux modes de jeu ou IA).


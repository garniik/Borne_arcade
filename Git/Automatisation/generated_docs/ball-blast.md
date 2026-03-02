# ball-blast

## Décris le jeu ball-blast (objectif, principe, gameplay) en te basant sur le code.

### Ball Blast : Description du Jeu

#### Objectif
Ball Blast est un jeu d'arcade où le joueur doit détruire des boules en utilisant des projectiles et des pouvoirs spéciaux. Le but est de détruire toutes les boules sur l'écran pour obtenir le meilleur score possible.

#### Principe
Le jeu se déroule sur une grille de jeu avec des boules de différentes tailles et couleurs. Le joueur contrôle un personnage qui peut se déplacer à gauche et à droite. Il peut également tirer des projectiles pour détruire les boules. Les boules peuvent avoir des effets spéciaux qui peuvent aider ou gêner le joueur.

#### Gameplay
1. **Interface de Jeu**:
   - **Joystick J1**: Utilisé pour déplacer le personnage.
   - **Joystick J2**: Utilisé pour tirer des projectiles.
   - **Touches J1**: `r`, `t`, `y` pour déplacer le personnage.
   - **Touches J2**: `a`, `z`, `e` pour déplacer le personnage.
   - **Touches J2**: `q`, `s`, `d` pour tirer des projectiles.

2. **Éléments de Jeu**:
   - **Boules**: De différentes tailles et couleurs, certaines peuvent avoir des effets spéciaux.
   - **Projetsiles**: Tirés par le joueur pour détruire les boules.
   - **Pouvoirs Spéciaux**: Peut être activé par le joueur pour obtenir des avantages temporaires.

3. **États du Jeu**:
   - **Menu**: Affiche les options de jeu (nouvelle partie, pause, crédits).
   - **Jeux**: Le joueur contrôle le personnage et détruit les boules.
   - **Pause**: Permet de mettre en pause le jeu.
   - **Fin de Partie**: Affiche le score et permet de reprendre la partie ou de quitter.

4. **Gestion des États**:
   - **State Machine**: Le jeu utilise une machine à états pour gérer les différents états (menu, jeu, pause, fin de partie).

5. **Sons et Musique**:
   - Le jeu utilise des sons pour les actions de jeu (tir, explosion, victoire) et des musiques de fond.

### Conclusion
Ball Blast est un jeu d'arcade qui combine des éléments de déplacement, de tir et de destruction. Le joueur doit être rapide et précis pour détruire les boules et obtenir le meilleur score possible. Le jeu est structuré autour d'un menu principal, d'un état de jeu, et d'états spécifiques pour la pause et la fin de partie.

## Quels sont les contrôles du jeu ball-blast sur la borne arcade (touches/boutons) ?

### Contrôles du jeu Ball Blast sur borne d'arcade

#### Joystick J1
- **Haut** : Interagir
- **Bas** : Interagir
- **Gauche** : Interagir
- **Droite** : Interagir

#### Joystick J2
- **O** : Interagir
- **L** : Interagir
- **K** : Interagir
- **M** : Interagir

#### Touches J1
- **R** : Interagir
- **T** : Interagir
- **Y** : Interagir

#### Touches J2
- **A** : Interagir
- **Z** : Interagir
- **E** : Interagir
- **Q** : Interagir
- **S** : Interagir
- **D** : Interagir

### Résumé
Le jeu Ball Blast est contrôlé par deux joysticks et six touches supplémentaires. Les joysticks J1 et J2 ont des fonctions de base (haut, bas, gauche, droite) et des touches supplémentaires (O, L, K, M, A, Z, E, Q, S, D). Les touches J1 et J2 permettent d'interagir avec le jeu, probablement pour lancer des projectiles ou déclencher des actions spécifiques. Les joysticks J1 et J2 ont des fonctions supplémentaires qui peuvent être personnalisées pour des actions spécifiques dans le jeu.

## Comment lancer et quitter le jeu ball-blast (scripts, classe main, commande) ?

### Lancer et Quitter le Jeu Ball-Blast

#### **1. Lancer le Jeu**
Pour lancer le jeu `Ball-Blast`, vous devez suivre ces étapes :

1. **Chemin d'accès au répertoire du projet** : Assurez-vous d'être dans le répertoire racine du projet `ball-blast`.

2. **Exécuter le script** : Utilisez le script `ball-blast.sh` pour exécuter le programme.

```sh
cd ./projet/ball-blast
python3.7 ./src/__main__.py
```

#### **2. Quitter le Jeu**
Pour quitter le jeu, vous pouvez :

1. **Utiliser les touches de la borne** : 
   - Pour quitter le jeu, utilisez les touches de la borne d'arcade. Selon le fichier `readme.md`, vous pouvez utiliser les touches `r`, `t`, `y` pour quitter le jeu.

2. **Utiliser les touches du clavier** : 
   - Si vous êtes en mode pause ou si vous voulez quitter le jeu, vous pouvez utiliser les touches du clavier. Le fichier `menu.py` indique que vous pouvez utiliser les touches de direction pour naviguer dans le menu. Pour quitter le jeu, vous pouvez appuyer sur la touche `ESC` ou `Q` dans le menu.

3. **Fermer la fenêtre** : Si vous êtes en mode pause ou si vous voulez quitter le jeu, vous pouvez fermer la fenêtre de jeu en cliquant sur le bouton "X" dans le coin supérieur droit de la fenêtre.

#### **3. Documentation**

- **Fichier `readme.md`** : Ce fichier contient les instructions de base pour utiliser le jeu. Il décrit les touches de la borne d'arcade et les touches du clavier pour naviguer et quitter le jeu.

- **Fichier `src/__main__.py`** : Ce fichier est le point d'entrée du programme. Il initialise Pygame, charge les assets, et gère le cycle de vie du jeu. Pour quitter le jeu, vous pouvez appuyer sur les touches de la borne d'arcade ou les touches du clavier comme indiqué dans le fichier `menu.py`.

- **Fichier `menu.py`** : Ce fichier gère le menu du jeu. Il permet de naviguer entre les options du menu et de quitter le jeu en appuyant sur les touches de la borne d'arcade ou les touches du clavier.

- **Fichier `ball-blast.sh`** : Ce script permet de lancer le programme en utilisant Python 3.7. Assurez-vous d'avoir Python 3.7 installé sur votre système.

En suivant ces étapes, vous pouvez lancer et quitter le jeu `Ball-Blast` de manière efficace.

## Quelles sont les classes principales et leurs responsabilités dans ball-blast ?

### Documentation des classes principales dans ball-blast

#### 1. **Class `Game` (src/game.py)**
   - **Responsabilités**:
     - Gestion du jeu principal.
     - Création et gestion des boules et des joueurs.
     - Gestion des niveaux et des scores.
     - Gestion des collisions et des effets spéciaux.
     - Gestion des effets sonores et visuels.
   - **Variables clés**:
     - `level`: Niveau actuel du jeu.
     - `ball_level`: Liste des couleurs et des tailles des boules.
     - `ballEquivalents`: Poids des boules.
     - `ballsToSpawn`: Nombre de boules à créer par niveau.
     - `perdu`: Indicateur de si le joueur a perdu.
     - `shootCD`: Compteur de refroidissement pour le tir.
     - `texture`: Texture de fond du jeu.
   - **Méthodes clés**:
     - `__init__`: Initialisation du jeu.
     - `showMenu`: Affichage du menu principal.
     - `update`: Mise à jour des objets et des effets.
     - `draw`: Dessin des objets sur l'écran.

#### 2. **Class `Menu` (src/menu.py)**
   - **Responsabilités**:
     - Affichage du menu principal.
     - Gestion des options du menu.
     - Gestion des événements clavier pour naviguer dans le menu.
   - **Variables clés**:
     - `selectedOption`: Option sélectionnée dans le menu.
     - `texture`: Texture de fond du menu.
   - **Méthodes clés**:
     - `__init__`: Initialisation du menu.
     - `showMenu`: Affichage du menu et gestion des événements clavier.
     - `update`: Mise à jour des options du menu.
     - `draw`: Dessin du menu sur l'écran.

#### 3. **Class `Ball` (src/ball.py)**
   - **Responsabilités**:
     - Gestion des boules dans le jeu.
     - Gestion des collisions et des effets spéciaux.
   - **Variables clés**:
     - `position`: Position de la boule.
     - `velocity`: Vitesse de la boule.
     - `size`: Taille de la boule.
     - `color`: Couleur de la boule.
   - **Méthodes clés**:
     - `__init__`: Initialisation de la boule.
     - `update`: Mise à jour de la position et de la vitesse de la boule.
     - `draw`: Dessin de la boule sur l'écran.

#### 4. **Class `Player` (src/player.py)**
   - **Responsabilités**:
     - Gestion des joueurs dans le jeu.
     - Gestion des mouvements et des tirs.
   - **Variables clés**:
     - `position`: Position du joueur.
     - `velocity`: Vitesse du joueur.
     - `direction`: Direction du joueur.
     - `health`: Points de vie du joueur.
   - **Méthodes clés**:
     - `__init__`: Initialisation du joueur.
     - `update`: Mise à jour de la position et de la vitesse du joueur.
     - `draw`: Dessin du joueur sur l'écran.

#### 5. **Class `Bullet` (src/bullet.py)**
   - **Responsabilités**:
     - Gestion des balles de tir dans le jeu.
     - Gestion des collisions et des effets spéciaux.
   - **Variables clés**:
     - `position`: Position de la balle de tir.
     - `velocity`: Vitesse de la balle de tir.
     - `size`: Taille de la balle de tir.
     - `color`: Couleur de la balle de tir.
   - **Méthodes clés**:
     - `__init__`: Initialisation de la balle de tir.
     - `update`: Mise à jour de la position et de la vitesse de la balle de tir.
     - `draw`: Dessin de la balle de tir sur l'écran.

#### 6. **Class `Constantes` (src/constantes.py)**
   - **Responsabilités**:
     - Définition des constantes utilisées dans le jeu.
   - **Variables clés**:
     - `SCREEN_WIDTH`: Largeur de l'écran.
     - `SCREEN_HEIGHT`: Hauteur de l'écran.
     - `WHITE`, `BLACK`, `RED`, `GREEN`, `BLUE`: Couleurs.
     - `FONT`: Police de caractères.
     - `FIRERATE`: Fréquence de tir.
     - `BALL_EQUIVALENT`: Poids des boules.
     - `FONT_SCORE`: Police de caractères pour les scores.
   - **Méthodes clés**:
     - Aucune méthode spécifique.

#### 7. **Class `Menu` (src/menu.py)**
   - **Responsabilités**:
     - Affichage du menu principal.
     - Gestion des options du menu.
     - Gestion des événements clavier pour naviguer dans le menu.
   - **Variables clés**:
     - `selectedOption`: Option sélectionnée dans le menu.
     - `texture`: Texture de fond du menu.
   - **Méthodes clés**:
     - `__init__`: Initialisation du menu.
     - `showMenu`: Affichage du menu et gestion des événements clavier.
     - `update`: Mise à jour des options du menu.
     - `draw`: Dessin du menu sur l'écran.

#### 8. **Class `Game` (src/game.py)**
   - **Responsabilités**:
     - Gestion du jeu principal.
     - Création et gestion des boules et des joueurs.
     - Gestion des niveaux et des scores.
     - Gestion des effets spéciaux.
   - **Variables clés**:
     - `level`: Niveau actuel du jeu.
     - `ball_level`: Liste des couleurs et des tailles des boules.
     - `ballEquivalents`: Poids des boules.
     - `ballsToSpawn`: Nombre de boules à créer par niveau.
     - `perdu`: Indicateur de si le joueur a perdu.
     - `shootCD`: Compteur de refroidissement pour le tir.
     - `texture`: Texture de fond du jeu.
   - **Méthodes clés**:
     - `__init__`: Initialisation du jeu.
     - `showMenu`: Affichage du menu principal.
     - `update`: Mise à jour des objets et des effets.
     - `draw`: Dessin des objets sur l'écran.

### Conclusion
Les classes principales dans `ball-blast` sont `Game`, `Menu`, `Ball`, `Player`, et `Bullet`. Chaque classe a des responsabilités spécifiques pour gérer les aspects clés du jeu, comme la gestion des niveaux, des joueurs, des boules, et des effets spéciaux. Les constantes définies dans `Constantes` fournissent les valeurs de base pour les couleurs, les tailles, et les fréquences utilisées dans le jeu.


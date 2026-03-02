# Minesweeper

## Décris le jeu Minesweeper (objectif, principe, gameplay) en te basant sur le code.

### Description du jeu Minesweeper

#### Objectif
Le jeu Minesweeper est un jeu de stratégie classique où le but est de déminer une grille sans déclencher les bombes. Le joueur doit découvrir les cases vides tout en évitant les cases contenant des bombes.

#### Principe
Le jeu se déroule sur une grille de cases. Chaque case peut être soit vide, soit contenir une bombe. Le nombre de bombes à proximité de chaque case est indiqué par des chiffres. Le joueur doit cliquer sur une case pour la découvrir. Si la case est vide, il peut continuer à cliquer pour découvrir davantage de cases. Si la case contient une bombe, le jeu est perdu.

#### Gameplay
1. **Initialisation** : Le jeu commence avec une grille de cases aléatoirement générée. Chaque case peut être soit vide (0 à 8 bombes à proximité) ou contenir une bombe (0 bombes à proximité).

2. **Interactions** :
   - **Clic gauche** : Découvre une case. Si elle est vide, le joueur peut cliquer sur d'autres cases. Si elle contient une bombe, le jeu est perdu.
   - **Clic droit** : Place un drapeau sur une case. Le drapeau indique que la case contient une bombe. Si la case est vide, le joueur peut cliquer sur d'autres cases. Si elle contient une bombe, le jeu est perdu.

3. **Gestion des cases** :
   - **Cases vides** : Lorsque la case est vide, le joueur peut cliquer pour découvrir davantage de cases.
   - **Cases bombes** : Si la case contient une bombe, le jeu est perdu.

4. **Gestion des drapeaux** :
   - Le joueur peut placer un drapeau sur une case pour indiquer qu'elle contient une bombe. Si la case est vide, le joueur peut cliquer pour découvrir davantage de cases.

#### Interface
- **Joysticks** : Les mouvements sont contrôlés par les flèches du joystick.
- **Boutons** : Les actions sont effectuées par les boutons du joystick. Le bouton gauche permet de creuser une case, le bouton droit permet de drapeau une case.

#### Interface Graphique
- **Fenêtre principale** : Affiche la grille de jeu avec les cases vides et les bombes.
- **Menu** : Affiche les options de jeu et permet de quitter le jeu.

#### Documentation Technique
- **Fichier MainGraphic.java** : Gère l'affichage de la fenêtre principale et du menu.
- **Fichier Menu.java** : Gère l'affichage du menu principal du jeu.
- **Fichier README.md** : Documente les commandes de jeu et les crédits du projet.
- **Fichier Basic.java** : Gère les paramètres de base du jeu (taille de la grille, nombre de bombes, etc.).
- **Fichier Board.java** : Gère la grille de jeu et la gestion des cases (vides et bombes).
- **Fichier Bomb.java** : Gère les cases contenant des bombes.
- **Fichier bouton.txt** : Documente les actions associées aux boutons du joystick.
- **Fichier Button.java** : Interface pour les boutons de jeu.

Ce jeu Minesweeper est conçu pour être joué sur une borne d'arcade, avec des contrôles simples et une interface graphique intuitive.

## Quels sont les contrôles du jeu Minesweeper sur la borne arcade (touches/boutons) ?

### Contrôles du jeu Minesweeper sur la borne arcade

#### Joysticks :
- **Up** : Flèche vers le haut
- **Down** : Flèche vers le bas
- **Left** : Flèche vers la gauche
- **Right** : Flèche vers la droite

#### Boutons :
- **Top** :
    - **1st** : X - Quitter/Sortir
    - **2nd** : Y - (Difficulté ? / Score)
    - **3rd** : Z
- **Bottom** :
    - **1st** : A - Bouton pour creuser
    - **2nd** : B - Bouton pour drapeau
    - **3rd** : C - Creuser/Drapeau - Réinitialiser

#### Documentation détaillée :
- **Joysticks** : Utilisés pour déplacer le curseur sur l'écran.
- **Boutons** : 
    - **Top** : 
        - **X** : Permet de quitter le jeu ou de revenir en arrière.
        - **Y** : Peut être associé à la difficulté du jeu ou au score.
        - **Z** : Fonction non spécifiée dans le document.
    - **Bottom** : 
        - **A** : Utilisé pour creuser une case.
        - **B** : Utilisé pour drapeau une case.
        - **C** : Permet de creuser ou drapeau une case et de réinitialiser le jeu.

Cette documentation fournit une vue d'ensemble des contrôles du jeu Minesweeper sur la borne arcade, basée sur les informations fournies dans le fichier README.md.

## Comment lancer et quitter le jeu Minesweeper (scripts, classe main, commande) ?

### Documentation pour lancer et quitter le jeu Minesweeper

#### 1. **Lancer le jeu Minesweeper**
Pour lancer le jeu Minesweeper, vous devez exécuter le programme principal qui charge la fenêtre principale du jeu. Voici les étapes à suivre :

1. **Exécuter le programme principal** :
   - Le programme principal est généralement exécuté à partir d'un fichier `MainGraphic.java`. Ce fichier contient la classe `MainGraphic` qui est le point d'entrée du programme.
   - Pour exécuter le programme, vous pouvez utiliser un compilateur Java (comme `javac`) pour compiler le fichier `MainGraphic.java` et exécuter le fichier exécuté (`.class`) avec `java`.

   ```bash
   javac MainGraphic.java
   java MainGraphic
   ```

2. **Interactions avec le joystick** :
   - Une fois le programme exécuté, vous pouvez utiliser un joystick pour contrôler le jeu. Les commandes de base sont les suivantes :
     - **Up** : Direction vers le haut
     - **Down** : Direction vers le bas
     - **Left** : Direction vers la gauche
     - **Right** : Direction vers la droite

#### 2. **Quitter le jeu Minesweeper**
Pour quitter le jeu Minesweeper, vous pouvez utiliser les commandes de bouton du joystick :

1. **Utiliser les boutons du joystick** :
   - **Top** :
     - **1st** : Appuyer sur le bouton X pour quitter le jeu.
   - **Bottom** :
     - **1st** : Appuyer sur le bouton A pour quitter le jeu.

2. **Interactions avec le joystick** :
   - Appuyez sur le bouton X (1er bouton du joystick) pour quitter le jeu.

#### 3. **Documentation des commandes**
- **Joysticks** :
  - **Up** : Direction vers le haut
  - **Down** : Direction vers le bas
  - **Left** : Direction vers la gauche
  - **Right** : Direction vers la droite
- **Boutons** :
  - **Top** :
    - **1st** : X - Quitter le jeu
    - **2nd** : Y - (Difficulté ? / Score)
    - **3rd** : Z
  - **Bottom** :
    - **1st** : A - Bouton pour creuser
    - **2nd** : B - Bouton pour drapeau
    - **3rd** : C - Creuser/Drapeau - Réinitialiser

#### 4. **Fichier README.md**
Le fichier `README.md` fournit des informations supplémentaires sur le projet et les commandes de jeu. Il est recommandé de consulter ce fichier pour une meilleure compréhension des commandes et des interactions avec le jeu.

### Conclusion
Pour lancer et quitter le jeu Minesweeper, vous devez exécuter le programme principal (`MainGraphic.java`) et utiliser les commandes de joystick pour contrôler le jeu. Pour quitter le jeu, appuyez sur le bouton X (1er bouton du joystick) du joystick.

## Quelles sont les classes principales et leurs responsabilités dans Minesweeper ?

### Classes Principales et Responsabilités dans Minesweeper

#### 1. **MainGraphic**
- **Responsabilités :**
  - Gestion de l'interface graphique principale.
  - Gestion des textures et des éléments graphiques.
  - Gestion du curseur et du menu.
  - Affichage des éléments graphiques sur la fenêtre.

#### 2. **Menu**
- **Responsabilités :**
  - Gestion de l'affichage du menu principal.
  - Gestion des options du menu (difficulté, score, etc.).
  - Interaction avec l'utilisateur pour sélectionner des options.

#### 3. **Board**
- **Responsabilités :**
  - Gestion de la grille du jeu.
  - Création et gestion des cases de la grille (tiles).
  - Génération aléatoire des bombes.
  - Gestion des cases découvertes.

#### 4. **Bomb**
- **Responsabilités :**
  - Gestion des bombes sur la grille.
  - Gestion des attributs de la bombe (masquée, drapeau).
  - Interaction avec les cases voisines pour déterminer le nombre de bombes adjacentes.

#### 5. **Basic**
- **Responsabilités :**
  - Gestion de la base de niveau.
  - Gestion des dimensions de la grille.
  - Gestion du nombre de bombes.
  - Gestion des dimensions de la fenêtre.

#### 6. **Button**
- **Responsabilités :**
  - Interface pour les boutons.
  - Gestion de l'affichage des boutons.
  - Gestion de l'action des boutons (creuser, drapeau, etc.).

#### 7. **bouton.txt**
- **Responsabilités :**
  - Gestion des mouvements et des actions associées aux boutons.
  - Définition des actions pour les boutons (creuser, drapeau, etc.).

#### 8. **README.md**
- **Responsabilités :**
  - Documentation du projet.
  - Instructions d'utilisation.
  - Crédits et informations sur les ressources utilisées.

### Conclusion
Les classes principales dans ce projet sont **MainGraphic**, **Menu**, **Board**, **Bomb**, **Basic**, **Button**, et **bouton.txt**. Chaque classe a des responsabilités spécifiques liées à la gestion de l'interface utilisateur, de la grille du jeu, des bombes, et des interactions utilisateur. Le **README.md** fournit des informations supplémentaires sur le projet et les ressources utilisées.


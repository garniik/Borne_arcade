# Columns

## Décris le jeu Columns (objectif, principe, gameplay) en te basant sur le code.

### Description du Jeu Columns

#### Objectif
Aligner trois gemmes de même couleur pour les faire disparaître.

#### Principe
Le jeu Columns est un jeu de puzzle où le joueur doit aligner trois gemmes de même couleur pour les faire disparaître. Le jeu se déroule sur une grille de colonnes, où chaque colonne contient des gemmes de différentes couleurs.

#### Gameplay
1. **Interface de Jeu**:
   - **Fenêtre**: La fenêtre principale du jeu est une fenêtre pleine écran avec un affichage de primitives et de FPS (frames par seconde) activé.
   - **Clavier**: Le clavier est utilisé pour contrôler le jeu. Les directions de déplacement (haut, bas, gauche, droite) et les boutons de jeu (A, B, C, X, Y, Z) sont gérés via le clavier.
   - **Menu**: Le menu principal du jeu permet de choisir entre plusieurs options, notamment le mode de jeu (1 joueur, 2 joueurs) et la fin du jeu (quitter).

2. **Gestion des Gemmes**:
   - **Colone**: Chaque colonne est représentée par une instance de la classe `Colone`, qui contient trois gemmes (`Gemme`).
   - **Gemme**: Les gemmes sont de différentes couleurs (jaune, orange, vert, violet, rouge, bleu) et peuvent être vides. Elles sont représentées par des textures chargées à partir de fichiers d'images.

3. **Interactions**:
   - **Intervertir**: Les gemmes peuvent être interverties pour aligner des séquences de trois gemmes de même couleur.
   - **Déplacement**: Les gemmes peuvent être déplacées verticalement dans les colonnes pour aligner des séquences de trois gemmes de même couleur.

4. **Gestion des États**:
   - **Menu**: Le menu permet de naviguer entre les différentes options du jeu.
   - **Partie**: La partie principale du jeu gère le gameplay et la gestion des scores.

5. **Contrôle**:
   - **ClavierBorneArcade**: Cette classe gère les interactions clavier pour contrôler le jeu, notamment les directions de déplacement et les boutons de jeu.

#### Conclusion
Columns est un jeu de puzzle où le joueur doit aligner trois gemmes de même couleur pour les faire disparaître. Le jeu est contrôlé via le clavier, avec des options de menu pour choisir le mode de jeu et la fin du jeu. Les gemmes sont représentées par des textures et peuvent être interverties pour aligner des séquences de trois gemmes de même couleur.

## Quels sont les contrôles du jeu Columns sur la borne arcade (touches/boutons) ?

### Contrôles du jeu Columns sur la borne arcade

#### ClavierBorneArcade.java
La classe `ClavierBorneArcade` gère les contrôles du clavier pour la borne d'arcade. Voici les contrôles disponibles :

- **Joysticks** :
  - `joyJ1Haut` : Joystick 1 vers le haut
  - `joyJ1Bas` : Joystick 1 vers le bas
  - `joyJ1Gauche` : Joystick 1 vers la gauche
  - `joyJ1Droite` : Joystick 1 vers la droite
  - `joyJ2Haut` : Joystick 2 vers le haut
  - `joyJ2Bas` : Joystick 2 vers le bas
  - `joyJ2Gauche` : Joystick 2 vers la gauche
  - `joyJ2Droite` : Joystick 2 vers la droite

- **Boutons** :
  - `boutonJ1A` : Bouton A du joystick 1
  - `boutonJ1B` : Bouton B du joystick 1
  - `boutonJ1C` : Bouton C du joystick 1
  - `boutonJ1X` : Bouton X du joystick 1
  - `boutonJ1Y` : Bouton Y du joystick 1
  - `boutonJ1Z` : Bouton Z du joystick 1
  - `boutonJ2A` : Bouton A du joystick 2
  - `boutonJ2B` : Bouton B du joystick 2
  - `boutonJ2C` : Bouton C du joystick 2
  - `boutonJ2X` : Bouton X du joystick 2
  - `boutonJ2Y` : Bouton Y du joystick 2
  - `boutonJ2Z` : Bouton Z du joystick 2

#### Description.txt
La description du jeu mentionne que les contrôles sont associés à des touches et des boutons, mais elle ne fournit pas de détails spécifiques sur les touches du clavier. Les contrôles sont plutôt associés aux joysticks et aux boutons du clavier pour la borne d'arcade.

#### Conclusion
Les contrôles du jeu Columns sur la borne arcade sont principalement gérés par les joysticks et les boutons du clavier. Les joysticks permettent de déplacer les colonnes vers le haut, le bas, la gauche et la droite, tandis que les boutons permettent d'interagir avec les gemmes et d'effectuer des actions spécifiques.

## Comment lancer et quitter le jeu Columns (scripts, classe main, commande) ?

Pour lancer et quitter le jeu Columns, voici les étapes à suivre basées sur les fichiers fournis :

### Lancer le jeu Columns

1. **Exécuter le fichier `Main.java`** :
   - Ouvrez un terminal ou une console de commande.
   - Naviguez jusqu au répertoire contenant le fichier `Main.java`.
   - Exécutez le fichier avec le compilateur Java (javac) puis avec le programme d'exécution (java).
   ```sh
   javac Main.java
   java Main
   ```

2. **Exécuter le programme** :
   - Une fenêtre de jeu apparaîtra avec le titre "Columns".
   - Vous pouvez commencer à jouer en utilisant les contrôles du clavier définis dans `ClavierBorneArcade.java`.

### Quitter le jeu Columns

1. **Utiliser les contrôles du clavier** :
   - Pour quitter le jeu, utilisez les touches de quitture définies dans `ClavierBorneArcade.java`. Par exemple, la touche "Q" ou "Escape" peut être utilisée pour quitter le jeu.

2. **Fermer la fenêtre** :
   - Si vous utilisez une fenêtre pleine écran (`FenetrePleinEcran`), vous pouvez fermer la fenêtre en cliquant sur le bouton "X" dans le coin supérieur droit de la fenêtre.

### Documentation

#### Classe `Main.java`
- **Fonction principale** : La classe `Main` est la classe principale du programme.
- **Méthode `main`** : Cette méthode est appelée lorsque le programme est exécuté.
- **Initialisation** : 
  - Crée une fenêtre avec le titre "Columns".
  - Ajoute un clavier pour contrôler le jeu.
  - Crée un menu et une partie du jeu.
  - Gère les événements clavier pour contrôler le jeu.

#### Classe `Menu.java`
- **Menu principal** : Cette classe gère le menu principal du jeu.
- **Attributs** : Contient les attributs nécessaires pour afficher le menu et gérer les interactions avec l'utilisateur.
- **Méthodes** : 
  - `afficherMenu()` : Affiche le menu principal.
  - `traiterChoix(int choix)` : Traite le choix de l'utilisateur et retourne le statut du menu.

#### Classe `ClavierBorneArcade.java`
- **Classe de gestion du clavier** : Cette classe gère les événements clavier spécifiques à la borne d'arcade.
- **Méthodes** : 
  - `keyTyped(KeyEvent e)` : Gère les touches de type.
  - `keyPressed(KeyEvent e)` : Gère les touches enfoncées.
  - `keyReleased(KeyEvent e)` : Gère les touches relâchées.

#### Classe `Colone.java`
- **Classe pour gérer les colonnes de gemmes** : Cette classe gère les colonnes de gemmes dans le jeu.
- **Méthodes** : 
  - `intervertir()` : Permet d'intervertir les positions des gemmes dans une colonne.
  - `getX()` : Retourne la position x de la colonne.
  - `getY()` : Retourne la position y de la colonne.

#### Classe `Gemme.java`
- **Classe pour gérer les gemmes** : Cette classe gère les différents types de gemmes et leurs propriétés.
- **Méthodes** : 
  - `intervertir()` : Permet d'intervertir les positions des gemmes dans une colonne.
  - `getX()` : Retourne la position x de la colonne.
  - `getY()` : Retourne la position y de la colonne.

### Conclusion
Pour lancer et quitter le jeu Columns, suivez les étapes ci-dessus. Le programme est exécuté en exécutant le fichier `Main.java` avec le compilateur et le programme d'exécution Java. Pour quitter le jeu, utilisez les contrôles du clavier spécifiques à la borne d'arcade.

## Quelles sont les classes principales et leurs responsabilités dans Columns ?

### Classes Principales et Responsabilités dans Columns

#### 1. **Main.java**
- **Responsabilités :**
  - Initialisation de la fenêtre de jeu.
  - Création et configuration de la fenêtre pleine écran.
  - Ajout d'un clavier pour la gestion des contrôles.
  - Création et gestion des objets de jeu (Menu et Partie).
  - Gestion de l'affichage des primitives et des FPS.
  - Gestion de l'interactivité avec le clavier.

#### 2. **Menu.java**
- **Responsabilités :**
  - Gestion du menu principal du jeu.
  - Affichage du fond et du titre du jeu.
  - Gestion des choix du joueur (Menu principal, Choix de la musique/difficulté, Quitter).
  - Gestion des interactions avec le joueur pour choisir les options du menu.

#### 3. **Colone.java**
- **Responsabilités :**
  - Gestion des colonnes de gemmes.
  - Création et gestion des gemmes dans une colonne.
  - Gestion de l'intervertissement des gemmes.
  - Calcul des coordonnées des gemmes.

#### 4. **Gemme.java**
- **Responsabilités :**
  - Gestion des types de gemmes (jaune, orange, vert, violet, rouge, bleu, vide).
  - Création et gestion des textures des gemmes.
  - Gestion des actions spécifiques aux gemmes (suppression, etc.).

#### 5. **Controles.java**
- **Responsabilités :**
  - Définition des constantes pour les directions et les boutons de contrôle.
  - Utilisation pour la gestion des mouvements et des actions dans le jeu.

#### 6. **ClavierBorneArcade.java**
- **Responsabilités :**
  - Gestion des événements clavier pour la borne d'arcade.
  - Interprétation des touches pour les joysticks et les boutons.
  - Gestion des mouvements et des actions du joueur.

#### 7. **bouton.txt**
- **Responsabilités :**
  - Définition des actions associées aux boutons de la borne d'arcade.
  - Interprétation des actions pour les joysticks et les boutons.

#### 8. **description.txt**
- **Responsabilités :**
  - Documentation du jeu.
  - Description des règles du jeu (aligner trois gemmes de même couleur pour les faire disparaître).
  - Auteur et année de création du jeu (Dorian Terlat, 2020).

### Conclusion
Les classes principales dans le projet Columns sont **Main.java**, **Menu.java**, **Colone.java**, **Gemme.java**, **Controles.java**, **ClavierBorneArcade.java**, **bouton.txt**, et **description.txt**. Chaque classe a des responsabilités spécifiques liées à la gestion des objets de jeu, des interactions utilisateur, et à la logique du jeu.


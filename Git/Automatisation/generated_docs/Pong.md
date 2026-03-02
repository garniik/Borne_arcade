# Pong

## Décris le jeu Pong (objectif, principe, gameplay) en te basant sur le code.

### Description du Jeu Pong

#### Objectif
Le jeu Pong est un jeu de réflexion classique où le but est de faire rebondir une balle sur une raquette pour la faire rebondir sur l'autre côté de la fenêtre. Le joueur doit éviter que la balle ne touche le bord de la fenêtre et doit essayer de faire rebondir la balle sur l'autre raquette pour gagner des points.

#### Principe
Le jeu se déroule dans une fenêtre de jeu rectangulaire. Le joueur contrôle une raquette horizontale située en bas de la fenêtre. L'objectif est de faire rebondir une balle circulaire sur la raquette pour la faire rebondir sur l'autre côté de la fenêtre. Si la balle touche le bord de la fenêtre, le joueur perd une vie. Si la balle touche la raquette adverse, le joueur gagne un point. Le jeu se termine lorsque le joueur atteint un certain nombre de points ou lorsque toutes les vies sont perdues.

#### Gameplay
- **Contrôle** : Le joueur contrôle la raquette en bas de la fenêtre à l'aide du clavier. Le joueur peut déplacer la raquette vers le haut ou le bas pour suivre la balle.
- **Balle** : La balle est un objet circulaire qui se déplace à une vitesse constante. Elle rebondit sur les bords de la fenêtre et sur la raquette du joueur. Si la balle touche la raquette adverse, le joueur gagne un point.
- **Vitesse** : La vitesse de la balle peut être ajustée en fonction de l'activité du joueur. Plus le joueur est actif, plus la vitesse de la balle diminue.
- **Score** : Le score est affiché en temps réel et augmente chaque fois que la balle rebondit sur la raquette adverse. Le jeu se termine lorsque le joueur atteint un certain nombre de points ou lorsque toutes les vies sont perdues.

#### Structure du Code
Le code est organisé en plusieurs classes. La classe `Main` gère le cycle de vie du jeu, incluant la mise à jour de l'état du jeu, la gestion des événements clavier et la mise à jour de l'affichage. La classe `Pong` gère les attributs et les méthodes liées au jeu, comme la taille de la fenêtre, la vitesse de la balle, et la gestion des rebonds. Les méthodes `majMenu()` et `maj()` sont utilisées pour mettre à jour l'affichage du menu et du jeu, respectivement.

#### Documentation Technique
- **Fichier 1 : Main.java**
  - **Rôle** : Gère le cycle de vie du jeu.
  - **Méthode `main`** : Démarre le jeu en initialisant les attributs du jeu et en entrant dans un loop infini pour gérer l'animation du jeu.
  - **Méthode `majMenu()` et `maj()`** : Mettent à jour l'affichage du menu et du jeu, respectivement.

- **Fichier 2 : bouton.txt**
  - **Rôle** : Spécifie les actions associées aux boutons du clavier.
  - **Définitions** : Les actions associées aux boutons du clavier sont définies pour le déplacement de la barre, le lancement de la balle, et le quitter.

- **Fichier 3 : ClavierBorneArcade.java**
  - **Rôle** : Implémente la gestion du clavier pour la borne d'arcade.
  - **Méthode `keyPressed` et `keyReleased`** : Gèrent les événements clavier pour déplacer la barre et lancer la balle.

- **Fichier 4 : description.txt**
  - **Rôle** : Fournit une description du jeu.
  - **Contenu** : Décris le jeu Pong, son objectif, son principe et son gameplay.

- **Fichier 5 : Pong.java**
  - **Rôle** : Gère les attributs et les méthodes liées au jeu.
  - **Attributs** : Taille de la fenêtre, vitesse de la balle, épaisseur de la ligne, rayon de la balle.
  - **Méthodes** : Gestion des rebonds, mise à jour de l'état du jeu, et gestion des événements clavier.

Ce code permet de créer une version de Pong pour une borne d'arcade, avec une interface utilisateur clavier et une gestion des rebonds et des scores.

## Quels sont les contrôles du jeu Pong sur la borne arcade (touches/boutons) ?

### Contrôles du jeu Pong sur la borne arcade

Le jeu Pong sur la borne arcade est contrôlé par les touches et boutons suivants :

#### Touches du clavier :
- **Déplacement de la raquette :** Utilisez les touches de direction (flèches gauche et droite) pour déplacer la raquette vers la gauche et la droite.
- **Lancer la balle :** Appuyez sur la touche de lancement (par défaut, la touche "Space" sur la plupart des claviers).

#### Boutons du joystick :
- **JoyJ1Haut, JoyJ1Bas, JoyJ1Gauche, JoyJ1Droite :** Ces boutons sont utilisés pour déplacer la raquette vers le haut, le bas, la gauche et la droite.
- **BoutonJ1A, BoutonJ1B, BoutonJ1C, BoutonJ1X, BoutonJ1Y, BoutonJ1Z :** Ces boutons sont utilisés pour lancer la balle et effectuer d'autres actions dans le jeu.

#### Boutons du clavier :
- **BoutonJ1A, BoutonJ1B, BoutonJ1C, BoutonJ1X, BoutonJ1Y, BoutonJ1Z :** Ces boutons sont utilisés pour lancer la balle et effectuer d'autres actions dans le jeu.

#### Boutons du joystick :
- **BoutonJ1A, BoutonJ1B, BoutonJ1C, BoutonJ1X, BoutonJ1Y, BoutonJ1Z :** Ces boutons sont utilisés pour lancer la balle et effectuer d'autres actions dans le jeu.

### Résumé des contrôles :
- **Déplacement de la raquette :** Utilisez les touches de direction (flèches gauche et droite) ou les boutons de déplacement du joystick.
- **Lancer la balle :** Appuyez sur la touche de lancement (par défaut, "Space") ou sur le bouton de lancement du joystick.

Cette documentation fournit une vue d'ensemble des contrôles du jeu Pong sur la borne arcade, basée sur les fichiers fournis.

## Comment lancer et quitter le jeu Pong (scripts, classe main, commande) ?

### Documentation pour lancer et quitter le jeu Pong

#### 1. **Lancer le jeu Pong**
Pour lancer le jeu Pong, vous devez exécuter le fichier `Main.java`. Voici les étapes à suivre :

1. **Compilation du code** :
   ```bash
   javac Main.java
   ```
   Cette commande compile le fichier `Main.java` en un fichier exécutable `Main.class`.

2. **Exécution du code** :
   ```bash
   java Main
   ```
   Cette commande exécute le programme `Main.class` qui contient le code principal du jeu Pong.

#### 2. **Quitter le jeu Pong**
Le jeu Pong est conçu pour fonctionner en boucle indéfinie. Pour quitter le jeu, vous pouvez :

1. **Utiliser le clavier** :
   - Appuyez sur la touche `Q` pour quitter le jeu.

2. **Utiliser le bouton de la souris** :
   - Si vous utilisez un joystick, appuyez sur le bouton correspondant à la touche `Q` pour quitter le jeu.

3. **Utiliser le clavier du joystick** :
   - Si vous utilisez un joystick, appuyez sur le bouton correspondant à la touche `Q` pour quitter le jeu.

#### 3. **Documentation des boutons et touches de quitture**
- **Déplacement barre** : `rien`
- **Quitter** : `Q`
- **Lancer la balle** : `rien`
- **Touche de quitture du clavier** : `Q`
- **Touche de quitture du joystick** : `rien`

#### 4. **Exemple de commande pour quitter le jeu**
```bash
java Main
```
Après lancer le jeu, vous pouvez quitter en appuyant sur la touche `Q` du clavier ou du joystick.

### Conclusion
Pour lancer et quitter le jeu Pong, vous devez compiler et exécuter le fichier `Main.java`. Le jeu fonctionne en boucle indéfinie, mais vous pouvez quitter en appuyant sur la touche `Q` du clavier ou du joystick.

## Quelles sont les classes principales et leurs responsabilités dans Pong ?

### Documentation des Classes Principales dans le Projet Pong

#### 1. **Main.java**
- **Responsabilités :**
  - Gestion de l'application principale.
  - Création et initialisation de l'objet `Pong`.
  - Boucle principale de l'application.
  - Gestion du temps avec `Thread.sleep`.
  - Mise à jour du menu et du jeu selon le statut de l'application.
  - Réglage de la vitesse de la balle en fonction du nombre de rebonds.

#### 2. **Pong.java**
- **Responsabilités :**
  - Gestion de l'interface graphique et de l'interaction utilisateur.
  - Gestion des animations et des collisions.
  - Gestion des événements clavier et joystick.
  - Gestion des rebonds de la balle.
  - Gestion des scores et des états du jeu.
  - Gestion des menus et des options de jeu.

#### 3. **ClavierBorneArcade.java**
- **Responsabilités :**
  - Gestion des événements clavier pour les joysticks.
  - Interprétation des touches de déplacement et de lancement de la balle.
  - Gestion des touches de quitture et de lancement de la balle.

#### 4. **bouton.txt**
- **Responsabilités :**
  - Définition des actions associées aux boutons de la borne d'arcade.
  - Définition des actions de déplacement de la barre et de lancement de la balle.

#### 5. **description.txt**
- **Responsabilités :**
  - Documentation du projet.
  - Auteur et année de création du projet.
  - Description du jeu et de sa programmation.
  - Mention de la bibliothèque utilisée et de son utilisation.

### Conclusion
Les classes principales dans le projet Pong sont `Main`, `Pong`, `ClavierBorneArcade`, et `bouton.txt`. Chaque classe a des responsabilités spécifiques qui contribuent à la gestion de l'application, de l'interface utilisateur, de l'interaction avec les contrôles de la borne d'arcade, et à la documentation du projet.


# DinoRail

## Décris le jeu DinoRail (objectif, principe, gameplay) en te basant sur le code.

### Description du jeu DinoRail

#### Objectif
Le jeu DinoRail est une reproduction du jeu Chrome Dino, où le joueur doit éviter des obstacles aériens et terrestres en sautant et en se déplaçant horizontalement.

#### Principe
Le jeu se déroule sur une fenêtre de 1275x1020 pixels. Le personnage principal, le dinosaure, peut se déplacer horizontalement en sautant et en se déplaçant vers le haut ou vers le bas. Le but du jeu est d'éviter les obstacles qui apparaissent sur le chemin du dinosaure.

#### Gameplay
- **Sauter** : Le joueur peut faire sauter le dinosaure en appuyant sur le bouton de saut (en haut) ou en utilisant le joystick vers le haut.
- **Se déplacer** : Le joueur peut faire avancer le dinosaure vers la gauche ou vers la droite en utilisant le joystick vers la gauche ou vers la droite.
- **Éviter les obstacles** : Le dinosaure doit sauter pour éviter les obstacles aériens et se déplacer horizontalement pour éviter les obstacles terrestres.

#### Contraintes Techniques
- Le jeu est conçu pour fonctionner sur un Raspberry Pi.
- Les animations sont basées sur la bibliothèque MG2D.
- Le jeu utilise des textures pour représenter les obstacles et le personnage.

#### Contributions
- **Thibaut DUFEUTREL** a développé le jeu DinoRail.

#### Problèmes rencontrés
- **Animations non fonctionnelles** : Le délai entre les frames est trop court, ce qui entraîne des problèmes d'optimisation.
- **Problèmes avec la classe Texture** : Il semble y avoir des problèmes avec la gestion des textures, ce qui peut affecter la qualité visuelle du jeu.

#### Documentation
- **Fichier README.md** : Contient les informations de base sur le jeu, son objectif et les instructions de jeu.
- **Fichier bouton.txt** : Liste des boutons disponibles sur la borne d'arcade.
- **Fichier ClavierBorneArcade.java** : Implémente la gestion du clavier pour contrôler le jeu.
- **Fichier description.txt** : Contient les détails techniques du jeu et les crédits aux contributeurs.
- **Fichier DinoRail.java** : Implémente le jeu principal, y compris les animations et la gestion des obstacles.
- **Fichier Obstacle.java** : Implémente la classe d'obstacles, utilisée pour gérer les obstacles aériens et terrestres.

Ce jeu est un projet de maintenance qui s'inspire des jeux existants sur la borne d'arcade, avec des contraintes techniques spécifiques liées à l'architecture du Raspberry Pi.

## Quels sont les contrôles du jeu DinoRail sur la borne arcade (touches/boutons) ?

### Contrôles du jeu DinoRail sur la borne arcade

Le jeu DinoRail sur la borne arcade est contrôlé par les touches et les boutons du clavier de la borne. Voici les contrôles correspondants :

#### Touches du clavier :
- **Sauter** : Utilisez la touche de saut (par défaut, la touche "Space" ou "Sauter" sur le clavier physique).
- **S'abaisser** : Utilisez la touche de bascule (par défaut, la touche "Bas" ou "S'abaisser" sur le clavier physique).

#### Boutons du clavier :
- **Bouton A** : Utilisez la touche "A" sur le clavier physique.
- **Bouton B** : Utilisez la touche "B" sur le clavier physique.
- **Bouton C** : Utilisez la touche "C" sur le clavier physique.
- **Bouton X** : Utilisez la touche "X" sur le clavier physique.
- **Bouton Y** : Utilisez la touche "Y" sur le clavier physique.
- **Bouton Z** : Utilisez la touche "Z" sur le clavier physique.

### Résumé des contrôles :
- **Sauter** : Utilisez la touche de saut (par défaut, "Space").
- **S'abaisser** : Utilisez la touche de bascule (par défaut, "Bas").
- **Bouton A** : Utilisez la touche "A".
- **Bouton B** : Utilisez la touche "B".
- **Bouton C** : Utilisez la touche "C".
- **Bouton X** : Utilisez la touche "X".
- **Bouton Y** : Utilisez la touche "Y".
- **Bouton Z** : Utilisez la touche "Z".

Ces contrôles sont gérés par la classe `ClavierBorneArcade` qui implémente les méthodes de `KeyListener` pour interpréter les touches et les boutons du clavier de la borne arcade.

## Comment lancer et quitter le jeu DinoRail (scripts, classe main, commande) ?

Pour lancer et quitter le jeu DinoRail, vous pouvez suivre les étapes suivantes :

### Lancer le jeu DinoRail

1. **Exécuter le programme principal** : Le programme principal est `DinoRail.java`. Pour exécuter le jeu, vous devez compiler et exécuter ce fichier Java.

   ```bash
   javac DinoRail.java
   java DinoRail
   ```

2. **Utiliser le clavier** : Une fois le jeu lancé, vous pouvez contrôler le dinosaure avec les touches du clavier. Pour sauter, utilisez la touche `Sauter` (par exemple, `S` ou `Space`). Pour s'abaisser, utilisez la touche `Abaisser` (par exemple, `A` ou `Down`).

### Quitter le jeu DinoRail

1. **Utiliser le bouton de quitture** : Le jeu dispose d'un bouton de quitture intégré. Pour quitter le jeu, appuyez sur le bouton `Quitter` (par exemple, `Q` ou `Escape`).

2. **Fermer la fenêtre** : Si vous utilisez un environnement de développement ou un émulateur, vous pouvez également fermer la fenêtre du jeu en cliquant sur la croix de fermeture dans la fenêtre.

### Documentation supplémentaire

- **Classe ClavierBorneArcade.java** : Cette classe gère les événements clavier pour contrôler le jeu. Elle permet de détecter les touches de saut et d'abaissement.
- **Fichier README.md** : Ce fichier contient les instructions de base pour jouer au jeu et les informations sur les contributeurs et les contraintes du projet.

En suivant ces étapes, vous devriez être en mesure de lancer et de quitter le jeu DinoRail de manière efficace.

## Quelles sont les classes principales et leurs responsabilités dans DinoRail ?

### Classes principales et leurs responsabilités dans DinoRail

#### 1. **DinoRail.java**
- **Responsabilités :**
  - Gestion de l'interface utilisateur et de l'affichage.
  - Gestion des événements clavier et de la gestion des obstacles.
  - Gestion des animations et des effets sonores.
  - Gestion des statistiques et du jeu.

#### 2. **Obstacle.java**
- **Responsabilités :**
  - Création et gestion des obstacles.
  - Détection de l'obstacle en dehors de l'écran.
  - Gestion des collisions avec le dinosaure.

#### 3. **ClavierBorneArcade.java**
- **Responsabilités :**
  - Gestion des événements clavier pour les joysticks et les boutons.
  - Conversion des événements clavier en actions de jeu.
  - Gestion des mouvements et des actions du joueur.

#### 4. **Texture.java**
- **Responsabilités :**
  - Gestion des textures et des images.
  - Création et gestion des images de fond et d'obstacles.

#### 5. **FenetrePleinEcran.java**
- **Responsabilités :**
  - Création et gestion de la fenêtre de jeu.
  - Gestion de l'affichage plein écran.
  - Gestion des événements de fermeture de la fenêtre.

#### 6. **README.md**
- **Responsabilités :**
  - Documentation du projet.
  - Description de l'objectif et des fonctionnalités du jeu.
  - Historique et contributions.
  - Problèmes rencontrés et contraintes.

#### 7. **bouton.txt**
- **Responsabilités :**
  - Définition des actions associées aux boutons de la borne d'arcade.
  - Gestion des actions de base comme le mouvement du dinosaure, le saut et l'accroupissement.

#### 8. **description.txt**
- **Responsabilités :**
  - Documentation détaillée du projet.
  - Historique du projet.
  - Crédits et informations supplémentaires sur le jeu.

### Conclusion
Les classes principales dans le projet DinoRail sont **DinoRail.java**, **Obstacle.java**, **ClavierBorneArcade.java**, et **Texture.java**. Chaque classe a des responsabilités spécifiques qui contribuent à la gestion globale du jeu, de la gestion des événements clavier, de la création et de la gestion des obstacles, jusqu'à la gestion des animations et des effets sonores.


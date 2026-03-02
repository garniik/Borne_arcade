# PianoTile

## Décris le jeu PianoTile (objectif, principe, gameplay) en te basant sur le code.

### Description du Jeu PianoTile

#### Objectif
Le jeu PianoTile est un jeu de piano qui propose une expérience musicale exceptionnelle. Son objectif est de permettre aux joueurs de jouer des morceaux de musique en appuyant sur les touches du piano virtuel.

#### Principe
Le jeu PianoTile est basé sur le principe de jeu où les touches du piano apparaissent sur l'écran et le joueur doit les appuyer dans l'ordre et à la bonne vitesse pour continuer à jouer. Le jeu est conçu pour être joué sur une borne d'arcade, ce qui ajoute une dimension visuelle et interactive à l'expérience musicale.

#### Gameplay
1. **Interface de Jeu**:
   - **Interface de Jeu**: L'interface du jeu est composée d'un écran de jeu où les touches du piano apparaissent. Le joueur doit appuyer sur ces touches pour continuer à jouer.
   - **Piano**: Le jeu utilise un système de piano virtuel intégré pour générer les notes qui doivent être jouées. Les touches du piano sont affichées sur l'écran et le joueur doit les appuyer dans l'ordre et à la bonne vitesse.
   - **Score et États de Jeu**: Le score du joueur est affiché à l'écran et peut être utilisé pour suivre les progrès du joueur. L'état de jeu peut être modifié en fonction de l'avancement du joueur, avec des états tels que "Jouer", "Pause", et "Game Over".

2. **Système de Gestion**:
   - **Base de Données**: Le jeu utilise une base de données pour stocker les informations des joueurs, leurs scores, et d'autres données pertinentes.
   - **Logique du Jeu**: La logique du jeu gère les interactions entre l'interface utilisateur et le jeu, y compris la génération des notes, la gestion des touches appuyées, et la mise à jour du score.
   - **Interface Utilisateur**: L'interface utilisateur est gérée par une classe `Interface` qui s'occupe de l'affichage des touches du piano et de la gestion des événements de l'utilisateur.

3. **Menu et Navigation**:
   - **Menu**: Le jeu dispose d'un menu principal qui permet aux joueurs de naviguer entre différents états de jeu, tels que le profil, l'inscription, la connexion, etc.
   - **Pages de Jeu**: Le jeu propose plusieurs pages de jeu, comme la page de jeu principale, la page de profil, la page d'inscription, etc. Chaque page est gérée par une classe spécifique qui s'occupe de l'affichage et de la gestion des événements associés à cette page.

4. **Système de Gestion des Événements**:
   - **Événements de Jeu**: Le jeu gère les événements de jeu tels que les touches appuyées, les touches libérées, et les interactions avec l'interface utilisateur. Ces événements sont gérés par la logique du jeu et l'interface utilisateur.

5. **Système de Gestion des États de Jeu**:
   - **États de Jeu**: Le jeu peut passer entre différents états de jeu, tels que "Jouer", "Pause", et "Game Over". Chaque état de jeu est géré par une classe spécifique qui s'occupe de l'affichage et de la gestion des événements associés à cet état.

#### Conclusion
PianoTile est un jeu de piano qui propose une expérience musicale exceptionnelle sur une borne d'arcade. Le jeu utilise un système de piano virtuel intégré pour générer les notes qui doivent être jouées. Les joueurs doivent appuyer sur les touches du piano dans l'ordre et à la bonne vitesse pour continuer à jouer. Le jeu dispose d'une interface utilisateur complète avec des pages de jeu, des états de jeu, et une gestion des événements et des états de jeu pour offrir une expérience de jeu fluide et interactive.

## Quels sont les contrôles du jeu PianoTile sur la borne arcade (touches/boutons) ?

### Documentation des contrôles du jeu PianoTile sur la borne arcade

#### Introduction
Le jeu PianoTile est un jeu de piano avec des musiques exceptionnelles, développé pour une borne d'arcade. Ce document décrit les contrôles du jeu, basés sur les fichiers fournis.

#### Contrôles du jeu PianoTile

##### Boutons de la borne d'arcade
Le jeu PianoTile est contrôlé par les boutons de la borne d'arcade. Les mouvements des notes sur le piano sont gérés par les touches de la borne d'arcade. Les mouvements des notes sont déterminés par les touches de la borne d'arcade, sans spécification de mouvement spécifique dans le fichier `bouton.txt`.

##### Interface utilisateur
L'interface utilisateur du jeu est gérée par l'objet `Interface` de la classe `Game` dans le fichier `app/game.py`. L'interface permet de gérer les interactions utilisateur, comme le retour au menu principal et le lancement du jeu.

##### Affichage et gestion des états
L'affichage du jeu est géré par les classes `GameView` et `MenuView` dans les fichiers `ui/layout/gameView.py` et `ui/layout/menuView.py`. Ces classes gèrent l'affichage des états du jeu, comme le menu principal et la vue du jeu.

##### Logique du jeu
La logique du jeu est gérée par la classe `Logic` dans le fichier `app/game.py`. Cette classe gère les actions et les interactions du jeu, comme la gestion des notes et des scores.

##### Base de données
La base de données est gérée par la classe `Database` dans le fichier `data/database.py`. Cette classe permet de stocker et de récupérer les données du jeu, comme les scores et les statistiques.

##### Conclusion
Les contrôles du jeu PianoTile sont principalement gérés par les boutons de la borne d'arcade, avec l'interface utilisateur et la logique du jeu gérés par les classes de l'application. Les mouvements des notes sont déterminés par les touches de la borne d'arcade, sans spécification de mouvement spécifique dans le fichier `bouton.txt`.

Pour plus de détails sur les contrôles spécifiques, il est recommandé de consulter le code source complet et les commentaires associés.

## Comment lancer et quitter le jeu PianoTile (scripts, classe main, commande) ?

### Lancer et Quitter le Jeu PianoTile

#### **1. Lancer le Jeu PianoTile**

Pour lancer le jeu PianoTile, vous devez exécuter le script `PianoTileArcade.sh`. Ce script est un fichier shell qui vous permet de démarrer le jeu en utilisant Python.

```bash
# Exécution du script
./PianoTileArcade.sh
```

#### **2. Quitter le Jeu PianoTile**

Pour quitter le jeu PianoTile, vous pouvez utiliser les boutons de retour et de pause disponibles dans l'interface du jeu. Voici les étapes à suivre :

1. **Bouton de Retour** : 
   - Appuyez sur le bouton "Retour" pour revenir à l'écran de menu principal.

2. **Bouton de Pause** : 
   - Si le jeu est en cours de jeu, vous pouvez appuyer sur le bouton "Pause" pour interrompre le jeu temporairement. Pour reprendre le jeu, appuyez à nouveau sur le bouton "Pause".

3. **Bouton de Quitter** : 
   - Pour quitter définitivement le jeu, vous pouvez appuyer sur le bouton "Quitter" qui se trouve généralement dans l'écran de menu principal.

#### **3. Structure de l'Interface et des Classes**

- **Classe `Game`** : Cette classe est la classe principale du jeu. Elle contient les getters pour accéder aux différents composants du jeu, tels que la base de données, l'interface et la logique.

- **Classe `GameView`** : Cette classe gère la vue du jeu. Elle définit les dimensions de la zone de jeu, la position des touches du piano, et les paramètres de jeu tels que le score et l'état de fin de jeu.

- **Classe `MenuView`** : Cette classe gère l'interface de menu du jeu. Elle permet de naviguer entre différents états de page, tels que le profil, l'inscription, la connexion, etc.

#### **4. Documentation Technique**

- **Fichier `README.md`** : Ce fichier contient les instructions de base pour lancer et quitter le jeu.

- **Fichier `app/game.py`** : Ce fichier contient la classe `Game` qui est la classe principale du jeu. Elle contient les getters pour accéder aux différents composants du jeu.

- **Fichier `ui/layout/gameView.py`** : Ce fichier contient la classe `GameView` qui gère la vue du jeu. Elle définit les dimensions de la zone de jeu et les paramètres de jeu.

- **Fichier `ui/layout/menuView.py`** : Ce fichier contient la classe `MenuView` qui gère l'interface de menu du jeu. Elle permet de naviguer entre différents états de page.

#### **5. Conclusion**

Pour lancer et quitter le jeu PianoTile, vous devez exécuter le script `PianoTileArcade.sh`. Pour quitter le jeu, vous pouvez utiliser les boutons de retour et de quitter disponibles dans l'interface du jeu. Les classes `Game`, `GameView`, et `MenuView` sont les principales classes implémentées pour gérer le jeu et son interface.

## Quelles sont les classes principales et leurs responsabilités dans PianoTile ?

### Classes Principales et Responsabilités dans PianoTile

#### 1. **Game**
- **Responsabilités :**
  - Gestion de l'interface utilisateur.
  - Interaction avec la base de données.
  - Gestion de la logique du jeu.
  
- **Méthodes principales :**
  - `getDatabase()`: Renvoie l'instance de la base de données.
  - `getInterface()`: Renvoie l'instance de l'interface utilisateur.
  - `getLogic()`: Renvoie l'instance de la logique du jeu.

#### 2. **GameView**
- **Responsabilités :**
  - Gestion de la vue du jeu.
  - Gestion des dimensions de la fenêtre de jeu.
  - Gestion des événements de jeu.
  
- **Méthodes principales :**
  - `getWindowManager()`: Renvoie l'instance de la gestionnaire de fenêtre.
  - `getPlayWidth()`: Renvoie la largeur de la zone de jeu.
  - `__init__`: Initialisation de la vue du jeu avec le gestionnaire de fenêtre.

#### 3. **MenuView**
- **Responsabilités :**
  - Gestion de la vue du menu.
  - Navigation entre les différentes pages du menu.
  
- **Méthodes principales :**
  - `__init__`: Initialisation de la vue du menu avec le gestionnaire de fenêtre.
  - `__pageViews`: Dictionnaire contenant les instances des différentes pages du menu.

#### 4. **GamePage**
- **Responsabilités :**
  - Affichage de la page de jeu.
  - Gestion des événements de jeu.
  
- **Méthodes principales :**
  - `affichagePage()`: Affiche les boutons "Retour" et "Play" sur la page de jeu.

#### 5. **Piano**
- **Responsabilités :**
  - Gestion des touches de piano.
  
- **Méthodes principales :**
  - Non spécifiées dans le code fourni.

#### 6. **bouton.txt**
- **Responsabilités :**
  - Contient des informations sur les mouvements des boutons de piano.
  
- **Contenu :**
  - Liste des mouvements des boutons de piano.

#### 7. **description.txt**
- **Responsabilités :**
  - Description du jeu PianoTile.
  
- **Contenu :**
  - Informations sur le jeu PianoTile, son créateur et sa date de création.

#### 8. **PianoTileArcade.sh**
- **Responsabilités :**
  - Exécution du projet PianoTile.
  
- **Contenu :**
  - Script Bash pour exécuter le projet en Python.

### Conclusion
Les classes principales dans PianoTile sont `Game`, `GameView`, `MenuView`, et `GamePage`. Chaque classe a des responsabilités spécifiques liées à la gestion de l'interface utilisateur, de la logique du jeu, et de la navigation entre les différentes pages du menu. Les autres fichiers et scripts sont soit des configurations, soit des scripts d'exécution.


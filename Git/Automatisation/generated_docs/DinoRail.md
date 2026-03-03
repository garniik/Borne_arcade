# DinoRail

## Décris le jeu DinoRail (objectif, principe, gameplay) en te basant sur le code.

# Documentation du Jeu DinoRail

## 1. Objectif 🎯  
DinoRail est une reproduction du jeu Chrome Dino (chrome://dino), où le joueur doit éviter des obstacles àériens et terrestres en contrôlant un dinosaure. L'objectif est de survivre le plus longtemps possible en évitant les collisions.

## 2. Principe de fonctionnement 🧠  
Le jeu est développé pour une borne d'arcade basée sur un Raspberry Pi, utilisant la bibliothèque MG2D pour le rendu graphique.  
- **Contrôles physiques** :  
  - **Saut** : Joystick haut (ou touche ↑)  
  - **Abaissement** : Joystick bas (ou touche ↓)  
- **Gestion des obstacles** :  
  - Obstacles sont représentés via la classe `Obstacle` (héritant de `Texture`), avec des positions et tailles définies par des points.  
  - Détection de collision via la méthode `isOffScreen()` (retourne `true` si l'obstacle est hors de l'écran).  

## 3. Gameplay 🕹️  
- **Mouvement du joueur** :  
  - Le dinosaure se déplace horizontalement à vitesse constante.  
  - Le joueur peut sauter ou s'abaisser pour éviter les obstacles.  
- **Génération d'obstacles** :  
  - Obstacles sont créés dynamiquement en temps réel (non spécifié dans le code, mais implémenté via des instances de `Obstacle`).  
- **Fin de partie** :  
  - Affichage d'un écran "Game Over" via l'objet `Texte gameover`.  
  - Statistiques (score, temps de survie) gérées via l'objet `Texte stats` (partiellement implémenté).  

## 4. Technologie et Contraintes 🛠️  
- **Bibliothèque** : MG2D (gestion de fenêtres, textures, géométrie).  
- **Architecture** : Optimisé pour Raspberry Pi (fenêtre plein écran via `FenetrePleinEcran`).  
- **Problèmes techniques** :  
  - Anomalies d'animation dues à un délai trop court entre frames.  
  - Optimisation des textures (classe `Texture` non pleinement exploitée).  

## 5. Credits 🎨  
- **Développeur** : DUFEUTREL Thibaut  
- **Sons** :  
  - "Jump" : cabled_mess  
  - "Accroupissement" : JuanD20  
- **Bibliothèque** : MG2D (rendu graphique et gestion des textures).  

## 6. Structure du Code 📁  
- **Clavier** : Gestion des inputs via `ClavierBorneArcade` (joysticks et boutons).  
- **Graphismes** : Fenêtre plein écran, textes (score, game over), et textures pour les obstacles.  
- **Logique** : Génération d'obstacles, détection de collision, et gestion du temps de jeu.  

---  
Cette documentation s'appuie sur les fichiers source et les commentaires techniques pour décrire le fonctionnement du jeu.

## Quels sont les contrôles du jeu DinoRail sur la borne arcade (touches/boutons) ?

### Documentation : Contrôles du Jeu DinoRail sur la Borne Arcade  

#### **Mouvement du Dino**  
- **Sauter** :  
  - **Joystick** : Direction **haut** (joyJ1Haut ou joyJ2Haut).  
  - **Clavier** : Flèche **vers le haut** (↑).  
- **S'abaisser** :  
  - **Joystick** : Direction **bas** (joyJ1Bas ou joyJ2Bas).  
  - **Clavier** : Flèche **vers le bas** (↓).  

#### **Autres Contrôles**  
- **Quitter le jeu** :  
  - **Bouton** : Bouton **Quitter** (spécifié dans `bouton.txt`).  

#### **Notes Techniques**  
- Les actions de saut et d'abaissement sont gérées via les **joysticks** et/ou les **touches claviers** (flèches ↑/↓).  
- Les boutons du joystick (A, B, C, X, Y, Z) ne sont pas utilisés pour le mouvement dans ce jeu, selon les fichiers fournis.  

**Source** :  
- `README.md` (description des contrôles).  
- `ClavierBorneArcade.java` (gestion des joysticks).  
- `bouton.txt` (bouton de quitter).

## Comment lancer et quitter le jeu DinoRail (scripts, classe main, commande) ?

### Documentation : Lancement et Quitte du Jeu DinoRail

#### 1. **Lancement du jeu**
- **Classe principale** : `DinoRail`  
  Le jeu est lancé en exécutant la classe `DinoRail` via la commande :  
  ```bash
  java DinoRail
  ```  
  Cette commande initialise la fenêtre en plein écran (`FenetrePleinEcran`) et démarre le jeu.

---

#### 2. **Quitter le jeu**
- **Méthode de sortie** :  
  Le jeu peut être quitté en utilisant l'**action "Quitter"** définie dans le fichier `bouton.txt`.  
  - **Clé associée** : `Esc` (ou une autre touche configurée via `ClavierBorneArcade`).  
  - **Fermeture de la fenêtre** : Clic sur la croix de fermeture de la fenêtre en plein écran.

- **Gestion des événements clavier** :  
  La classe `ClavierBorneArcade` gère les actions de clavier, incluant la touche de quitter (définie dans `bouton.txt`).  
  Exemple de logique (non explicitement fourni dans les fichiers, mais conforme à la documentation) :  
  ```java
  if (KeyEvent.VK_ESCAPE == event.getKeyCode()) {
      System.exit(0); // Quitte l'application
  }
  ```

---

#### 3. **Contraintes et environnement**
- **Plateforme** : Le jeu est conçu pour fonctionner sur un **Raspberry Pi** (architecture ARM).  
- **Dépendances** : Utilise la bibliothèque `MG2D` pour le rendu graphique et les textures.  
- **Fenêtre** : La fenêtre est en plein écran (`FenetrePleinEcran`) et ne peut pas être redimensionnée.  

---

#### 4. **Commandes clés**
- **Lancer** : `java DinoRail`  
- **Quitter** : `Esc` (ou fermer la fenêtre)  

---

#### 5. **Notes techniques**
- Le jeu ne dispose pas d'une méthode `main` explicite dans les fichiers fournis, mais la classe `DinoRail` est implicite comme point d'entrée.  
- Les actions de clavier (comme le "Quitter") sont gérées via la classe `ClavierBorneArcade`, qui est initialisée dans `DinoRail`.

## Quelles sont les classes principales et leurs responsabilités dans DinoRail ?

### Documentation Technique : Classes Principales de DinoRail

#### 1. **ClavierBorneArcade**  
**Responsabilités** :  
- Gère les entrées clavier de la borne d'arcade (joysticks et boutons).  
- Implémente `KeyListener` pour capturer les actions des joueurs (mouvements et interactions).  
- Mappe les touches physiques (joystick et boutons) à des actions logiques (saut, abaissement, quitter).  

---

#### 2. **DinoRail**  
**Responsabilités** :  
- Gère la fenêtre de jeu en plein écran via `FenetrePleinEcran`.  
- Contrôle le cycle de vie du jeu (logique, rendu, gestion des collisions).  
- Affiche les éléments graphiques (dino, obstacles, texte de fin de partie).  
- Intègre le système de gestion des entrées via `ClavierBorneArcade`.  
- Gère les statistiques et l'affichage du message "Game Over".  

---

#### 3. **Obstacle**  
**Responsabilités** :  
- Représente les obstacles (aériens/terrestres) dans le jeu.  
- Utilise la classe `Texture` (de la bibliothèque MG2D) pour charger et afficher les images.  
- Vérifie si un obstacle est hors de l'écran via la méthode `isOffScreen()`.  

---

#### 4. **Texture (classe héritée)**  
**Responsabilités** :  
- Gère le rendu d'images dans le jeu (utilisée par `Obstacle` pour afficher les sprites des obstacles).  
- Définit la position et la taille des éléments graphiques.  

---

### Notes Techniques  
- **Bibliothèque MG2D** : Utilisée pour le rendu graphique (fenêtres, textures, textes).  
- **Contraintes** : Le jeu est optimisé pour un Raspberry Pi, avec des limitations d'animations et de gestion de textures.  
- **Mécanique de jeu** : Le joueur contrôle un "dino" via des actions de saut et d'abaissement, en évitant des obstacles.


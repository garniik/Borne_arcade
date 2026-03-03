# Columns

## Décris le jeu Columns (objectif, principe, gameplay) en te basant sur le code.

### Documentation du Jeu Columns

---

#### **1. Objectif du jeu**  
Le jeu **Columns** est un puzzle où l'objectif est d'aligner **trois gemmes de la même couleur** pour les faire disparaître. Les joueurs doivent éliminer les gemmes en créant des combinaisons de trois ou plus, tout en gérant un **temps limité** (indiqué par le message "SACLIGNOTT!!!"). L'accumulation de gemmes non éliminées entraîne une perte de vie.

---

#### **2. Principe du jeu**  
- **Grille de gemmes** : La partie se déroule sur une grille de gemmes (probablement 8 colonnes x 10 lignes).  
- **Mouvement des gemmes** : Les joueurs peuvent déplacer des gemmes en les **échangeant** avec celles adjacentes (via des touches de direction ou des boutons).  
- **Élimination** : Lorsque trois ou plus de gemmes identiques sont alignées horizontalement ou verticalement, elles disparaissent, et des nouvelles gemmes tombent pour remplir les espaces.  
- **Temps** : Le jeu comporte un **chronomètre** (non explicitement codé, mais suggéré par le message "SACLIGNOTT!!!").  

---

#### **3. Gameplay**  
- **Contrôles** :  
  - **Joystick J1** : Déplacement des gemmes (HAUT, BAS, GAUCHE, DROITE).  
  - **Boutons J1** :  
    - **ACTION** : Échanger des gemmes.  
    - **QUITTER** : Quitter la partie.  
  - **Joystick J2** : Non implémenté (partie du code tronquée).  
- **Logique de jeu** :  
  - La classe `Colone` gère la logique des colonnes de gemmes, avec une méthode `intervertir()` pour échanger des gemmes.  
  - La classe `Gemme` définit les couleurs des gemmes (JAUNE, ORANGE, VERT, VIOLET, ROUGE, BLEU) et charge leurs textures depuis des fichiers images (`img/game/gems/...`).  
  - La classe `Partie` (non entièrement visible) gère la logique de détection des combinaisons, la gestion du temps, et la mise à jour de l'affichage.  

---

#### **4. Structure Technique**  
- **Fenêtre** :  
  - Utilise `FenetrePleinEcran` pour un affichage en plein écran (1280x1024).  
  - Affichage des primitives et textures activé.  
- **Menu** :  
  - Gère l'entrée du jeu avec des options : "1 Joueur", "2 Joueurs", "Quitter".  
  - Utilise des textures (`bg`, `title`) et des rectangles pour l'interface.  
- **Gestion des inputs** :  
  - `ClavierBorneArcade` mappe les touches du clavier aux actions (directions et boutons).  
  - Constantes définies dans `Controles.java` (ex. `HAUT`, `ACTION`, `QUITTER`).  

---

#### **5. Fichiers Clés**  
- **Main.java** : Point d'entrée, initialise la fenêtre et les gestionnaires d'événements.  
- **Menu.java** : Gère l'affichage et les options du menu.  
- **Gemme.java** : Définit les couleurs et textures des gemmes.  
- **Colone.java** : Gère la logique des colonnes et des échanges de gemmes.  
- **ClavierBorneArcade.java** : Mappe les touches du clavier aux actions du jeu.  

---

#### **6. Points à Développer**  
- **Gestion du temps** : Implémenter un chronomètre et un système de pénalités.  
- **Niveaux de difficulté** : Ajouter des paramètres de difficulté (vitesse de chute des gemmes).  
- **Multijoueur** : Finaliser la logique pour deux joueurs (via `Partie` et `ClavierBorneArcade`).  
- **Effets sonores** : Ajouter des sons pour les éliminations et les collisions.  

--- 

Cette documentation s'appuie sur les fichiers fournis et les constantes/structures de code pour décrire le jeu de manière technique et structurée.

## Quels sont les contrôles du jeu Columns sur la borne arcade (touches/boutons) ?

**Documentation des Contrôles du Jeu Columns sur la Borne Arcade**

---

### **Contrôles du Jeu**
Les contrôles du jeu **Columns** sur la borne arcade sont définis via des constantes et une configuration spécifique. Voici les touches/boutons associés aux actions principales :

#### **1. Joystick (Joueur 1)**
- **Direction** :
  - **Haut** : `Controles.HAUT` (déplacement de la barre vers le haut)
  - **Bas** : `Controles.BAS` (déplacement de la barre vers le bas)
  - **Gauche** : `Controles.GAUCHE` (déplacement de la barre vers la gauche)
  - **Droite** : `Controles.DROITE` (déplacement de la barre vers la droite)

#### **2. Boutons (Joueur 1)**
- **Quitter** : `Controles.QUITTER` (action de quitter le jeu)
- **Intervertir** : Action associée à `Controles.ACTION` (échange des gemmes en haut/bas)

#### **3. Configuration des Boutons**
Le fichier `bouton.txt` définit les associations :
```
Déplacement barre:rien:rien:Quitter:Intervertir:rien:rien
```
- **"Quitter"** : Bouton de sortie (probablement associé à `Controles.QUITTER`)
- **"Intervertir"** : Bouton pour échanger les gemmes (associé à `Controles.ACTION`)

---

### **Notes Techniques**
- Les **joysticks** (`joyJ1`, `joyJ2`) gèrent les déplacements de la barre.
- Les **boutons** (`boutonJ1A`, `boutonJ1B`, etc.) sont utilisés pour des actions spécifiques (quitter, intervertir).
- Les constantes `Controles` (ex: `HAUT`, `BAS`, `ACTION`, `QUITTER`) définissent les codes associés aux touches/boutons dans le code source.

---

### **Résumé**
| Action               | Contrôle                  | Code Constante       |
|----------------------|---------------------------|----------------------|
| Déplacement barre    | Joystick (Haut/Bas/Gauche/Droite) | `Controles.HAUT`, `BAS`, `GAUCHE`, `DROITE` |
| Quitter le jeu      | Bouton spécifique         | `Controles.QUITTER`  |
| Intervertir gemmes   | Bouton spécifique         | `Controles.ACTION`   |

Ces contrôles sont implémentés via la classe `ClavierBorneArcade` et les constantes de `Controles`.

## Comment lancer et quitter le jeu Columns (scripts, classe main, commande) ?

### Documentation : Lancement et Quitte du Jeu Columns

---

#### **1. Lancement du Jeu**
- **Script principal** :  
  Exécutez la classe `Main` via le JDK :  
  ```bash
  java Main
  ```
  - Le programme initialise une fenêtre en plein écran (`FenetrePleinEcran`) avec le titre "Columns".
  - Un gestionnaire de clavier (`ClavierBorneArcade`) est associé à la fenêtre pour gérer les entrées du joueur.

---

#### **2. Quitte du Jeu**
- **Méthodes de sortie** :  
  Le jeu peut être quitté via deux mécanismes :
  1. **Clavier** :  
     - Appuyez sur le bouton **"Quitter"** associé au joueur (mappé à `Controles.QUITTER`).  
     - Ce bouton est configuré dans le fichier `bouton.txt` (ligne : `Quitter:Intervertir`).  
     - Lors de la détection de cette entrée, le programme met fin à la boucle de jeu et ferme la fenêtre.

  2. **Menu principal** :  
     - Sélectionnez l'option **"Quitter"** (`Menu.BOUTONEXIT`) dans le menu principal.  
     - Cela active la logique de fermeture via la variable `fermetureJeu` dans la classe `Main`.

- **Fermeture de la fenêtre** :  
  La fenêtre (`FenetrePleinEcran`) est fermée via la méthode `setVisible(false)` ou `dispose()` lors de la détection de l'option de sortie.

---

#### **3. Commandes Clavier**
- **Bouton "Quitter"** :  
  - Mappé à `Controles.QUITTER` (valeur `2`).  
  - Correspond à une touche spécifique sur la borne d'arcade (à définir dans `ClavierBorneArcade`).

- **Autres commandes** :  
  - Les mouvements et actions sont gérés via `Controles.HAUT`, `Controles.BAS`, etc. (détaillés dans `Controles.java`).

---

#### **4. Structure du Code**
- **Main.java** :  
  - Contient la boucle principale et la logique de gestion des menus/parties.  
  - Utilise `FenetrePleinEcran` pour la fenêtre et `ClavierBorneArcade` pour les entrées.

- **Menu.java** :  
  - Gère l'affichage et les transitions entre les états du menu (statut `STATUTMENU`, `BOUTONEXIT`, etc.).

- **ClavierBorneArcade.java** :  
  - Implémente les écouteurs de clavier pour les boutons et joysticks de la borne.

---

#### **5. Notes Techniques**
- **Fermeture propre** :  
  Le jeu ferme la fenêtre et libère les ressources via `FenetrePleinEcran` et `ClavierBorneArcade`.
- **Compatibilité** :  
  Le code est conçu pour fonctionner sur une borne d'arcade avec un clavier personnalisé (via `ClavierBorneArcade`).

## Quelles sont les classes principales et leurs responsabilités dans Columns ?

### Documentation Technique : Projet Columns

#### **Classes Principales et Responsabilités**

1. **`Main`**  
   - **Responsabilité** : Point d'entrée du jeu.  
   - **Fonctions** :  
     - Initialise la fenêtre en plein écran (`FenetrePleinEcran`).  
     - Configure le gestionnaire de clavier (`ClavierBorneArcade`).  
     - Gère l'état du jeu (menu principal, partie en cours).  
     - Crée les instances de `Menu` et `Partie` pour démarrer le jeu.  

2. **`Menu`**  
   - **Responsabilité** : Gestion de l'interface de menu.  
   - **Fonctions** :  
     - Affiche les options de démarrage (1 joueur, 2 joueurs, quitter).  
     - Gère les interactions utilisateur via les boutons du clavier.  
     - Définit les états du menu (`STATUTMENU`, `BOUTON1JOUEUR`, etc.).  
     - Intègre un fond d'écran et des éléments graphiques (textes, boutons).  

3. **`ClavierBorneArcade`**  
   - **Responsabilité** : Gestion des entrées clavier pour la borne d'arcade.  
   - **Fonctions** :  
     - Mappe les touches du clavier aux actions du jeu (directions, boutons).  
     - Transmet les événements clavier à l'application via `KeyListener`.  
     - Supporte jusqu'à 6 boutons par joueur (A/B/C/X/Y/Z).  

4. **`Colone`**  
   - **Responsabilité** : Gestion des colonnes de gemmes.  
   - **Fonctions** :  
     - Stocke et gère trois gemmes par colonne.  
     - Implémente la logique d'échange des gemmes (méthode `intervertir()`).  
     - Fournit des accesseurs pour les positions et états des gemmes.  

5. **`Controles`**  
   - **Responsabilité** : Définition des codes constants pour les actions du jeu.  
   - **Fonctions** :  
     - Définit les codes pour les directions (HAUT, BAS, etc.) et les boutons (ACTION, QUITTER).  
     - Centralise les valeurs numériques pour faciliter la gestion des entrées.  

6. **`Gemme`**  
   - **Responsabilité** : Représentation des gemmes du jeu.  
   - **Fonctions** :  
     - Définit les couleurs des gemmes (JAUNE, ORANGE, etc.) et leur apparence (textures).  
     - Gère les états spéciaux (VIDE, NBFRAMESUPPR).  
     - Fournit des textures préchargées pour le rendu graphique.  

---

#### **Structure du Projet**
- **Fenêtre** : Gérée par `FenetrePleinEcran` pour le rendu en plein écran.  
- **Gestion des entrées** : Centralisée via `ClavierBorneArcade` et `Controles`.  
- **Logique de jeu** : Gérée par `Partie` (non complet dans les fichiers fournis).  
- **Graphismes** : Utilisation de `Texture` et `Point` pour le rendu des gemmes.  

Cette documentation reflète les rôles clés des classes principales et leur interaction dans le cadre du jeu Columns.


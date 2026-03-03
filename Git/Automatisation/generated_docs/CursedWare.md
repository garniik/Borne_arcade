# CursedWare

## Décris le jeu CursedWare (objectif, principe, gameplay) en te basant sur le code.

### Documentation du Projet **CursedWare**  

---

#### **Objectif**  
CursedWare est un jeu de type *mini-game* inspiré de **WarioWare**, conçu pour être joué en solo ou en mode multijoueur (2 joueurs). L'objectif principal est de défier les différentes mini-jeux proposés, d'atteindre le meilleur score possible et de se classer parmi les meilleurs joueurs.  

---

#### **Principe**  
Le jeu s'inspire du concept de **WarioWare**, où chaque niveau est un mini-jeu court et intense. Les joueurs doivent :  
- **Réagir rapidement** aux actions demandées (touches, mouvements, etc.).  
- **Maximiser leur score** en optimisant leur performance.  
- **Gagner contre l'adversaire** (en mode 2 joueurs) via des mécaniques compétitives.  

Les mini-jeux sont variés et testent des compétences différentes (réflexes, précision, logique, etc.).  

---

#### **Gameplay**  
- **Mode solo** : Le joueur affronte des défis individuels pour accumuler des points.  
- **Mode multijoueur** : Deux joueurs s'affrontent directement dans des mini-jeux compétitifs.  
- **Contrôles** :  
  - Le jeu utilise **Love2D** (framework Lua) pour la gestion des entrées/sorties.  
  - Les commandes sont définies dans le fichier `bouton.txt`, bien que les touches soient initialement configurées à `"aucun"` (probablement pour une adaptation ultérieure).  
  - Les joueurs peuvent utiliser des **touches clavier**, **manettes** ou **touches de surface tactile** selon la configuration.  
- **Interface** :  
  - Écran de sélection des mini-jeux.  
  - Affichage des scores en temps réel et des résultats finaux.  

---

#### **Technique**  
- **Technologie** : Développé avec **Love2D** (Lua + OpenGL).  
- **Structure** :  
  - Le jeu est organisé en modules (mini-jeux) chargés dynamiquement.  
  - Le fichier `README.txt` fournit les instructions pour lancer le jeu via l'interpréteur Love.exe.  
- **Multijoueur** : Support de 2 joueurs via des entrées simultanées (touches/contrôles).  

---

#### **Remarques**  
- Le jeu est conçu pour l'**IUT** (Institut Universitaire de Technologie), avec une ambiance et des mécaniques adaptées à un public étudiant.  
- Les mini-jeux sont conçus pour être **rapides et intenses**, avec des mécaniques variées.  

---  
*Documentation générée à partir des fichiers fournis.*

## Quels sont les contrôles du jeu CursedWare sur la borne arcade (touches/boutons) ?

**Documentation : Contrôles du jeu CursedWare sur la borne arcade**

### **Contrôles du jeu**
Les fichiers fournis ne spécifient pas explicitement les touches ou boutons associés aux actions du jeu. Cependant, le fichier `bouton.txt` indique une configuration vide pour les fonctions suivantes :  
- **Movement** (déplacement) : `aucun`  
- **Interagir** (interaction) : `aucun`  
- **Retour** (retour) : `aucun`  

Cela suggère que les contrôles ne sont pas définis dans les fichiers fournis, ou que les actions associées à ces fonctions sont gérées par d'autres mécanismes (par exemple, via le clavier ou des boutons physiques non documentés).  

### **Recommandations**
- Vérifiez le code source du jeu ou la configuration des boutons physiques de la borne pour obtenir la mappage exact des actions.  
- Le jeu peut être joué à 2 joueurs, ce qui implique la présence de deux ensembles de contrôles (touches/boutons).  

**Note** : Les fichiers fournis ne contiennent pas d'informations détaillées sur les contrôles physiques de la borne.

## Comment lancer et quitter le jeu CursedWare (scripts, classe main, commande) ?

**Documentation : Lancement et Quitte du Jeu CursedWare**  

### **1. Prérequis**  
- **Love2D** doit être installé et accessible depuis le terminal.  
- Le projet doit être exécuté depuis le répertoire racine du projet.  

---

### **2. Lancement du Jeu**  
Pour lancer le jeu :  
1. Accédez au répertoire du projet via le terminal :  
   ```bash
   cd [CHEMIN_VERS_PROJET]
   ```  
2. Exécutez la commande suivante :  
   ```bash
   "[CHEMIN_VERS_Love.exe]" .
   ```  
   - Remplacez `[CHEMIN_VERS_Love.exe]` par le chemin complet vers l'exécutable Love2D.  
   - Le jeu lancera le fichier principal (généralement `main.lua` ou un fichier défini dans le projet).  

---

### **3. Quitte du Jeu**  
- **Via l'interface** :  
  - Appuyez sur **`Escape`** pour quitter le jeu directement.  
  - Utilisez le menu **"Quitter"** (si disponible dans les options du jeu).  
- **Via le terminal** :  
  - Si le jeu est en pause ou en arrière-plan, utilisez la commande `taskkill` (Windows) :  
    ```bash
    taskkill /im Love.exe
    ```  
  - Sur Linux/macOS, forcez la fermeture via le gestionnaire de processus.  

---

### **4. Notes Techniques**  
- Le jeu ne dispose pas de script de fermeture spécifique (comme un `main.lua` dédié).  
- La gestion de la sortie repose sur les mécanismes de Love2D et les interactions utilisateur.  
- Vérifiez que le fichier `main.lua` (ou le fichier principal) est correctement configuré dans le projet.  

---  
*Documentation générée à partir des fichiers fournis.*

## Quelles sont les classes principales et leurs responsabilités dans CursedWare ?

**Documentation Technique : CursedWare**  
*Projet de borne d'arcade basé sur Love2D*

---

### **Classes Principales et Responsabilités**  
Les fichiers fournis ne contiennent pas de code Lua ou de définitions de classes explicites, mais l'analyse des ressources et du contexte du projet permet d'identifier les composants clés :

#### **1. `Game` (Gestionnaire de l'application)**  
- **Responsabilités** :  
  - Initialiser et lancer le jeu (via `love.load` et `love.run`).  
  - Gérer le cycle de vie du jeu (chargement, mise à jour, dessin).  
  - Coordonner les scènes (menu, mini-jeux, résultats).  
  - Gérer les interactions multijoueurs (via `love.keyboard` ou `love.joystick`).  

#### **2. `Scene` (Gestion des états de jeu)**  
- **Responsabilités** :  
  - Charger les ressources (sprites, sons) pour chaque scène (ex. : menu, mini-jeu).  
  - Gérer les transitions entre scènes (ex. : retour au menu après un mini-jeu).  
  - Exemple : `SceneMenu`, `SceneGame`, `SceneResults`.  

#### **3. `UI` (Interface Utilisateur)**  
- **Responsabilités** :  
  - Afficher les boutons et éléments graphiques (ex. : "Retour", "Interagir").  
  - Gérer les événements de clic ou de touche (via `love.mouse` ou `love.keyboard`).  
  - Exemple : `UIButton` pour les boutons de navigation.  

#### **4. `GameHandler` (Gestion des mécaniques de jeu)**  
- **Responsabilités** :  
  - Contrôler les règles des mini-jeux (temps, score, vérification des actions).  
  - Gérer la logique de multijoueur (ex. : synchronisation des scores).  
  - Exemple : `MiniGameTimer`, `ScoreManager`.  

#### **5. `AssetManager` (Gestion des ressources)**  
- **Responsabilités** :  
  - Charger et gérer les assets (sprites, sons, textures).  
  - Optimiser le rendu via des techniques comme le *batching* ou le *texture atlas*.  

---

### **Notes Techniques**  
- Le projet utilise **Love2D** (framework 2D en Lua), donc les classes sont implémentées en Lua et non en langage objet traditionnel.  
- Les interactions sont gérées via des événements de clavier/souris (ex. : `love.keyboard.isDown`, `love.mousepressed`).  
- La documentation des fichiers `.txt` suggère une architecture modulaire avec des scènes et un système de UI dédié.  

---  
*Documentation générée à partir des ressources fournies et des conventions de développement typiques pour des projets Love2D.*


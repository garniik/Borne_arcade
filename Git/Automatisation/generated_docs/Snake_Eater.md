# Snake_Eater

## Décris le jeu Snake_Eater (objectif, principe, gameplay) en te basant sur le code.

**Documentation du jeu Snake_Eater**

---

### **Objectif du jeu**  
Le jeu **Snake_Eater** est une version classique de *Snake* où l'objectif est de manger un maximum de pommes en évitant de heurter les murs ou le corps du serpent. Si le joueur perd trop rapidement, le jeu se moque de lui (comme indiqué dans le fichier `description.txt`).

---

### **Principe du jeu**  
- **Contrôle** : Le joueur utilise un clavier arcade (via la classe `ClavierBorneArcade.java`) pour diriger le serpent.  
  - **Joueur 1** : Joystick `joyJ1` (haut/bas/gauche/droite) et boutons `boutonJ1A`, `boutonJ1B`, `boutonJ1C` (bas) et `boutonJ1X`, `boutonJ1Y`, `boutonJ1Z` (haut).  
  - **Joueur 2** : Joystick `joyJ2` et boutons `boutonJ2A`, `boutonJ2B`, `boutonJ2C`, `boutonJ2X`, `boutonJ2Y`, `boutonJ2Z`.  
- **Mécanique** :  
  - Le serpent se déplace en diagonale ou en ligne droite, selon la direction choisie.  
  - Chaque fois que le serpent mange une pomme, il grandit (ajout d'une segment) et le score augmente.  
  - Si le serpent heurte un mur ou son propre corps, la partie se termine.  

---

### **Gameplay**  
- **Génération des pommes** :  
  - Les pommes sont générées aléatoirement sur une grille de 30x30 pixels (via `Nourriture.java` et `Pomme.java`).  
  - Elles apparaissent à des positions multiples de 30 pixels pour aligner le jeu sur une grille.  
- **Collision et score** :  
  - Lorsque le serpent mange une pomme, un nouveau segment est ajouté à la queue du serpent (via `Serpent.java`).  
  - Le score est enregistré et comparé aux scores high-score.  
- **High-score** :  
  - Les scores sont sauvegardés dans un fichier (via `HighScore.java` et `LigneHighScore.java`).  
  - Le joueur peut entrer son nom (max. 3 caractères) pour enregistrer son score.  

---

### **Technologies et structures de données**  
- **Gestion des collisions** :  
  - Le serpent est représenté par une liste d'objets `Carre` (via `Serpent.java`).  
  - Les pommes sont des objets `Carre` rouges (via `Pomme.java`).  
- **Gestion des inputs** :  
  - La classe `ClavierBorneArcade.java` mappe les touches du clavier à des actions (mouvement et boutons).  
- **Gestion du score** :  
  - Les scores sont stockés dans un fichier texte, avec un format `nom-score` (via `LigneHighScore.java`).  

---

### **Limites et particularités**  
- **Grille de jeu** :  
  - La taille de la fenêtre est de 960x700 pixels, avec des positions alignées sur des multiples de 30 pixels.  
- **Fin de partie** :  
  - Le jeu se termine si le serpent heurte un mur ou son propre corps.  
- **Défis** :  
  - Le joueur doit éviter de perdre trop rapidement (comme indiqué dans `description.txt`), ce qui ajoute une pression temporelle.  

--- 

Cette documentation est basée sur l'analyse des fichiers fournis, en se concentrant sur les mécanismes de jeu, les structures de données et les interactions utilisateur.

## Quels sont les contrôles du jeu Snake_Eater sur la borne arcade (touches/boutons) ?

**Documentation des Contrôles pour Snake_Eater sur la Borne Arcade**

### **Contrôles du Jeu**
Le jeu *Snake_Eater* utilise les éléments suivants pour le contrôle :

#### **1. Mouvement du Serpent**
- **Joystick J1** :  
  - **Haut** : `joyJ1Haut` (direction vers le haut)  
  - **Bas** : `joyJ1Bas` (direction vers le bas)  
  - **Gauche** : `joyJ1Gauche` (direction vers la gauche)  
  - **Droite** : `joyJ1Droite` (direction vers la droite)  

#### **2. Action de Quitter**
- **Bouton J1** :  
  - `boutonJ1` (ou un bouton spécifique comme `boutonJ1A`, `boutonJ1B`, etc.) :  
    - Action : Quitter le jeu (confirmer via le fichier `bouton.txt`).

#### **3. Autres Actions**
- **Boutons J1 et J2** :  
  - Les 6 boutons (A, B, C, X, Y, Z) sont définis dans la classe `ClavierBorneArcade`, mais leur utilisation spécifique au jeu *Snake_Eater* n'est pas explicitement mentionnée dans les fichiers fournis.  
  - Ils pourraient être utilisés pour des actions supplémentaires (ex : pause, accélérer, etc.), mais leur configuration dépend du contexte de l'application.

---

### **Notes Techniques**
- Les mouvements sont gérés via le clavier virtuel (joystick) et les boutons physiques de la borne.  
- Les touches/boutons associés aux actions (ex : "Quitter") sont configurés dans le fichier `bouton.txt` et la classe `ClavierBorneArcade`.  
- Les détails des mappages exacts (ex : `joyJ1Haut` → touche physique) dépendent de l'implémentation de la borne arcade.

## Comment lancer et quitter le jeu Snake_Eater (scripts, classe main, commande) ?

### Documentation : Lancement et Quitte du jeu Snake_Eater

#### 1. **Structure du projet**
Le jeu Snake_Eater est composé des classes suivantes :
- `Serpent` : Gère le serpent et son mouvement.
- `Nourriture` : Gère la génération et la logique des pommes.
- `ClavierBorneArcade` : Gère les entrées clavier (joysticks et boutons).
- `HighScore` : Gère l'enregistrement des scores.
- `LigneHighScore` : Représente une ligne du tableau des scores.
- `Pomme` : Représente une pomme dans le jeu.

#### 2. **Lancement du jeu**
Pour lancer le jeu, il faut créer une classe `main` qui initialise l'interface graphique et les composants du jeu. Voici un exemple de code :

```java
import MG2D.Fenetre;

public class MainSnake {
    public static void main(String[] args) {
        Fenetre fenetre = new Fenetre("Snake Eater", 960, 700);
        Serpent serpent = new Serpent(fenetre, new Carre(Couleur.BLANC, new Point(480, 350), 30, true));
        Nourriture nourriture = new Nourriture(fenetre);
        
        // Ajout des écouteurs de clavier
        ClavierBorneArcade clavier = new ClavierBorneArcade();
        fenetre.setKeyListener(clavier);
        
        // Démarrage du jeu
        fenetre.setVisible(true);
        // Logique de jeu (boucle principale)
    }
}
```

#### 3. **Quitter le jeu**
Pour quitter le jeu, deux méthodes sont disponibles :
- **Clavier** : Appuyez sur la touche **"Quitter"** (définie dans `ClavierBorneArcade.java`).
- **Bouton physique** : Appuyez sur le bouton "Quitter" de la borne d'arcade (défini dans `bouton.txt`).

#### 4. **Commandes clavier**
Les commandes clavier sont gérées par la classe `ClavierBorneArcade` :
- **Joueur 1** : 
  - `joyJ1Haut`, `joyJ1Bas`, `joyJ1Gauche`, `joyJ1Droite` pour le mouvement.
  - `boutonJ1A`, `boutonJ1B`, `boutonJ1C` pour les actions.
- **Joueur 2** : 
  - `joyJ2Haut`, `joyJ2Bas`, `joyJ2Gauche`, `joyJ2Droite`.
  - `boutonJ2X`, `boutonJ2Y`, `boutonJ2Z`.

#### 5. **Enregistrement des scores**
Pour enregistrer un score, utilisez la méthode `demanderEnregistrerNom` de la classe `HighScore` :
```java
HighScore.demanderEnregistrerNom(fenetre, clavier, texture, score, "highscores.txt");
```

#### 6. **Fichiers requis**
- `Fenetre.java` (MG2D) : Interface graphique.
- `ClavierBorneArcade.java` : Gestion des entrées.
- `HighScore.java` : Gestion des scores.
- `Pomme.java` et `Nourriture.java` : Génération des éléments.
- `Serpent.java` : Logique du serpent.

#### 7. **Commandes de base**
- **Lancer** : Exécuter la classe `MainSnake` (ou équivalent).
- **Quitter** : Appuyer sur "Quitter" (clavier ou bouton).
- **Manger une pomme** : Utiliser les touches de direction pour le serpent.

---

**Note** : Le code complet doit être compilé avec la bibliothèque `MG2D` pour fonctionner.

## Quelles sont les classes principales et leurs responsabilités dans Snake_Eater ?

### Documentation des Classes Principales de **Snake_Eater**

---

#### **1. `ClavierBorneArcade`**  
**Responsabilité** : Gère les entrées clavier et joysticks pour la borne d'arcade.  
- **Joysticks** : `joyJ1`, `joyJ2` (ex: `joyJ1Haut`, `joyJ1Bas`, etc.).  
- **Boutons** : `boutonJ1`, `boutonJ2` (ex: `boutonJ1A`, `boutonJ1X`, etc.).  
- **Fonctionnalité** : Convertit les pressions de touches en actions (déplacement, pause, etc.) pour le jeu.  

---

#### **2. `HighScore`**  
**Responsabilité** : Gère la gestion des scores et leur sauvegarde.  
- **Fonctionnalité** :  
  - Lit et écrit les scores depuis un fichier (`fichierHighScore`).  
  - Permet à l'utilisateur d'entrer un nom pour un nouveau score.  
  - Utilise la classe `LigneHighScore` pour stocker chaque entrée (nom + score).  

---

#### **3. `LigneHighScore`**  
**Responsabilité** : Représente une entrée de score (nom + score).  
- **Attributs** :  
  - `nom` (max 3 caractères).  
  - `score` (entier).  
- **Méthodes** :  
  - `getNom()`, `getScore()` : Accesseurs.  
  - `toString()` : Formatage de l'entrée (ex: `"AAA-100"`).  

---

#### **4. `Nourriture`**  
**Responsabilité** : Gère la logique des pommes (nourriture) du jeu.  
- **Fonctionnalité** :  
  - Crée des pommes aléatoires sur la fenêtre (`Fenetre`).  
  - Gère la position et l'apparition des pommes.  
  - Intégre les pommes dans la scène via `Fenetre.ajouter()`.  

---

#### **5. `Pomme`**  
**Responsabilité** : Représente une pomme graphique.  
- **Attributs** :  
  - `Carre c` : Le carré (rectangle) de la pomme.  
  - `boolean etat` : État de la pomme (ex: "mangée" ou non).  
- **Méthodes** :  
  - `getC()` : Récupère le carré graphique.  
  - `setEtat(boolean)` : Met à jour l'état de la pomme.  

---

#### **6. `Serpent`**  
**Responsabilité** : Gère le serpent (joueur) et son comportement.  
- **Fonctionnalité** :  
  - Gère le déplacement, la croissance et les collisions.  
  - Utilise des `Carre` pour représenter chaque segment du serpent.  
  - Gère la direction (ex: `direction = 1` pour droite).  
  - Intègre le serpent dans la scène via `Fenetre.ajouter()`.  

---

### **Classes Annexes**  
- **`Fenetre`** (importé) : Gère la fenêtre graphique et l'affichage des éléments (pommes, serpent).  
- **`Carre`** (importé) : Représente un carré (rectangle) pour les graphismes.  
- **`Point`** (importé) : Représente des coordonnées (x, y).  
- **`Couleur`** (importé) : Définit les couleurs utilisées (ex: `Couleur.ROUGE`, `Couleur.BLANC`).  

---

### **Fichiers Non Classes**  
- **`bouton.txt`** : Fichier de configuration des boutons (non utilisé dans le code fourni).  
- **`description.txt`** : Description du jeu (non lié à la logique).  

--- 

Cette documentation structure les responsabilités des classes principales, en se basant sur les fichiers fournis.


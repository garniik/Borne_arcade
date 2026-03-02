# Puissance_X

## Décris le jeu Puissance_X (objectif, principe, gameplay) en te basant sur le code.

### Puissance_X : Jeu d'Arcade

#### Objectif
Le jeu Puissance_X est un jeu d'arcade où le but est de remplir une grille de jeu avec des jetons de manière à former une ligne de 4 jetons de la même couleur horizontalement, verticalement ou diagonalement. Le joueur qui parvient à former cette ligne avant l'adversaire gagne la partie.

#### Principe
Le jeu se déroule sur une grille de jeu de taille variable (définie par l'utilisateur). Les joueurs prennent tour à tour pour placer leurs jetons sur la grille. Le joueur qui parvient à aligner 4 jetons de la même couleur gagne la partie.

#### Gameplay
1. **Menu de Nouvelle Partie** : Le joueur peut définir la taille de la grille (nombre de lignes et de colonnes) et le nombre de joueurs. Le jeu commence alors avec ces paramètres.

2. **Menu de Choix des Joueurs** : Le joueur peut choisir le type de joueur pour chaque position sur la grille. Les types de joueurs disponibles sont :
   - Aucun : Position vide
   - Joueur normal : Humain jouant manuellement
   - IA - Débutante, Normale, Avancée, Experte : Intelligences artificielles de difficulté croissante

3. **Menu de Fin de Partie** : Si une partie est terminée, le joueur peut choisir de rejouer ou de quitter le jeu.

4. **Menu de Paramètres** : Le joueur peut ajuster les paramètres du jeu tels que la définition (HD ou Basse définition) et la fréquence des images par seconde.

#### Structure du Jeu
- **MenuNouvellePartie.java** : Permet de définir la taille de la grille et le nombre de joueurs.
- **MenuChoixJoueurs.java** : Permet de choisir le type de joueur pour chaque position sur la grille.
- **MenuFinPartie.java** : Affiche le résultat de la partie et permet au joueur de rejouer ou de quitter.
- **MenuParametres.java** : Permet de modifier les paramètres du jeu tels que la définition et la fréquence des images.

#### Conclusion
Puissance_X est un jeu d'arcade simple mais stratégique, où le joueur doit planifier ses coups pour aligner 4 jetons de la même couleur avant l'adversaire. Le jeu offre une variété de modes de jeu, y compris des intelligences artificielles de différentes difficultés, ce qui ajoute une dimension de challenge et de stratégie.

## Quels sont les contrôles du jeu Puissance_X sur la borne arcade (touches/boutons) ?

### Contrôles du jeu Puissance_X sur la borne arcade

#### Menu de Configuration des Joueurs
- **Touches** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les types de joueurs. Appuyer sur une touche pour sélectionner un type de joueur.
- **Boutons** : Utiliser le bouton de sélection pour confirmer la sélection d'un type de joueur.

#### Menu de Choix des Joueurs
- **Touches** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les options de menu. Appuyer sur une touche pour sélectionner une option.
- **Boutons** : Utiliser le bouton de sélection pour confirmer la sélection d'une option.

#### Menu de Fin de Partie
- **Touches** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les options de menu. Appuyer sur une touche pour sélectionner une option.
- **Boutons** : Utiliser le bouton de sélection pour confirmer la sélection d'une option.

#### Menu de Nouvelle Partie
- **Touches** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les options de menu. Appuyer sur une touche pour sélectionner une option.
- **Boutons** : Utiliser le bouton de sélection pour confirmer la sélection d'une option.

#### Menu de Paramètres
- **Touches** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les options de menu. Appuyer sur une touche pour sélectionner une option.
- **Boutons** : Utiliser le bouton de sélection pour confirmer la sélection d'une option.

### Résumé
- **Navigation** : Utiliser les touches de direction (flèches gauche/droite) pour naviguer entre les options.
- **Sélection** : Utiliser le bouton de sélection pour confirmer la sélection d'une option.

Cette documentation fournit les contrôles clés pour interagir avec les menus du jeu Puissance_X sur la borne arcade.

## Comment lancer et quitter le jeu Puissance_X (scripts, classe main, commande) ?

Pour lancer et quitter le jeu Puissance_X, voici les étapes à suivre basées sur les fichiers fournis :

### Lancer le jeu Puissance_X

1. **Exécuter le script principal** :
   - Le script principal est `Main.java`. Pour exécuter le jeu, vous devez compiler et exécuter ce fichier Java.
   - Utilisez la commande suivante pour compiler et exécuter le programme :
   ```bash
   javac Main.java
   java Main
   ```

2. **Exécuter le jeu** :
   - Une fois le programme exécuté, le jeu Puissance_X devrait s'ouvrir automatiquement. Vous pouvez interagir avec le jeu en utilisant les touches du clavier pour naviguer et sélectionner les options.

### Quitter le jeu Puissance_X

1. **Utiliser la touche de quitture** :
   - Le jeu Puissance_X dispose d'une touche de quitture. Vous pouvez quitter le jeu en appuyant sur la touche `Q` ou `Esc` (Escape) sur le clavier.

2. **Exécuter le script principal pour quitter** :
   - Si vous souhaitez quitter le jeu via le script principal, vous pouvez appeler la méthode `quitter()` dans le menu correspondant.
   - Par exemple, dans le menu `MenuFinPartie`, vous pouvez appeler la méthode `quitter()` pour quitter le jeu.

### Documentation détaillée

#### Classe `Main.java`
- **Rôle** : Gère l'interface utilisateur et le cycle de vie du jeu.
- **Méthode principale** : `main(String[] args)`
  - **Description** : Cette méthode est appelée lorsque le programme est exécuté.
  - **Actions** :
    - Crée une instance de `GestionAffichage` avec le titre du jeu.
    - Appelle la méthode `nouvellePartie()` pour commencer une nouvelle partie.
    - Gère l'interface utilisateur en rafraîchissant l'affichage et en gérant les événements clavier.

#### Classe `Menu.java`
- **Rôle** : Gère les menus de l'application.
- **Méthode `ajouter(ElementMenu element)`** :
  - **Description** : Ajoute un élément au menu.
  - **Actions** : Ajoute l'élément spécifié à la liste des éléments du menu.

#### Classe `MenuChoixJoueurs.java`
- **Rôle** : Gère le menu de choix des joueurs.
- **Méthode `ajouter(new TexteItem("Choix des joueurs", "Monospaced", 100))`** :
  - **Description** : Ajoute un texte au menu.
  - **Actions** : Ajoute un texte spécifique au menu pour indiquer le choix des joueurs.

#### Classe `MenuFinPartie.java`
- **Rôle** : Gère le menu de fin de partie.
- **Méthode `ajouter(new TexteItem("Partie Terminée !", "Monospaced", 100))`** :
  - **Description** : Ajoute un texte au menu.
  - **Actions** : Ajoute un texte spécifique au menu pour indiquer la fin de la partie.

#### Classe `MenuNouvellePartie.java`
- **Rôle** : Gère le menu de nouvelle partie.
- **Méthode `ajouter(nbLignes_item = new ChoixValeurItem("Nombre de lignes", 1, 10, 5, "Monospaced", 70))`** :
  - **Description** : Ajoute un choix de valeur au menu.
  - **Actions** : Ajoute un choix de valeur pour le nombre de lignes dans la partie.

#### Classe `MenuParametres.java`
- **Rôle** : Gère les paramètres du jeu.
- **Méthode `ajouter(this.hd_bouton = new BoutonItem("Basse définition", "Monospaced", 70) {`** :
  - **Description** : Ajoute un bouton au menu.
  - **Actions** : Ajoute un bouton pour basculer entre les modes haute et basse définition.

### Conclusion
Pour lancer et quitter le jeu Puissance_X, vous devez compiler et exécuter le fichier `Main.java`. Vous pouvez quitter le jeu en appuyant sur la touche `Q` ou `Esc` sur le clavier. Les menus permettent de naviguer et de sélectionner les options du jeu, et les méthodes spécifiques comme `nouvellePartie()` et `quitter()` gèrent les actions correspondantes.

## Quelles sont les classes principales et leurs responsabilités dans Puissance_X ?

### Classes Principales et Responsabilités dans Puissance_X

#### 1. **Menu**
- **Responsabilités** : Gère l'affichage et l'interaction avec les éléments de menu.
- **Responsabilités spécifiques** :
  - **Menu** : Gère la structure de base des menus et permet d'ajouter des éléments.
  - **MenuChoixJoueurs** : Gère le menu pour choisir les joueurs.
  - **MenuFinPartie** : Gère le menu après la fin d'une partie.
  - **MenuNouvellePartie** : Gère le menu pour commencer une nouvelle partie.
  - **MenuParametres** : Gère le menu des paramètres.

#### 2. **ElementMenu**
- **Responsabilités** : Représente un élément de menu avec des méthodes pour mettre à jour et afficher l'élément.
- **Responsabilités spécifiques** :
  - **ElementMenu** : Classe abstraite définissant les méthodes à implémenter pour mettre à jour et afficher l'élément.
  - **TexteItem** : Implémente l'ElementMenu pour afficher du texte.
  - **BoutonItem** : Implémente l'ElementMenu pour afficher un bouton avec une action à exécuter.

#### 3. **ConfigurationJoueurMenu**
- **Responsabilités** : Gère la configuration des joueurs dans le menu de configuration.
- **Responsabilités spécifiques** :
  - **ConfigurationJoueurMenu** : Classe dérivée de MenuChoixJoueurs, gérant spécifiquement la configuration des joueurs.
  - **TexteItem** : Implémente l'ElementMenu pour afficher le nom du joueur et le type de joueur sélectionné.

#### 4. **MenuChoixJoueurs**
- **Responsabilités** : Gère le menu pour choisir les joueurs.
- **Responsabilités spécifiques** :
  - **MenuChoixJoueurs** : Classe dérivée de Ecran, gérant le menu de choix des joueurs avec des instructions et des boutons pour ajouter des joueurs.

#### 5. **MenuFinPartie**
- **Responsabilités** : Gère le menu après la fin d'une partie.
- **Responsabilités spécifiques** :
  - **MenuFinPartie** : Classe dérivée de Ecran, gérant le menu avec des options pour rejouer ou quitter.

#### 6. **MenuNouvellePartie**
- **Responsabilités** : Gère le menu pour commencer une nouvelle partie.
- **Responsabilités spécifiques** :
  - **MenuNouvellePartie** : Classe dérivée de Ecran, gérant le menu avec des options pour configurer les dimensions de la grille et continuer.

#### 7. **MenuParametres**
- **Responsabilités** : Gère le menu des paramètres.
- **Responsabilités spécifiques** :
  - **MenuParametres** : Classe dérivée de Ecran, gérant le menu avec des options pour basculer entre haute et basse définition, ajuster le FPS et la vitesse de chute.

#### 8. **Ecran**
- **Responsabilités** : Gère l'affichage de l'écran principal.
- **Responsabilités spécifiques** :
  - **Ecran** : Classe abstraite définissant les méthodes pour initialiser et afficher l'écran.

### Conclusion
Les classes principales dans Puissance_X sont **Menu**, **ElementMenu**, **ConfigurationJoueurMenu**, **MenuChoixJoueurs**, **MenuFinPartie**, **MenuNouvellePartie**, **MenuParametres**, et **Ecran**. Chaque classe a des responsabilités spécifiques liées à la gestion des menus et des interactions utilisateur. Les classes dérivées comme **MenuChoixJoueurs**, **MenuFinPartie**, **MenuNouvellePartie**, et **MenuParametres** ont des responsabilités plus spécifiques liées à la gestion des différents états de l'application.


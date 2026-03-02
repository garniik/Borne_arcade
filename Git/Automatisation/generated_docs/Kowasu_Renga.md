# Kowasu_Renga

## Décris le jeu Kowasu_Renga (objectif, principe, gameplay) en te basant sur le code.

### Documentation du jeu Kowasu_Renga

#### **Titre :** Kowasu_Renga

#### **Équipe :** MG2D - 2013

#### **Description :**
Kowasu_Renga est un jeu de casse-briques classique faisant partie des démos de la bibliothèque MG2D. Le jeu se déroule dans un environnement de jeu 2D où le joueur doit frapper des briques avec une balle pour les faire exploser.

#### **Objectif :**
Le but du jeu est de détruire toutes les briques du jeu avant que le joueur ne soit touché par la balle. Le score est basé sur le nombre de briques détruites et le temps mis à les détruire.

#### **Principe :**
Le jeu se joue avec une barre de mouvement horizontale qui permet de déplacer la balle à gauche et à droite. La balle est lancée vers le haut et rebondit sur les briques. Le joueur doit ajuster la position de la barre pour frapper les briques et les faire exploser. Si la balle atteint le bas de l'écran, le jeu se termine.

#### **Gameplay :**
- **Barre de mouvement :** La barre de mouvement est située au bas de l'écran et permet de déplacer la balle horizontalement à gauche et à droite.
- **Balle :** La balle est lancée vers le haut et rebondit sur les briques. Le joueur doit ajuster la position de la barre pour frapper les briques et les faire exploser.
- **Briques :** Les briques sont disposées en lignes horizontales. Chaque brique est représentée par une texture et est détruite lorsque la balle la frappe.
- **Score :** Le score est affiché en haut à droite de l'écran et augmente avec chaque brique détruite. Le temps mis à détruire toutes les briques est également comptabilisé.
- **Vitesse :** La vitesse de la balle peut être ajustée via un attribut du jeu. Le joueur peut également ajuster la vitesse de la balle en modifiant le code.

#### **Attributs et Variables :**
- **largeur et hauteur :** Définissent les dimensions de la fenêtre de jeu (1280x1024).
- **vitesseBase :** Définit la vitesse de base de la balle (2).
- **FenetrePleinEcran f :** La fenêtre du jeu est définie comme une fenêtre pleine écran avec le titre "Kowasu Renga".

#### **Instructions de jeu :**
1. Déplacez la barre de mouvement horizontalement pour déplacer la balle.
2. Frappez les briques avec la balle pour les détruire.
3. Continuez à frapper les briques jusqu'à ce que toutes soient détruites.
4. Si la balle atteint le bas de l'écran, le jeu se termine.

#### **Fichiers liés :**
- **bouton.txt :** Contient les mouvements de la barre de mouvement.
- **description.txt :** Contient les informations sur le jeu et son équipe.
- **Kowasu_Renga.java :** Le code source du jeu, implémentant les fonctionnalités de base du jeu.

#### **Conclusion :**
Kowasu_Renga est un jeu de casse-briques classique qui offre une expérience de jeu simple et amusante. Le jeu est conçu pour être joué sur un écran de jeu 2D et nécessite une coordination et une précision pour détruire les briques.

## Quels sont les contrôles du jeu Kowasu_Renga sur la borne arcade (touches/boutons) ?

### Documentation des contrôles du jeu Kowasu_Renga sur la borne arcade

#### Contrôles du jeu Kowasu_Renga

Le jeu Kowasu_Renga est contrôlé par les boutons de la borne d'arcade. Voici les actions associées à chaque bouton :

- **Mouvement barre**: Aucun mouvement spécifique n'est associé à ce bouton.
- **Quitter**: Quitte le jeu.
- **Lancer la balle**: Lance la balle dans le jeu.

Les autres boutons ne sont pas spécifiquement mentionnés dans le fichier `bouton.txt`, ce qui suggère qu'ils ne sont pas utilisés pour contrôler le jeu.

## Comment lancer et quitter le jeu Kowasu_Renga (scripts, classe main, commande) ?

### Documentation pour lancer et quitter le jeu Kowasu_Renga

#### 1. **Lancer le jeu Kowasu_Renga**

Pour lancer le jeu Kowasu_Renga, vous devez exécuter le fichier Java `Kowasu_Renga.java`. Voici les étapes à suivre :

1. **Compilation du code Java** :
   - Assurez-vous que vous avez Java installé sur votre système.
   - Ouvrez une fenêtre de terminal ou de commande.
   - Naviguez vers le répertoire contenant le fichier `Kowasu_Renga.java`.
   - Exécutez la commande suivante pour compiler le fichier Java :
     ```sh
     javac Kowasu_Renga.java
     ```
   - Si la compilation est réussie, vous devriez voir un fichier `Kowasu_Renga.class` créé.

2. **Exécution du programme Java** :
   - Exécutez le fichier compilé avec la commande suivante :
     ```sh
     java Kowasu_Renga
     ```
   - Le jeu devrait alors s'ouvrir dans une fenêtre de jeu.

#### 2. **Quitter le jeu Kowasu_Renga**

Pour quitter le jeu Kowasu_Renga, vous pouvez :

1. **Utiliser le bouton de quittage** :
   - Le fichier `bouton.txt` indique que le bouton de quittage est associé à la commande `Quitter`.
   - Appuyez sur le bouton de quittage pour fermer le jeu.

2. **Utiliser la commande de quittage** :
   - Si vous avez ouvert le jeu à partir d'une fenêtre de commande, vous pouvez taper la commande suivante pour quitter :
     ```sh
     exit
     ```
   - Si vous avez ouvert le jeu à partir d'un menu ou d'une interface utilisateur, recherchez l'option de quittage et cliquez dessus.

3. **Fermer la fenêtre** :
   - Si vous avez ouvert le jeu à partir d'une fenêtre de jeu, vous pouvez fermer la fenêtre en cliquant sur le bouton de fermeture (croix en haut à droite de la fenêtre).

#### 3. **Documentation des commandes de quittage**

- **Bouton de quittage** : Le bouton de quittage est associé à la commande `Quitter` dans le fichier `bouton.txt`.
- **Commande de quittage** : Vous pouvez quitter le jeu en tapant `exit` dans une fenêtre de commande ou en cliquant sur le bouton de fermeture de la fenêtre de jeu.

### Conclusion

Pour lancer et quitter le jeu Kowasu_Renga, vous devez compiler et exécuter le fichier Java `Kowasu_Renga.java`. Vous pouvez quitter le jeu en utilisant le bouton de quittage, en tapant `exit` dans une fenêtre de commande, ou en fermant la fenêtre de jeu.

## Quelles sont les classes principales et leurs responsabilités dans Kowasu_Renga ?

### Documentation des classes principales dans Kowasu_Renga

#### 1. **FenetrePleinEcran**
- **Responsabilités :**
  - Gestion de la fenêtre de jeu en plein écran.
  - Configuration de la taille de la fenêtre (largeur et hauteur).
  - Affichage de la barre de titre et du texte de titre du jeu.
  
- **Extrait du code :**
  ```java
  static FenetrePleinEcran f = new FenetrePleinEcran ("Kowasu Renga");
  ```

#### 2. **Fenetre**
- **Responsabilités :**
  - Gestion de la fenêtre principale du jeu.
  - Configuration de la taille de la fenêtre (largeur et hauteur).
  - Affichage de la barre de titre et du texte de titre du jeu.
  
- **Extrait du code :**
  ```java
  //static Fenetre f = new Fenetre ("Kowasu Renga",largeur,hauteur);
  ```

#### 3. **MG2D**
- **Responsabilités :**
  - Bibliothèque graphique utilisée pour le développement du jeu.
  - Gestion des objets graphiques (Cercle, Rectangle, Texture, Texte).
  - Gestion des couleurs et des polices de caractères.
  
- **Extrait du code :**
  ```java
  import MG2D.*;
  import MG2D.geometrie.Cercle;
  import MG2D.geometrie.Point;
  import MG2D.geometrie.Rectangle;
  import MG2D.geometrie.Texture;
  import MG2D.geometrie.Texte;
  import MG2D.Couleur;
  import MG2D.Font;
  import MG2D.GraphicsDevice;
  import MG2D.GraphicsEnvironment;
  ```

### Résumé
- **FenetrePleinEcran** et **Fenetre** sont des classes qui gèrent la fenêtre de jeu, y compris la taille et l'affichage des titres.
- **MG2D** est une bibliothèque graphique qui fournit les outils nécessaires pour créer des objets graphiques, des couleurs, et des polices de caractères.

Ces classes sont essentielles pour la création et la gestion de l'interface utilisateur du jeu "Kowasu Renga".


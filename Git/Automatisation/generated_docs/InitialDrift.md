# InitialDrift

## Décris le jeu InitialDrift (objectif, principe, gameplay) en te basant sur le code.

### Documentation du jeu InitialDrift

#### **Titre :** InitialDrift

#### **Objectif :**
Le jeu InitialDrift est un jeu de course en arcade où le joueur doit rouler le plus loin possible en évitant les voitures arrivant en sens inverse, les chars et les barils de pétrole. Le tout se déroule sur une musique entêtante.

#### **Principe :**
Le jeu se déroule dans une fenêtre de jeu pleine écran. Le joueur contrôle un véhicule qui doit avancer en évitant les obstacles et les ennemis. Le jeu se déroule en boucle, avec une progression du temps et des événements aléatoires.

#### **Gameplay :**

1. **Contrôle :**
   - Le joueur contrôle le véhicule avec les touches de direction standard (flèches gauche et droite pour déplacer le véhicule, touche espace pour accélérer).

2. **Avancement du temps :**
   - Le jeu avance en temps réel, avec une progression du temps indiquée par le compteur `i42` dans le fichier `Main.java`.

3. **Génération d'ennemis et de décor :**
   - À chaque itération du temps (quand `i42` atteint 15), le jeu génère de nouveaux ennemis et de nouveaux éléments de décor (comme les barils de pétrole) pour maintenir l'intérêt et la difficulté du jeu.

4. **Événements aléatoires :**
   - Le jeu génère des événements aléatoires pour ajouter de la variété et du challenge, comme la génération de nouveaux ennemis ou de nouveaux obstacles.

5. **Gestion des ennemis :**
   - Les ennemis sont définis dans la classe `Ennemi.java`. Ils ont des textures personnalisées et peuvent avoir des vitesses variables. Le joueur doit éviter ces ennemis pour progresser.

6. **Gestion des décorations :**
   - Les décorations sont gérées dans la classe `Jeu.java`. Elles peuvent inclure des barils de pétrole et d'autres obstacles qui doivent être évités pour continuer à avancer.

7. **Fin du jeu :**
   - Le jeu se termine lorsque le joueur sort de la zone de jeu ou que le temps est épuisé. Le joueur peut alors recommencer pour essayer de progresser plus loin.

#### **Techniques utilisées :**
- **Framework MG2D :** Le jeu utilise le framework MG2D pour gérer les graphismes, la géométrie et l'audio.
- **ArrayList :** L'utilisation de `ArrayList` permet de gérer dynamiquement les ennemis et les décorations.
- **Fenêtre pleine écran :** Le jeu s'affiche dans une fenêtre pleine écran pour offrir une meilleure expérience de jeu.

#### **Attributs clés :**
- **Joueur :** Le joueur est représenté par une texture personnalisée (image du stickman).
- **Ennemi :** Les ennemis sont définis par une texture et une vitesse.
- **Décor :** Les décorations sont également définies par des textures et peuvent inclure des barils de pétrole.

#### **Conclusion :**
InitialDrift est un jeu de course en arcade qui combine des éléments de course et d'éviter les obstacles. Le jeu est structuré pour offrir une progression constante et des défis variés grâce à la génération aléatoire d'ennemis et de décorations. Le jeu est conçu pour être joué sur une fenêtre pleine écran, offrant une expérience immersive et dynamique.

## Quels sont les contrôles du jeu InitialDrift sur la borne arcade (touches/boutons) ?

### Contrôles du Jeu InitialDrift sur la borne arcade

#### Touches/Boutons de Contrôle

- **Mouvement de la Voiture** : Aucun contrôle spécifique n'est mentionné dans le fichier `bouton.txt`. Cependant, en se basant sur le nom du fichier, on peut supposer que les mouvements de la voiture sont gérés par des boutons ou des touches non spécifiées dans le fichier.

- **Quitter le Jeu** : Le bouton de quitter est défini comme "Quitter" dans le fichier `bouton.txt`. Cela suggère que le joueur peut quitter le jeu en appuyant sur ce bouton.

#### Conclusion

- **Mouvement de la Voiture** : Les détails spécifiques sur les touches ou boutons de mouvement de la voiture ne sont pas fournis dans les fichiers fournis. Il faudrait consulter le code source pour déterminer les contrôles exacts.

- **Quitter le Jeu** : Le joueur peut quitter le jeu en appuyant sur le bouton "Quitter".

Pour une documentation plus détaillée, il faudrait accéder au code source complet et aux spécifications du jeu pour déterminer les contrôles exacts.

## Comment lancer et quitter le jeu InitialDrift (scripts, classe main, commande) ?

Pour lancer et quitter le jeu InitialDrift, vous devez vous baser sur le fichier `Main.java`, qui contient la classe principale du jeu. Voici les étapes à suivre :

### Lancer le jeu
1. **Exécuter le programme** :
   Pour exécuter le programme, vous pouvez utiliser un compilateur Java. Assurez-vous que vous avez Java installé sur votre système. Vous pouvez compiler et exécuter le programme en utilisant la commande suivante dans un terminal ou une fenêtre de commande :

   ```sh
   javac Main.java
   java Main
   ```

   Cette commande compile le fichier `Main.java` et exécute le programme.

### Quitter le jeu
1. **Arrêter le programme** :
   Le programme est conçu pour exécuter en boucle indéfinie. Pour le quitter, vous pouvez interrompre l'exécution du programme en utilisant les commandes suivantes dans le terminal ou la fenêtre de commande :

   ```sh
   Ctrl + C
   ```

   Cette commande interrompt l'exécution du programme.

### Documentation claire et structurée

#### Classe `Main.java`
- **Attributs** :
  - `i42` : Un compteur utilisé pour contrôler la fréquence de génération de décor et d'ennemis.
  - `j` : Une instance de la classe `Jeu` qui gère le jeu.

- **Méthode `main`** :
  - La méthode `main` est la méthode d'entrée principale du programme.
  - Elle contient une boucle `while(true)` qui exécute indéfiniment le jeu.
  - À chaque itération de la boucle, le jeu avance d'un pas de temps, affiche l'état actuel de la fenêtre, et génère de nouveaux éléments (décor et ennemis) à intervalles réguliers.

#### Commentaires dans le code
- Le code est commenté pour expliquer les différentes parties du programme. Par exemple, les commentaires expliquent le but de chaque variable et la logique de la boucle principale.

#### Conclusion
Pour lancer le jeu, compilez et exécutez le fichier `Main.java`. Pour le quitter, interrompez l'exécution du programme en utilisant `Ctrl + C`. Le programme est conçu pour exécuter en boucle indéfinie, donc vous devrez interrompre l'exécution manuellement pour le quitter.

## Quelles sont les classes principales et leurs responsabilités dans InitialDrift ?

### Documentation des Classes Principales dans le Projet InitialDrift

#### 1. **Main.java**
- **Responsabilités :**
  - Gestion de l'application principale.
  - Création et initialisation de l'objet `Jeu`.
  - Boucle principale de l'application qui avance le temps et rafraîchit la fenêtre.
  - Génération de décor et d'ennemis à intervalles réguliers.
  - Gestion de l'arrêt de l'application.

#### 2. **Jeu.java**
- **Responsabilités :**
  - Gestion de l'interface utilisateur.
  - Gestion des objets de jeu (joueur, ennemis, décor).
  - Gestion de la fenêtre de jeu.
  - Gestion des animations et des effets sonores.
  - Gestion des collisions et des interactions entre les objets de jeu.

#### 3. **Joueur.java**
- **Responsabilités :**
  - Gestion de l'objet joueur.
  - Gestion des attributs du joueur (position, taille, texture).
  - Gestion des méthodes de déplacement et de gestion des collisions.

#### 4. **Ennemi.java**
- **Responsabilités :**
  - Gestion de l'objet ennemi.
  - Gestion des attributs de l'ennemi (texture, vitesse).
  - Gestion des méthodes de déplacement et de gestion des collisions.
  - Gestion des interactions avec le joueur.

#### 5. **Fichier 2 (bouton.txt)**
- **Responsabilités :**
  - Contient des informations sur les boutons de mouvement du joueur.
  - Utilisé pour la gestion des commandes de mouvement du joueur.

#### 6. **Fichier 3 (description.txt)**
- **Responsabilités :**
  - Contient une description du jeu.
  - Utilisé pour fournir des informations sur le jeu à l'utilisateur.

### Conclusion
Les classes principales dans le projet InitialDrift sont `Main`, `Jeu`, `Joueur`, et `Ennemi`. Chaque classe a des responsabilités spécifiques qui contribuent à la gestion de l'application, à la gestion des objets de jeu, et à la gestion de l'interface utilisateur. Les autres fichiers (bouton.txt et description.txt) fournissent des informations supplémentaires sur le jeu et les commandes de mouvement.


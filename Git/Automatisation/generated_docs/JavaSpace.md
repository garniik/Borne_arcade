# JavaSpace

## Décris le jeu JavaSpace (objectif, principe, gameplay) en te basant sur le code.

### Description du Jeu JavaSpace

#### Objectif
Le jeu JavaSpace est un Shoot 'em Up où le joueur contrôle un vaisseau spatial dans un environnement spatial. Le but du jeu est de détruire des ennemis et des boss pour gagner des vies et progresser dans le jeu.

#### Principe
Le jeu est basé sur un système de phases. Il commence par une phase de tir (PHASESHOOT) où le joueur doit détruire des ennemis pour gagner des vies. Une fois que le joueur a gagné suffisamment de vies, il passe à la phase de boss (PHASEBOSS) où il doit affronter un boss spécifique.

#### Gameplay
1. **Phase de Tir (PHASESHOOT)**
   - Le joueur contrôle un vaisseau spatial et doit tirer sur des ennemis qui apparaissent sur l'écran.
   - Les ennemis ont des vitesses et des trajectoires variables.
   - Le joueur gagne des vies en détruisant les ennemis.
   - Le jeu se termine lorsque le joueur n'a plus de vies.

2. **Phase de Boss (PHASEBOSS)**
   - Une fois que le joueur a gagné suffisamment de vies, il entre dans la phase de boss.
   - Le boss apparaît et déplace son vaisseau selon une trajectoire définie.
   - Le joueur doit détruire le boss pour gagner une vie supplémentaire.
   - Le boss a une vie maximale définie (VIEBOSS).

#### Mécanismes clés
- **Clavier et Joysticks** : Le joueur contrôle le vaisseau avec le clavier ou les joysticks. Les touches de déplacement et de tir sont spécifiées dans le fichier `bouton.txt`.
- **Textures et Images** : Les ennemis et le boss sont représentés par des textures chargées à partir de fichiers d'images.
- **Vie et Points** : Le joueur gagne des vies en détruisant les ennemis et le boss. Le nombre de vies est limité et réinitialisé à chaque passage à la phase de tir.
- **Phase de Début** : Le jeu commence avec une phase de menu où le joueur peut choisir de commencer une nouvelle partie ou de quitter le jeu.

#### Structure du Jeu
- **Menu** : Le jeu commence avec un menu où le joueur peut choisir de commencer une nouvelle partie.
- **Phase de Tir** : Le joueur tire sur des ennemis pour gagner des vies.
- **Phase de Boss** : Le joueur doit détruire le boss pour gagner une vie supplémentaire.

#### Conclusion
JavaSpace est un Shoot 'em Up où le joueur doit détruire des ennemis et un boss pour gagner des vies et progresser dans le jeu. Le jeu est structuré en phases de tir et de boss, avec des mécanismes de vie et de déplacement complexes. Le joueur contrôle le vaisseau avec le clavier ou les joysticks, et le jeu utilise des textures pour représenter les ennemis et le boss.

## Quels sont les contrôles du jeu JavaSpace sur la borne arcade (touches/boutons) ?

### Contrôles du Jeu JavaSpace sur la Borne Arcade

#### Clavier et Joysticks

La gestion des contrôles du jeu JavaSpace est réalisée à travers les événements de clavier et de joysticks. Voici les contrôles disponibles :

1. **Clavier** :
   - **Mouvement des vaisseaux** : Les mouvements des vaisseaux sont gérés par les touches de direction du clavier.
   - **Tirer** : Le tir est effectué en appuyant sur la touche de tir du clavier.

2. **Joysticks** :
   - **Mouvement des vaisseaux** : Les mouvements des vaisseaux sont également gérés par les joysticks, avec les directions de mouvement spécifiées dans le fichier `bouton.txt`.
   - **Tirer** : Le tir est effectué en appuyant sur le bouton de tir du joystick.

#### Fichier `bouton.txt`

Le fichier `bouton.txt` définit les actions associées aux boutons du clavier et des joysticks. Voici les actions spécifiées :

```txt
Mouvement vaisseaux:aucun:aucun:aucun:Tirer:aucun:aucun
```

- **Mouvement vaisseaux** : Aucun mouvement est spécifié pour les vaisseaux.
- **Tirer** : Le tir est effectué en appuyant sur la touche de tir du clavier.

#### Gestion des événements

La gestion des événements clavier et joystick est réalisée par la classe `ClavierBorneArcade.java`, qui implémente la méthode `KeyListener` pour gérer les événements de clavier. Les actions de mouvement et de tir sont gérées en fonction des touches et des boutons pressés.

#### Conclusion

Les contrôles du jeu JavaSpace sont principalement gérés par les touches de direction et de tir du clavier, ainsi que par les boutons de direction et de tir des joysticks. Les mouvements des vaisseaux ne sont pas spécifiquement gérés par les joysticks, mais les actions de tir sont effectuées de la même manière pour les deux types de contrôles.

## Comment lancer et quitter le jeu JavaSpace (scripts, classe main, commande) ?

### Documentation pour lancer et quitter le jeu JavaSpace

#### **1. Lancer le jeu JavaSpace**

Pour lancer le jeu JavaSpace, vous devez exécuter le fichier `Main.java`. Voici les étapes à suivre :

1. **Compilation du code Java** :
   ```bash
   javac Main.java
   ```
   Cette commande compile le fichier `Main.java` en un fichier `.class` qui peut être exécuté.

2. **Exécution du programme** :
   ```bash
   java Main
   ```
   Cette commande exécute le programme JavaSpace.

#### **2. Quitter le jeu JavaSpace**

Pour quitter le jeu JavaSpace, vous pouvez utiliser les commandes suivantes :

1. **Utiliser la touche `ESC`** :
   - Appuyez sur la touche `ESC` sur le clavier pour quitter le jeu.

2. **Utiliser la commande `System.exit(0)`** :
   - Si vous souhaitez quitter le jeu de manière programmée, vous pouvez utiliser la méthode `System.exit(0)` dans le code Java. Par exemple, vous pouvez ajouter cette ligne de code dans le bloc `while` de `Main.java` pour quitter le jeu lorsque le joueur souhaite quitter.

   ```java
   while(finJeu != 1) {
       // ... (code existant)
       if (finJeu == 1) {
           System.exit(0); // Quitter le jeu
       }
       // ... (code existant)
   }
   ```

#### **3. Documentation des classes et méthodes clés**

- **Classe `Main.java`** :
  - **Méthode `main`** : Cette méthode est le point d'entrée du programme Java. Elle instancie une nouvelle instance de la classe `Jeu` et démarre le jeu.
  - **Variable `finJeu`** : Cette variable est utilisée pour déterminer si le jeu doit être quitté. Elle est initialisée à `0` et est mise à `1` lorsque le joueur souhaite quitter le jeu.

- **Classe `Jeu.java`** :
  - **Constantes** : Les constantes `PHASESHOOT`, `PHASEBOSS`, `VIEBOSS`, et `TEMPSPHASE` définissent les phases du jeu et les paramètres de vie du boss.
  - **Méthode `majMenu`** : Cette méthode est utilisée pour actualiser le menu du jeu.
  - **Méthode `getStatus`** : Cette méthode est utilisée pour obtenir le statut du jeu (par exemple, si le joueur a gagné ou perdu).

#### **4. Conclusion**

Pour lancer et quitter le jeu JavaSpace, vous devez compiler et exécuter le fichier `Main.java`. Vous pouvez quitter le jeu en appuyant sur la touche `ESC` ou en utilisant la méthode `System.exit(0)` dans le code Java. La documentation fournie dans les fichiers fournis fournit les détails techniques nécessaires pour comprendre et utiliser correctement le code.

## Quelles sont les classes principales et leurs responsabilités dans JavaSpace ?

### Classes Principales et Responsabilités dans JavaSpace

#### 1. **Main.java**
- **Responsabilités :**
  - **Initialisation du Jeu :** Déclare et initialise l'objet `Jeu`.
  - **Gestion du Jeu :** Gère le déroulement du jeu en boucle, en appelant les méthodes du jeu pour la mise à jour du menu et la gestion du statut du jeu.
  - **Thread.sleep :** Utilise `Thread.sleep` pour contrôler le déplacement fluide des images et le déplacement des joueurs avec le clavier.

#### 2. **Jeu.java**
- **Responsabilités :**
  - **Constantes :** Définit les constantes de phase du jeu (SHOOT et BOSS), la vie du boss, et les textures pour les lasers du boss.
  - **Mise à Jour du Menu :** Appelle la méthode `majMenu()` pour mettre à jour le menu du jeu.
  - **Statut du Jeu :** Gère le statut du jeu en appelant la méthode `getStatus()` pour vérifier si le jeu est en cours.
  - **Fin du Jeu :** Vérifie si la vie du joueur est différente de zéro pour continuer la boucle de jeu.

#### 3. **Ennemi.java**
- **Responsabilités :**
  - **Constructeur :** Permet de créer un ennemi avec des attributs tels que la texture, la vitesse, la vie et le trajet.
  - **Getters et Setters :** Permettent d'obtenir et de modifier les attributs de l'ennemi.
  - **Méthodes de Déplacement :** Permettent aux ennemis de se déplacer selon un trajet défini.

#### 4. **Boss.java**
- **Responsabilités :**
  - **Constructeur :** Permet de créer un boss avec des attributs tels que la texture, la vitesse, la vie et le trajet.
  - **Méthode d'Apparition :** Permet au boss de se déplacer et de vérifier s'il est en dehors de l'écran.
  - **Méthode de Déplacement :** Permet au boss de se déplacer selon un trajet défini.

#### 5. **Bonus.java**
- **Responsabilités :**
  - **Constructeur :** Permet de créer un bonus avec des attributs tels que la texture, le numéro du bonus et la durée.
  - **Getters et Setters :** Permettent d'obtenir et de modifier les attributs du bonus.
  - **Méthodes de Gestion :** Permettent de gérer les bonus, notamment leur durée et leur numéro.

#### 6. **ClavierBorneArcade.java**
- **Responsabilités :**
  - **Classe de KeyListener :** Implémente les méthodes de KeyListener pour gérer les entrées clavier.
  - **Méthodes de Gestion des Joysticks et Boutons :** Permettent de gérer les entrées provenant des joysticks et des boutons de la borne d'arcade.

#### 7. **description.txt**
- **Responsabilités :**
  - **Description du Jeu :** Fournit une description du jeu, en particulier les objectifs et le contexte de l'histoire.

#### 8. **bouton.txt**
- **Responsabilités :**
  - **Configuration des Boutons :** Fournit une configuration des boutons de la borne d'arcade, notamment les mouvements et les actions associées.

### Conclusion
Les classes principales dans JavaSpace sont `Main`, `Jeu`, `Ennemi`, `Boss`, `Bonus`, `ClavierBorneArcade`, `description.txt`, et `bouton.txt`. Chaque classe a des responsabilités spécifiques liées à la gestion du jeu, à la création et à la manipulation des ennemis, des bonus, et à la gestion des entrées clavier et joysticks.


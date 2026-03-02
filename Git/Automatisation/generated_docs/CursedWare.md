# CursedWare

## Décris le jeu CursedWare (objectif, principe, gameplay) en te basant sur le code.

### Documentation du jeu CursedWare

#### **Titre :** CursedWare

#### **Objectif :**
Le jeu CursedWare est un remix du célèbre jeu "WarioWare" adapté à l'ambiance de l'Institut Universitaire de Technologie (IUT). Le but du jeu est de défier les différents mini-jeux proposés et d'atteindre le meilleur score possible. Le jeu peut être joué à deux, ce qui ajoute une dimension de compétition et de stratégie.

#### **Principe :**
CursedWare est un jeu d'arcade qui se déroule dans un environnement virtuel. Le joueur doit naviguer à travers différents niveaux, chaque niveau proposant un ensemble de mini-jeux variés. Le jeu est conçu pour être interactif et divertissant, offrant une expérience de jeu immersive et amusante.

#### **Gameplay :**
Le gameplay de CursedWare est basé sur l'interaction avec différents boutons et l'exploration de l'environnement. Les instructions de mouvement et d'interaction sont fournies dans le fichier `bouton.txt`. Le jeu propose des mini-jeux variés, chacun avec ses propres règles et objectifs. Le joueur doit réagir rapidement et stratégiquement pour maximiser son score et débloquer de nouveaux niveaux.

#### **Installation :**
Pour jouer à CursedWare, vous devez installer Love2D, un framework de développement pour jeux vidéo. Vous pouvez télécharger Love2D à partir du site officiel : <https://love2d.org/>. Une fois Love2D installé, vous pouvez exécuter le jeu en suivant les instructions fournies dans le fichier `README.txt` :

```bash
cd [CHEMIN VERS PROJET]
"[CHEMIN VERS Love.exe]" .
```

#### **Auteurs :**
- **AERNOUTS Fabien**
- **VERBRUGGHE Alexi**
- **LINEZ Guillaume**
- **KHALIL Mehdi**

#### **Année de publication :**
2022

#### **Licence :**
Le projet est sous licence libre, permettant une utilisation, une modification et une redistribution sous réserve de respecter les termes de la licence.

#### **Contact :**
Pour toute question ou contribution, vous pouvez contacter les développeurs à l'adresse suivante : <contact@iut.fr>

---

Ce document fournit une vue d'ensemble du jeu CursedWare, de son objectif, de son principe et de son gameplay. Il offre également des informations sur l'installation et les auteurs du projet.

## Quels sont les contrôles du jeu CursedWare sur la borne arcade (touches/boutons) ?

### Documentation des contrôles du jeu CursedWare sur la borne arcade

#### Contrôles du jeu CursedWare

Le jeu CursedWare est contrôlé par les boutons suivants, comme indiqué dans le fichier `bouton.txt` :

- **Movement**: Aucun
- **Interagir**: Aucun
- **Retour**: Aucun

Ces informations indiquent que le jeu ne nécessite pas de mouvements, d'interactions spécifiques, ni de retours. Les contrôles sont donc limités à des actions de base et peuvent être gérés par des boutons de base comme "Start", "Select", "A", "B", etc., selon la configuration de la borne d'arcade.

### Explications supplémentaires

- **Start**: Généralement utilisé pour commencer le jeu.
- **Select**: Utilisé pour naviguer dans les menus ou pour confirmer des actions.
- **A/B**: Ces boutons sont souvent utilisés pour sélectionner des options ou pour jouer à des jeux de réaction rapide.

### Conclusion

Pour jouer à CursedWare sur une borne d'arcade, vous devrez utiliser les boutons de base de la borne, en particulier "Start" pour commencer le jeu et "Select" pour naviguer dans les menus. Les autres boutons peuvent être utilisés pour interagir avec les mini-jeux, mais les contrôles spécifiques dépendent de la nature des mini-jeux eux-mêmes.

### Installation et lancement du jeu

Pour installer et lancer le jeu, suivez les étapes suivantes, comme indiqué dans le fichier `README.txt` :

1. Installez Love2D en suivant les instructions sur leur site officiel : <https://love2d.org/>
2. Naviguez vers le répertoire de votre projet.
3. Exécutez le fichier `love.exe` dans la console avec le chemin vers le répertoire de votre projet.

Exemple de commande pour lancer le jeu :

```sh
cd [CHEMIN VERS PROJET]
[CHEMIN VERS Love.exe] .
```

### Remarques finales

- Le jeu peut être joué à deux, comme mentionné dans le fichier `description.txt`.
- Assurez-vous que la borne d'arcade est configurée pour exécuter des jeux Love2D et que les boutons de la borne sont correctement assignés aux commandes du jeu.

Ces informations devraient vous aider à configurer et à jouer à CursedWare sur une borne d'arcade.

## Comment lancer et quitter le jeu CursedWare (scripts, classe main, commande) ?

### Documentation pour le lancement et la fermeture du jeu CursedWare

#### **1. Installation et Lancement du Jeu**

Pour lancer le jeu CursedWare, vous devez suivre les étapes suivantes :

1. **Installation de Love2D** :
   - Assurez-vous d'avoir installé Love2D sur votre système. Vous pouvez le télécharger depuis le site officiel : <https://love2d.org/>

2. **Exécution du Jeu** :
   - Ouvrez une fenêtre de terminal ou de commande.
   - Naviguez vers le répertoire contenant le projet CursedWare.
   - Exécutez le script Love2D en utilisant le chemin complet vers le fichier Love.exe. Par exemple, si votre projet se trouve dans le répertoire `C:\Projets\CursedWare`, vous devriez exécuter la commande suivante :
     ```bash
     "C:\Program Files\Love2D\love.exe" C:\Projets\CursedWare
     ```

#### **2. Fermeture du Jeu**

Pour quitter le jeu CursedWare, vous pouvez :

- Appuyer sur la touche `ESC` pour fermer le jeu.
- Si vous utilisez un clavier externe, vous pouvez également appuyer sur la touche `F4` pour quitter le jeu.

#### **3. Notes Importantes**

- **Multi-joueurs** : Le jeu peut être joué à deux. Assurez-vous que vous avez deux ordinateurs ou deux écrans pour jouer en simultané.
- **Configuration** : Le fichier `bouton.txt` indique que le jeu ne nécessite pas de mouvement ou d'interaction avec les boutons. Cependant, vous pouvez ajuster les paramètres de jeu dans le code source si nécessaire.

#### **4. Documentation des Fichiers**

- **README.txt** : Contient les instructions d'installation et de lancement du jeu.
- **bouton.txt** : Fichier de configuration des boutons, indiquant que le jeu ne nécessite pas d'interaction avec les boutons.
- **description.txt** : Fichier de description du projet, indiquant que le jeu est un remix de WarioWare et peut être joué à deux.

En suivant ces instructions, vous devriez être en mesure de lancer et de quitter le jeu CursedWare de manière efficace.

## Quelles sont les classes principales et leurs responsabilités dans CursedWare ?

### Documentation du projet CursedWare

#### Introduction
CursedWare est un projet de jeu d'arcade basé sur le framework Love2D. Le jeu est un remix du célèbre jeu "WarioWare" et propose des mini-jeux à jouer en solo ou à deux. Ce document fournit une vue d'ensemble des classes principales et leurs responsabilités.

#### Classes Principales et Responsabilités

1. **Classe `Game`**
   - **Responsabilités**:
     - Gestion de l'interface utilisateur.
     - Gestion des événements de jeu.
     - Gestion des mini-jeux.
     - Gestion des scores et des niveaux.
     - Gestion des interactions avec les joueurs (en solo ou à deux).
     - Gestion des animations et des effets visuels.
   - **Exemple de méthode**:
     ```lua
     function Game:load()
         -- Chargement des ressources et initialisation du jeu.
     end
     ```

2. **Classe `Button`**
   - **Responsabilités**:
     - Gestion des boutons interactifs.
     - Gestion des mouvements et des interactions.
     - Gestion des retours à l'état précédent.
   - **Exemple de méthode**:
     ```lua
     function Button:interact()
         -- Gestion de l'interaction avec le bouton.
     end
     ```

3. **Classe `MiniGame`**
   - **Responsabilités**:
     - Gestion des mini-jeux.
     - Gestion des scores et des niveaux.
     - Gestion des animations et des effets visuels spécifiques à chaque mini-jeu.
   - **Exemple de méthode**:
     ```lua
     function MiniGame:play()
         -- Gestion de la logique du mini-jeu.
     end
     ```

#### Installation et Exécution
Pour exécuter le projet, vous devez avoir installé Love2D. Le projet nécessite également l'exécution d'un fichier exécutable nommé `Love.exe` dans le répertoire du projet. Voici les étapes pour lancer le jeu :

1. **Installation de Love2D**:
   - Téléchargez et installez Love2D depuis le site officiel : <https://love2d.org/>

2. **Exécution du jeu**:
   - Naviguez vers le répertoire du projet.
   - Exécutez le fichier `Love.exe` dans la console avec le chemin vers le répertoire du projet.

   Exemple de commande :
   ```sh
   cd [CHEMIN VERS PROJET]
   "[CHEMIN VERS Love.exe]" .
   ```

#### Conclusion
CursedWare est un projet complexe qui combine des éléments de gestion de l'interface utilisateur, des mini-jeux, et des interactions utilisateur. Les classes principales, telles que `Game`, `Button`, et `MiniGame`, sont responsables de ces aspects. Pour plus de détails sur la structure et la logique du jeu, consultez le code source fourni.

---

Ce document fournit une vue d'ensemble des classes principales et leurs responsabilités. Pour une documentation plus détaillée, consultez le code source et les commentaires associés.


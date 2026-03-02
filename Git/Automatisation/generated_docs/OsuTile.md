# OsuTile

## Décris le jeu OsuTile (objectif, principe, gameplay) en te basant sur le code.

### Description du Jeu OsuTile

#### Objectif
OsuTile est un jeu d'arcade où le joueur doit toucher le plus de notes possibles en les déviant vers la gauche ou la droite. Le jeu se déroule sur une grille de 4 voies (lanes) et les notes tombent en continu.

#### Principe
Le jeu est basé sur le format de fichier `.osu` utilisé par le jeu Osu! et le convertit en format interne pour le jeu. Les notes sont représentées par des rectangles qui tombent du haut vers le bas de l'écran. Le joueur doit déviant les notes vers la gauche ou la droite pour les faire toucher. Si une note n'est pas déviée à temps, elle se transforme en un "miss" et le joueur perd une vie.

#### Gameplay
1. **Configuration de la Borne d'Arcade**:
   - Le jeu est configuré pour une résolution de 1280x960 pixels avec 60 FPS.
   - Les touches de jeu sont mappées pour chaque voie (Lane 1 à Lane 4) et pour les actions de pause et de menu.
   - Les touches de navigation dans les menus sont également mappées.

2. **Génération des Maps**:
   - Les cartes de jeu sont générées à partir de fichiers `.osu` utilisant le script `tools/export_map.py`. Chaque fichier `.osu` est converti en un module Python (`<map_name>.py`) qui contient les informations sur les notes et les temps de déviation.

3. **Affichage et Interactions**:
   - Le jeu utilise des sprites pour représenter les notes et les déviers.
   - Les notes tombent en fonction du temps et de la position sur l'écran.
   - Les déviers sont effectués en appuyant sur les touches de jeu mappées pour chaque voie.

4. **Score et Vies**:
   - Le score est calculé en fonction du nombre de notes touchées.
   - Les vies sont réduites lorsque les notes ne sont pas déviées à temps.

5. **Menu et Pause**:
   - Le jeu dispose d'un menu principal avec des options pour reprendre, quitter, et revenir au menu principal.
   - Un menu de pause permet de gérer les actions de pause et de reprendre le jeu.

#### Structure du Jeu
- **Fichier `game.py`** : Gestion de l'interface principale du jeu, chargement des cartes de jeu, et gestion des sprites.
- **Fichier `main.py`** : Gestion de l'export des cartes de jeu et de l'affichage du menu principal.
- **Fichier `menu.py`** : Gestion de l'affichage du menu principal et des interactions avec le joueur.
- **Fichier `bouton.txt`** : Mappage des touches de jeu pour chaque voie et les actions de pause et de menu.
- **Fichier `config.py`** : Configuration des paramètres de base du jeu, tels que la résolution, la couleur de fond, et les touches de jeu.
- **Fichier `map_parser.py`** : Conversion des fichiers `.osu` en format interne pour le jeu.
- **Fichier `tile.py`** : Gestion des sprites représentant les notes et les déviers.

#### Conclusion
OsuTile est un jeu d'arcade qui utilise les cartes de jeu `.osu` pour générer des cartes de jeu interactives. Le joueur doit déviant les notes tombant en continu pour les toucher. Le jeu est configuré pour une résolution de 1280x960 pixels et dispose de menus pour gérer les actions de pause et de reprendre le jeu. Les cartes de jeu sont converties en format interne pour le jeu à l'aide d'un script d'exportation.

## Quels sont les contrôles du jeu OsuTile sur la borne arcade (touches/boutons) ?

### Contrôles du jeu OsuTile sur la borne arcade

#### Mappage des touches de jeu par colonne
Le mappage des touches de jeu est défini dans le fichier `config.py` et est utilisé pour contrôler les mouvements et les actions dans le jeu.

- **Colonne 0 (Lane 1)** : `pygame.K_t`
- **Colonne 1 (Lane 2)** : `pygame.K_y`
- **Colonne 2 (Lane 3)** : `pygame.K_a`
- **Colonne 3 (Lane 4)** : `pygame.K_z`

#### Contrôles de navigation dans les menus
Les contrôles de navigation dans les menus sont également définis dans le fichier `config.py`.

- **Menu Up** : `pygame.K_UP`
- **Menu Down** : `pygame.K_DOWN`
- **Menu Select** : `pygame.K_g`
- **Menu Back** : `pygame.K_h`

#### Contrôles pour les menus (pause, fin)
Les contrôles spécifiques pour les menus (pause, fin) sont également définis dans le fichier `config.py`.

- **Menu Resume** : `pygame.K_g`
- **Menu Quit** : `pygame.K_q`

#### Pause
La touche de pause est définie comme `pygame.K_f` dans le fichier `config.py`.

#### Interactions
Les interactions sont définies dans le fichier `bouton.txt` et sont utilisées pour interagir avec le menu.

- **Interact** : `pygame.K_i`

#### Retour
Le retour est défini comme `pygame.K_h` dans le fichier `config.py`.

### Résumé
- **Touches de jeu** : `pygame.K_t`, `pygame.K_y`, `pygame.K_a`, `pygame.K_z`
- **Menu Up** : `pygame.K_UP`
- **Menu Down** : `pygame.K_DOWN`
- **Menu Select** : `pygame.K_g`
- **Menu Back** : `pygame.K_h`
- **Menu Resume** : `pygame.K_g`
- **Menu Quit** : `pygame.K_q`
- **Pause** : `pygame.K_f`
- **Interact** : `pygame.K_i`
- **Retour** : `pygame.K_h`

Cette documentation fournit une vue d'ensemble des contrôles utilisés pour interagir avec le jeu OsuTile sur la borne arcade.

## Comment lancer et quitter le jeu OsuTile (scripts, classe main, commande) ?

### Documentation pour lancer et quitter le jeu OsuTile

#### **1. Lancer le jeu OsuTile**

Pour lancer le jeu OsuTile, vous devez exécuter le script `main.py`. Ce script est responsable de l'exportation des maps et de l'exécution du menu principal.

```bash
python3 main.py
```

#### **2. Quitter le jeu OsuTile**

Pour quitter le jeu, vous pouvez utiliser les touches de menu définies dans le fichier `config.py` :

- **MENU_QUIT_KEY** : Cette touche permet de quitter le menu principal et peut être utilisée pour quitter le jeu.

```python
# Dans le fichier main.py
if event.key == pygame.K_g:  # MENU_QUIT_KEY
    pygame.quit()
    sys.exit()
```

#### **3. Structure du projet**

- **main.py** : Ce script est le point d'entrée du projet. Il s'occupe de l'exportation des maps et de l'exécution du menu principal.
- **menu.py** : Ce script gère l'affichage du menu principal et les interactions avec l'utilisateur.
- **config.py** : Ce fichier contient les configurations générales du jeu, telles que les dimensions de l'écran, les couleurs, les touches de contrôle, etc.
- **game.py** : Ce script contient la logique principale du jeu, notamment la gestion des tiles et des notes.
- **tile.py** : Ce script définit la classe `Tile` qui gère les positions et les animations des notes dans le jeu.
- **map_parser.py** : Ce script permet de parser les fichiers `.osu` et de les convertir en format utilisable pour le jeu.
- **bouton.txt** : Ce fichier contient les mappages des touches de jeu par colonne.
- **description.txt** : Ce fichier contient une description du jeu.

#### **4. Exécution du jeu**

Pour exécuter le jeu, vous devez vous assurer que tous les fichiers nécessaires sont dans le même répertoire que `main.py`. Vous pouvez également utiliser un environnement virtuel pour gérer les dépendances Python.

```bash
# Créer un environnement virtuel (si nécessaire)
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances (si nécessaire)
pip install pygame

# Exécuter le jeu
python3 main.py
```

#### **5. Documentation des fichiers**

- **main.py** : Ce script est le point d'entrée du projet. Il s'occupe de l'exportation des maps et de l'exécution du menu principal.
- **menu.py** : Ce script gère l'affichage du menu principal et les interactions avec l'utilisateur.
- **config.py** : Ce fichier contient les configurations générales du jeu, telles que les dimensions de l'écran, les couleurs, les touches de contrôle, etc.
- **game.py** : Ce script contient la logique principale du jeu, notamment la gestion des tiles et des notes.
- **tile.py** : Ce script définit la classe `Tile` qui gère les positions et les animations des notes dans le jeu.
- **map_parser.py** : Ce script permet de parser les fichiers `.osu` et de les convertir en format utilisable pour le jeu.
- **bouton.txt** : Ce fichier contient les mappages des touches de jeu par colonne.
- **description.txt** : Ce fichier contient une description du jeu.

#### **6. Conclusion**

Pour lancer et quitter le jeu OsuTile, vous devez exécuter le script `main.py`. Vous pouvez utiliser les touches de menu définies dans le fichier `config.py` pour quitter le jeu. Les autres fichiers sont responsables de la gestion des maps, des touches de jeu, et de la logique du jeu.

## Quelles sont les classes principales et leurs responsabilités dans OsuTile ?

### Classes Principales et Responsabilités dans OsuTile

#### 1. **Tile**
- **Responsabilités :**
  - **Classe de base pour les blocs de notes.**
  - **Attributs :**
    - `lane`: Ligne de la note (0 à 3).
    - `time`: Temps de l'apparition de la note (en ms).
    - `hit`: Indicateur de frappe (True si frappé, False sinon).
  - **Méthodes :**
    - `get_y(current_time)`: Calcule la position y de la note en fonction du temps actuel.
    - `draw(surface, x, width, current_time, color)`: Dessine le bloc de note sur la surface de dessin.

#### 2. **Game**
- **Responsabilités :**
  - **Classe principale pour le jeu.**
  - **Attributs :**
    - `SCREEN_WIDTH`, `SCREEN_HEIGHT`: Dimensions de la fenêtre.
    - `BACKGROUND_COLOR`, `LANE_COLOR`, `TEXT_COLOR`, `HIGHLIGHT_COLOR`: Couleurs de fond et de texte.
    - `LANE_COUNT`, `TILE_COLOR`, `HIT_LINE_Y`, `FPS`, `FULLSCREEN`: Paramètres de jeu.
    - `KEY_MAPPING`: Mappage des touches de jeu.
    - `PAUSE_KEY`, `MENU_RESUME_KEY`, `MENU_QUIT_KEY`, `MENU_BACK_TO_MENU_KEY`, `MENU_RETRY_KEY`: Touches de contrôle.
  - **Méthodes :**
    - `load_beatmap(filename)`: Charge un beatmap à partir d'un fichier.
    - `draw_pause_menu(screen, font)`: Dessine le menu de pause.
    - `play_map(map_name)`: Joue un beatmap spécifique.

#### 3. **Menu**
- **Responsabilités :**
  - **Classe pour gérer les menus.**
  - **Attributs :**
    - `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `BACKGROUND_COLOR`, `TEXT_COLOR`, `HIGHLIGHT_COLOR`, `FPS`: Dimensions et couleurs de la fenêtre.
    - `BEATMAP_FOLDER`: Chemin vers le dossier des beatmaps.
    - `MENU_TITLE`, `SELECT_PROMPT`: Titre et prompt du menu.
    - `MENU_UP_KEY`, `MENU_DOWN_KEY`, `MENU_SELECT_KEY`, `MENU_QUIT_KEY`: Touches de navigation et de sélection.
  - **Méthodes :**
    - `draw_gradient_background(screen, color1, color2)`: Dessine un fond dégradé.
    - `neon_text(surface, text, font, pos, color)`: Affiche du texte avec un effet néon.
    - `run_menu()`: Gère l'affichage et la navigation dans les menus.

#### 4. **MapParser**
- **Responsabilités :**
  - **Classe pour parser les fichiers Osu.**
  - **Attributs :**
    - `lane_count`: Compte le nombre de lignes de notes.
  - **Méthodes :**
    - `parse_osu_file(filepath, lane_count=4)`: Lit et parse un fichier Osu pour extraire les notes.

#### 5. **Bouton.txt**
- **Responsabilités :**
  - **Fichier de configuration pour les boutons.**
  - **Attributs :**
    - Liste de mouvements et d'actions associées à chaque bouton.

#### 6. **Config.py**
- **Responsabilités :**
  - **Fichier de configuration pour les paramètres du jeu.**
  - **Attributs :**
    - Dimensions de la fenêtre, couleur de fond, fréquence d'images par seconde, etc.

#### 7. **Description.txt**
- **Responsabilités :**
  - **Fichier de description du jeu.**
  - **Attributs :**
    - Titre du jeu et objectif.

#### 8. **Main.py**
- **Responsabilités :**
  - **Fichier principal pour l'exécution du projet.**
  - **Attributs :**
    - Génération des beatmaps à partir des fichiers Osu.
    - Exécution du menu principal.
  - **Méthodes :**
    - `ensure_maps_exported()`: Génère les beatmaps à partir des fichiers Osu.
    - `run_menu()`: Exécute le menu principal.

### Conclusion
Les classes principales dans OsuTile sont `Tile`, `Game`, `Menu`, `MapParser`, et `Config`. Chaque classe a des responsabilités spécifiques liées à la gestion des blocs de notes, du jeu, des menus, de la lecture des fichiers Osu, et des paramètres du jeu. Les autres fichiers (description.txt, bouton.txt) fournissent des informations supplémentaires et de configuration.


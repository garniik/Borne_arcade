# Rapport SAE - Développement de la Borne Arcade

## Liste des choses réalisées durant la SAE

### 1. Migration vers Raspberry Pi
- Passage du système sous Raspberry Pi modèle 3 pour une meilleure intégration matérielle.
- Installation d'un système d'exploitation Raspberry Pi OS, téléchargé via l'imager officiel (https://www.raspberrypi.com/software/).
- Configuration pour écran 4:3 en résolution 1280x1024, adapté à la borne arcade.

### 2. Correction des problèmes d'imports
- Résolution des imports pour MG2D (bibliothèque Java 2D), Python, Java, et autres dépendances.
- Installation automatique des paquets via apt-get : git, curl, wget, build-essential, default-jdk, python3, python3-pip, python3-pygame, xdotool, love.
- Compilation de MG2D depuis les sources GitHub (https://github.com/synave/MG2D.git) et ajout au CLASSPATH dans ~/.bashrc automatique.

### 3. Ajout d'un script d'installation automatique
- Développement du script `install-all.sh` pour automatiser l'installation complète.
- Le script met à jour le système (apt update/upgrade), installe les dépendances, clone et compile MG2D, configure l'environnement Python virtuel, copie les fichiers de configuration clavier (`borne` vers `/usr/share/X11/xkb/symbols/`), et active le lancement automatique au démarrage via un fichier .desktop dans `~/.config/autostart/`.

### 4. Ajout d'un script de lancement automatique
- Création d'un script de lancement (`lancerBorne.sh`) pour démarrer l'interface de la borne.
- Configuration du démarrage automatique au boot via un fichier .desktop pointant vers le script de lancement.

### 5. Ajout d'un script d'automatisation de documentation pour les jeux
- Intégration d'outils pour générer automatiquement la documentation des jeux (JavaDoc pour les jeux Java, etc.).
- Mise à jour du README.md avec les instructions d'installation automatisée, remplaçant les étapes manuelles.

### 6. Ajout d'un jeu (Balapy)
- Intégration du jeu Balapy dans la collection de jeux de la borne.
- Adaptation et test pour le système Raspberry Pi et les contrôles de la borne.

### 7. Tentative d'ajout d'un script de génération de documentation utilisateur/technique
- Essai de développement d'un script pour générer automatiquement la documentation utilisateur et technique.
- Abandonné en raison de timeouts constants dus à la durée excessive du rendu.

### 8. Correction du fichier de touches
- Modification du fichier `borne` (fichier de symboles XKB) pour corriger la correspondance entre les boutons physiques de la borne et les touches clavier.
- Corrections des mappings pour les joysticks (J1: flèches, J2: o l k m) et boutons (J1: r t y f g h, J2: a z e q s d).

### 9. Correction et mise à jour du README
- Révision complète du fichier README.md 
- Suppression des étapes manuelles désormais automatisées.

IUT du Littoral Côte d'Opale (IUTLCO)
====================================
Projet tutoré 2017-2018- 2ème année
----------------------------------

Groupe projet : Romaric Bougard, Pierre Delobel et Bastien Ducloy


Plus d'infos [ici](http://iut.univ-littoral.fr/gitlab/synave/borne_arcade/wikis/home)

# touche de la borne

Correspondance clavier -> bouton borne

joystick j1
fleches haut bas gauche droite

joystick j2
o l k m

6 touches J1
r t y
f g h

6 touches J2
a z e
q s d 

Attention ! De base, l'encodeur clavier de la borne de l'IUT a té mal relié aux boutons. Ce ne sont donc pas les bonnes lettres qui son identifiées lorsque l'on appuie sur un bouton ou fait bouger un joystick. Voir fichier **borne**


Contrainte matérielle
----
- Raspberry pi model 3 de préférence
- Ecran 4:3 de résolution 1280x1024
- Pour borne 2 joueurs, joystick et 6 boutons par joueur + d'autres boutons inutilisés pour le moment.


# Installation du système d'exploitation
----
Installez un os rasberry sur votre raspberry.
aller sur le site officel de raspberry pi et téléchargez l'imager : https://www.raspberrypi.com/software/
suivez les instructions pour flasher votre carte SD.
ensuite lancer la carte sur la raspberry pi.

# Installation automatique
----

Un script d'installation automatique est fourni pour simplifier le processus. Il installe toutes les dépendances nécessaires (Java, Python, MG2D, bibliothèques SDL pour pygame, etc.), configure l'environnement virtuel Python, copie les fichiers de configuration clavier et active le lancement automatique au démarrage.

Dans un terminal :

```
sudo apt-get update
```

```
sudo apt-get install git
```

```
cd ~
```

```
mkdir git
```

```
cd git
```

```
git clone https://github.com/garniik/Borne_arcade
```

```
cd borne_arcade
```

```
sudo ./install-all.sh
```

Le script install-all.sh gère automatiquement :
- Les dépendances système (Java, Python, libs SDL, etc.)
- La bibliothèque MG2D
- L'environnement virtuel Python avec les requirements
- La configuration du clavier personnalisé pour la borne
- Le lancement automatique au démarrage via autostart

Après l'installation, redémarrez la Raspberry Pi. Le logiciel de la borne se lancera automatiquement au démarrage.

Sélectionnez le jeu avec haut/bas du joystick du joueur 1 et lancez le jeu avec le bouton A du joueur 1.
Quittez le logiciel avec le bouton Z du joueur 1. Une demande de confirmation s'affichera. Validez oui ou non avec le bouton A du joueur 1.

Si vous quittez le menu, vous reviendrez sur le terminal. Attendez 30 secondes pour une extinction totale de la machine.


# génération des documents
----
la borne est fourni avec un script qui permet de générer des jeux 
assurez vous de bien etre sur le reseau de l'iut avant de lancer le script

rendez vous dans le dossier Automatisation :
```
cd Automatisation
```
```
python3 generate_games.py
```

# injecter des commentaire et la javadoc
----

la borne est fourni avec un script qui permet d'injecter des commentaire et la javadoc

rendez vous dans le dossier Automatisation :
```
cd Automatisation
```
```
python3 inject_docstring.py
```
```
python3 inject_javadoc.py
```


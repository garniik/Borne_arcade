#!/bin/bash
# Script de lancement pour Space Invaders

# Description: Lance le jeu Space Invaders sur la borne arcade
# Usage: ./lancement.sh

echo "Démarrage de Space Invaders..."

# Retour au répertoire principal
cd ../../

# Lancement du jeu avec la bibliothèque MG2D
java -cp .:MG2D projet/SpaceInvaders/SpaceInvaders

echo "Space Invaders terminé."

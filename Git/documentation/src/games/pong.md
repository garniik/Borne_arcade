# Pong

Jeu classique de Pong pour la borne arcade.

## Description

Pong est un jeu de tennis simplifié où deux joueurs contrôlent des raquettes pour frapper une balle.

## Contrôles

### Joueur 1
- **Haut/Bas**: Flèches haut/bas
- **Frapper**: Bouton A

### Joueur 2  
- **Haut/Bas**: O/L
- **Frapper**: Bouton A (Joueur 2)

## Règles du jeu

1. Chaque joueur contrôle une raquette
2. La balle rebondit sur les raquettes et les murs
3. Manquer la balle = point pour l'adversaire
4. Premier à atteindre 11 points gagne

## Installation

```bash
# Lancer Pong
cd borne_arcade
./Pong.sh
```

## Configuration

- **Vitesse balle**: Configurable dans le code
- **Taille raquettes**: Fixe
- **Score maximum**: 11 points

## Dépannage

### Problèmes courants

1. **Le jeu ne démarre pas**
   - Vérifier que Java est installé
   - Vérifier les permissions du script

2. **Contrôles ne répondent pas**
   - Vérifier le mapping des touches
   - Consulter [Hardware/Controls](../hardware/controls.md)

---

*Pour la liste complète des jeux, voir [Index des jeux](index.md)*

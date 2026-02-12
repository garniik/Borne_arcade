# Contrôles de la Borne Arcade

Documentation du système de contrôle de la borne arcade.

## Mapping des contrôles

### Joueur 1

#### Joystick
- **Haut**: Flèche haut
- **Bas**: Flèche bas  
- **Gauche**: Flèche gauche
- **Droite**: Flèche droite

#### Boutons (6 boutons)
- **Boutons supérieurs**: R, T, Y
- **Boutons inférieurs**: F, G, H

### Joueur 2

#### Joystick
- **Haut**: O
- **Bas**: L
- **Gauche**: K
- **Droite**: M

#### Boutons (6 boutons)
- **Boutons supérieurs**: A, Z, E
- **Boutons inférieurs**: Q, S, D

## Contrôles système

- **Sélection jeu**: Bouton A (Joueur 1)
- **Lancement jeu**: Bouton A (Joueur 1)
- **Quitter**: Bouton Z (Joueur 1)
- **Confirmation**: Bouton A (Joueur 1)

## Important

> **Attention** : L'encodeur clavier de la borne de l'IUT a été mal relié aux boutons. Les lettres identifiées ne correspondent pas forcément aux vrais boutons physiques. Voir le fichier **borne** pour le mapping réel.

## Configuration matérielle

- **Raspberry Pi 3** (recommandé)
- **Écran 4:3** (1280x1024)
- **2 joysticks**
- **12 boutons (6 par joueur)

## Dépannage

### Problèmes courants

1. **Boutons ne répondent pas**
   - Vérifier le branchement
   - Consulter le fichier `borne` pour le mapping

2. **Mauvaises touches détectées**
   - L'encodeur est mal configuré
   - Modifier le mapping dans `ClavierBorneArcade.java`

3. **Joystick ne fonctionne pas**
   - Vérifier la connexion USB
   - Tester avec `jstest`

---

*Pour la configuration complète, voir [Installation](../how-to/install.md)*

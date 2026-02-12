# How-to : Ajouter un jeu

Guide complet pour ajouter un nouveau jeu à la borne arcade.

## Prérequis

- Java 8+ installé
- Connaissance de base en Java
- Accès au dépôt Git

## 🎮 Structure d'un jeu

```
borne_arcade/projet/
├── MonJeu/                    # Dossier du jeu
│   ├── MonJeu.java           # Classe principale
│   ├── lancement.sh          # Script de lancement
│   └── README.md             # Documentation du jeu
```

## 🛠️ Étapes de création

### 1. Créer le dossier du jeu

```bash
cd borne_arcade/projet
mkdir MonJeu
cd MonJeu
```

### 2. Écrire le code Java

```java
// MonJeu.java
import MG2D.*;
import MG2D.geometrie.*;

public class MonJeu {
    private Fenetre f;
    private boolean enCours = true;
    
    public MonJeu() {
        f = new Fenetre("Mon Jeu", 1280, 1024);
    }
    
    public void jouer() {
        while(enCours) {
            // Logique du jeu
            f.rafraichir();
            try {
                Thread.sleep(16); // ~60 FPS
            } catch(InterruptedException e) {
                enCours = false;
            }
        }
        f.fermer();
    }
    
    public static void main(String[] args) {
        MonJeu jeu = new MonJeu();
        jeu.jouer();
    }
}
```

### 3. Créer le script de lancement

```bash
#!/bin/bash
# lancement.sh
cd ../../
java -cp .:MG2D projet/MonJeu/MonJeu
```

### 4. Ajouter au menu principal

Modifier `Graphique.java` pour inclure votre jeu dans la sélection.

### 5. Documenter le jeu

Créer `README.md` avec :
- Description du jeu
- Contrôles
- Règles
- Installation

## 🎯 Bonnes pratiques

### Code
- Utiliser la bibliothèque MG2D
- Gérer les entrées clavier avec `ClavierBorneArcade`
- Respecter les contrôles standards de la borne

### Performance
- Viser 60 FPS
- Optimiser les graphiques
- Gérer la mémoire correctement

### Documentation
- Documenter les contrôles
- Expliquer les règles
- Ajouter des exemples

## 🧪 Tests

### Test local
```bash
# Compiler
javac -cp .:MG2D projet/MonJeu/MonJeu.java

# Tester
java -cp .:MG2D projet/MonJeu/MonJeu
```

### Test sur borne
1. Copier les fichiers sur la borne
2. Lancer avec le script
3. Vérifier les contrôles
4. Tester le retour au menu

## 📝 Checklist avant intégration

- [ ] Code compile sans erreur
- [ ] Jeu fonctionne à 60 FPS
- [ ] Contrôles respectent le mapping standard
- [ ] Script de lancement fonctionnel
- [ ] Documentation complète
- [ ] Testé sur la borne réelle

## 🔧 Intégration au système

### 1. Ajouter au Git
```bash
git add projet/MonJeu/
git commit -m "feat: add MonJeu"
git push
```

### 2. Mettre à jour la documentation
- Ajouter `mon-jeu.md` dans `documentation/src/games/`
- Mettre à jour l'index des jeux

### 3. Créer une PR
- Ouvrir une Pull Request
- Faire reviewer le code
- Attendre l'approbation

---

*Pour l'installation de base, voir [Installation](install.md)*

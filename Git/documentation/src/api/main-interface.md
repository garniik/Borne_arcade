# API Main Interface

Documentation de l'interface principale de la borne arcade.

## Overview

La classe `Main` est le point d'entrée de l'application borne arcade.

## Classe Main

### Description

Classe principale qui initialise et lance l'interface graphique de la borne arcade.

### Méthodes

#### `main(String[] args)`
- **Type**: `public static void`
- **Paramètres**: `String[] args` - Arguments de ligne de commande
- **Description**: Point d'entrée principal de l'application
- **Comportement**: 
  - Crée une instance de `Graphique`
  - Lance la boucle de sélection de jeux

### Exemple d'utilisation

```java
// Lancement de la borne arcade
public class Main {
    public static void main(String[] args){
        Graphique g = new Graphique();
        while(true){
            try{
                // Thread.sleep(250);
            }catch(Exception e){};
            g.selectionJeu();
        }
    }
}
```

## Dépendances

- `Graphique` - Interface graphique principale
- Aucune dépendance externe

## Notes

- L'application tourne en boucle infinie
- La gestion des exceptions est minimale
- Le `Thread.sleep(250)` est commenté

---

*Pour plus de détails, voir [Graphique Interface](gui-components.md)*

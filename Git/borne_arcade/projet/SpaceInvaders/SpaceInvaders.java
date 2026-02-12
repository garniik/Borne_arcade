/**
 * Jeu Space Invaders pour la borne arcade.
 * Contrôlez un vaisseau spatial pour détruire les envahisseurs.
 */
public class SpaceInvaders {
    private boolean jeuEnCours = true;
    private int score = 0;
    
    /**
     * Constructeur du jeu Space Invaders.
     * Initialise les paramètres par défaut.
     */
    public SpaceInvaders() {
        // Initialisation du jeu
    }
    
    /**
     * Lance la boucle principale du jeu.
     * Gère les entrées joueur et la logique du jeu.
     */
    public void jouer() {
        while(jeuEnCours) {
            // Logique du jeu
        }
    }
    
    /**
     * Gère le mouvement du vaisseau joueur.
     * @param direction Direction du mouvement (-1: gauche, 1: droite)
     */
    public void deplacerVaisseau(int direction) {
        // Mouvement du vaisseau
    }
    
    /**
     * Tire un projectile depuis le vaisseau.
     * @return true si le tir a réussi
     */
    public boolean tirer() {
        return true;
    }
    
    /**
     * Point d'entrée pour lancer le jeu.
     * @param args Arguments de ligne de commande
     */
    public static void main(String[] args) {
        SpaceInvaders jeu = new SpaceInvaders();
        jeu.jouer();
    }
}

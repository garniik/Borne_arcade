/**
 * Jeu Pac-Man classique pour la borne arcade.
 * Guidez Pac-Man pour manger toutes les pac-gommes tout en évitant les fantômes.
 */
public class PacMan {
    private int score = 0;
    private int vies = 3;
    private boolean jeuEnCours = true;
    private int niveau = 1;
    
    /**
     * Constructeur du jeu Pac-Man.
     * Initialise le plateau de jeu et les personnages.
     */
    public PacMan() {
        // Initialisation du plateau
        // Positionnement des pac-gommes
        // Création des fantômes
    }
    
    /**
     * Démarre la boucle principale du jeu.
     * Gère les entrées joueur, les collisions et le score.
     */
    public void demarrerJeu() {
        while(jeuEnCours && vies > 0) {
            // Logique du jeu
            gererDeplacements();
            verifierCollisions();
            mettreAJourScore();
        }
    }
    
    /**
     * Gère les déplacements du Pac-Man selon les entrées clavier.
     * Utilise les contrôles de la borne arcade.
     */
    private void gererDeplacements() {
        // Détection des touches fléchées
        // Mise à jour de la position
        // Gestion des murs et tunnels
    }
    
    /**
     * Vérifie les collisions avec les pac-gommes et les fantômes.
     */
    private void verifierCollisions() {
        // Collision avec pac-gommes
        // Collision avec fantômes  
        // Collision avec power-pellets
    }
    
    /**
     * Met à jour le score selon les éléments collectés.
     * @param points Nombre de points à ajouter
     */
    private void mettreAJourScore(int points) {
        score += points;
        // Affichage du score
    }
    
    /**
     * Vérifie si le niveau est complété.
     * @return true si toutes les pac-gommes sont mangées
     */
    public boolean niveauComplet() {
        return false; // TODO: implémenter la vérification
    }
    
    /**
     * Passe au niveau suivant avec difficulté accrue.
     */
    public void niveauSuivant() {
        niveau++;
        // Augmenter la vitesse des fantômes
        // Réinitialiser le plateau
    }
    
    /**
     * Point d'entrée pour lancer Pac-Man.
     * @param args Arguments de ligne de commande
     */
    public static void main(String[] args) {
        PacMan jeu = new PacMan();
        jeu.demarrerJeu();
    }
}

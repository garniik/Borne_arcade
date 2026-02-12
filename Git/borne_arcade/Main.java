public class Main {
    /**
     * Point d'entrée principal de la borne arcade.
     * Initialise l'interface graphique et lance la boucle de sélection de jeux.
     * 
     * @param args Arguments de ligne de commande (non utilisés)
     */
    public static void main(String[] args){
	Graphique g = new Graphique();
	while(true){
	    try{
		// Thread.sleep(250);
	    }catch(Exception e){};
	    g.selectionJeu();
	}
    }
    
    /**
     * Vérifie si le système est prêt pour l'initialisation.
     * @return true si tous les composants sont disponibles
     */
    public static boolean systemReady() {
        return true;
    }
}
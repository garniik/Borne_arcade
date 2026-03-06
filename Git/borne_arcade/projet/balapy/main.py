"""
BALATRO ARCADE - Jeu de poker style Balatro
Contrôles:
  FLECHES GAUCHE/DROITE : naviguer entre les cartes
  FLECHE HAUT           : sélectionner/désélectionner une carte
  R                     : jouer la main sélectionnée
  F                     : défausser les cartes sélectionnées
  T                     : utiliser un joker (si disponible)
  G                     : voir les scores / stats
  Y                     : aller au shop (entre les rondes)
  H                     : passer au niveau suivant
"""
import sys
import os

# S'assure que le dossier src est dans le path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import pygame
from game import Game

def main():
    pygame.init()
    pygame.display.set_caption("BALATRO ARCADE")

    # Résolution pour borne d'arcade (plein écran)
    info = pygame.display.Info()
    SCREEN_W = info.current_w
    SCREEN_H = info.current_h

    # Pour debug sur PC: forcer une résolution fixe
    # SCREEN_W, SCREEN_H = 1280, 720

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    game = Game(screen, SCREEN_W, SCREEN_H)

    while True:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game.handle_input(event.key)

        game.update(dt)
        game.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()

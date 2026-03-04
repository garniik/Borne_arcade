import pygame
import sys
import random
from pygame.locals import *

# Initialisation
pygame.init()

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
MAZE_WIDTH = SCREEN_WIDTH // CELL_SIZE
MAZE_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Couleurs
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.color = YELLOW
        
    def move(self, dx, dy, maze):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
            if maze[int(new_y)][int(new_x)] != 1:
                self.x = new_x
                self.y = new_y
                
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, 
                         (int(self.x * CELL_SIZE + CELL_SIZE // 2), 
                          int(self.y * CELL_SIZE + CELL_SIZE // 2)), 
                         CELL_SIZE // 2 - 2)

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 0.5
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        
    def move(self, maze, player):
        # Mouvement simple vers le joueur
        if random.random() < 0.7:  # 70% de chance de suivre le joueur
            dx = player.x - self.x
            dy = player.y - self.y
            
            if abs(dx) > abs(dy):
                self.direction = (1 if dx > 0 else -1, 0)
            else:
                self.direction = (0, 1 if dy > 0 else -1)
        else:
            # Mouvement aléatoire
            if random.random() < 0.1:
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed
        
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
            if maze[int(new_y)][int(new_x)] != 1:
                self.x = new_x
                self.y = new_y
            else:
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                         (int(self.x * CELL_SIZE + CELL_SIZE // 2),
                          int(self.y * CELL_SIZE + CELL_SIZE // 2)),
                         CELL_SIZE // 2 - 2)

def create_maze():
    # Crée un labyrinthe simple (0 = vide, 1 = mur, 2 = point)
    maze = [[0 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
    
    # Ajoute les murs extérieurs
    for i in range(MAZE_WIDTH):
        maze[0][i] = 1
        maze[MAZE_HEIGHT-1][i] = 1
    for i in range(MAZE_HEIGHT):
        maze[i][0] = 1
        maze[i][MAZE_WIDTH-1] = 1
    
    # Ajoute quelques murs intérieurs
    for i in range(5, MAZE_WIDTH-5, 8):
        for j in range(5, MAZE_HEIGHT-5, 6):
            maze[j][i] = 1
            if i + 2 < MAZE_WIDTH-1:
                maze[j][i+2] = 1
            if j + 2 < MAZE_HEIGHT-1:
                maze[j+2][i] = 1
    
    # Ajoute des points
    for y in range(1, MAZE_HEIGHT-1):
        for x in range(1, MAZE_WIDTH-1):
            if maze[y][x] == 0 and random.random() < 0.3:
                maze[y][x] = 2
    
    return maze

def draw_maze(screen, maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:  # Mur
                pygame.draw.rect(screen, BLUE,
                               (x * CELL_SIZE, y * CELL_SIZE, 
                                CELL_SIZE, CELL_SIZE))
            elif maze[y][x] == 2:  # Point
                pygame.draw.circle(screen, WHITE,
                                 (x * CELL_SIZE + CELL_SIZE // 2,
                                  y * CELL_SIZE + CELL_SIZE // 2), 3)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pacman")
    clock = pygame.time.Clock()
    
    # Police pour le score
    font = pygame.font.Font(None, 36)
    
    # Crée le labyrinthe
    maze = create_maze()
    
    # Crée le joueur
    player = Player(1, 1)
    
    # Crée les fantômes
    ghosts = [
        Ghost(MAZE_WIDTH-2, 1, RED),
        Ghost(MAZE_WIDTH-2, MAZE_HEIGHT-2, PINK),
        Ghost(1, MAZE_HEIGHT-2, BLUE)
    ]
    
    score = 0
    game_over = False
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and not game_over:
                if event.key == K_UP:
                    player.move(0, -1, maze)
                elif event.key == K_DOWN:
                    player.move(0, 1, maze)
                elif event.key == K_LEFT:
                    player.move(-1, 0, maze)
                elif event.key == K_RIGHT:
                    player.move(1, 0, maze)
                elif event.key == K_r and game_over:
                    # Recommence le jeu
                    maze = create_maze()
                    player = Player(1, 1)
                    ghosts = [
                        Ghost(MAZE_WIDTH-2, 1, RED),
                        Ghost(MAZE_WIDTH-2, MAZE_HEIGHT-2, PINK),
                        Ghost(1, MAZE_HEIGHT-2, BLUE)
                    ]
                    score = 0
                    game_over = False
        
        if not game_over:
            # Déplace les fantômes
            for ghost in ghosts:
                ghost.move(maze, player)
                
                # Vérifie les collisions avec le joueur
                if abs(ghost.x - player.x) < 0.5 and abs(ghost.y - player.y) < 0.5:
                    game_over = True
            
            # Vérifie si le joueur mange un point
            if maze[int(player.y)][int(player.x)] == 2:
                maze[int(player.y)][int(player.x)] = 0
                score += 10
                
                # Vérifie si tous les points ont été mangés
                points_remaining = sum(row.count(2) for row in maze)
                if points_remaining == 0:
                    game_over = True
        
        # Dessine tout
        screen.fill(BLACK)
        draw_maze(screen, maze)
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        
        # Affiche le score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Affiche game over
        if game_over:
            game_over_text = font.render("GAME OVER! Press R to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

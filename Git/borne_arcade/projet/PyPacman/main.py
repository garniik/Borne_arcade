import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# Constantes
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680
CELL_SIZE = 20
MAZE_WIDTH = 39   # doit être impair pour DFS
MAZE_HEIGHT = 31  # doit être impair pour DFS
MAZE_OFFSET_X = (SCREEN_WIDTH - MAZE_WIDTH * CELL_SIZE) // 2
MAZE_OFFSET_Y = 60  # espace pour le score en haut

# Couleurs
BLACK      = (0, 0, 0)
DARK_BG    = (10, 10, 30)
YELLOW     = (255, 220, 0)
WHITE      = (255, 255, 255)
RED        = (220, 50, 50)
BLUE_WALL  = (30, 80, 200)
BLUE_WALL2 = (60, 120, 255)
PINK       = (255, 100, 180)
CYAN       = (0, 220, 220)
ORANGE     = (255, 165, 0)
DOT_COLOR  = (200, 200, 160)
PELLET_COL = (255, 255, 150)
SCARED_COL = (50, 50, 200)
UI_COLOR   = (180, 160, 255)

# Vitesses
PLAYER_SPEED = 0.2
GHOST_SPEED  = 0.1         # réduit (était 0.5)
GHOST_SCARED_SPEED = 0.2
SCARED_DURATION = 300      # frames (~10s à 30fps)


def generate_maze_dfs():
    """Génère un labyrinthe style Pac-Man via DFS + ouvertures supplémentaires."""
    cols = MAZE_WIDTH  // 2
    rows = MAZE_HEIGHT // 2

    # Tout est mur au départ
    maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]

    visited = [[False] * cols for _ in range(rows)]

    def carve(r, c):
        visited[r][c] = True
        my = r * 2 + 1
        mx = c * 2 + 1
        maze[my][mx] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                wall_y = my + dr
                wall_x = mx + dc
                maze[wall_y][wall_x] = 0
                carve(nr, nc)

    carve(0, 0)

    # ── Étape 1 : Casser des murs supplémentaires pour créer des boucles ──
    # Plus le ratio est élevé, plus le labyrinthe est ouvert (0.0 = parfait, 1.0 = chaos)
    LOOP_RATIO = 0.30  # 30 % des murs intérieurs éligibles sont supprimés

    interior_walls = []
    for y in range(2, MAZE_HEIGHT - 2):
        for x in range(2, MAZE_WIDTH - 2):
            if maze[y][x] == 1:
                # Mur horizontal entre deux cellules libres (gauche/droite)
                if maze[y][x - 1] == 0 and maze[y][x + 1] == 0:
                    interior_walls.append((y, x))
                # Mur vertical entre deux cellules libres (haut/bas)
                elif maze[y - 1][x] == 0 and maze[y + 1][x] == 0:
                    interior_walls.append((y, x))

    random.shuffle(interior_walls)
    nb_to_remove = int(len(interior_walls) * LOOP_RATIO)
    for y, x in interior_walls[:nb_to_remove]:
        maze[y][x] = 0

    # ── Étape 2 : Ouvrir des grands couloirs horizontaux / verticaux ──
    # Crée 2-3 lignes et colonnes quasi-dégagées pour les grandes courses
    NB_CORRIDORS = 2

    # Couloirs horizontaux (une ligne sur deux pour rester dans la grille)
    h_candidates = [y for y in range(3, MAZE_HEIGHT - 3, 2)]
    random.shuffle(h_candidates)
    for y in h_candidates[:NB_CORRIDORS]:
        for x in range(1, MAZE_WIDTH - 1):
            # On ne touche pas aux blocs très isolés (évite de tout ouvrir)
            if maze[y][x] == 1:
                # Ouvre seulement si ça connecte des espaces existants
                if maze[y][x - 1] == 0 or maze[y][x + 1] == 0:
                    maze[y][x] = 0

    # Couloirs verticaux
    v_candidates = [x for x in range(3, MAZE_WIDTH - 3, 2)]
    random.shuffle(v_candidates)
    for x in v_candidates[:NB_CORRIDORS]:
        for y in range(1, MAZE_HEIGHT - 1):
            if maze[y][x] == 1:
                if maze[y - 1][x] == 0 or maze[y + 1][x] == 0:
                    maze[y][x] = 0

    # ── Étape 3 : Supprimer les culs-de-sac isolés (dead-ends) ──
    # Un cul-de-sac = cellule libre avec un seul voisin libre → on ouvre un mur adjacent
    DEAD_END_OPEN_PROB = 0.60  # Probabilité d'ouvrir chaque cul-de-sac

    def count_free_neighbors(y, x):
        return sum(
            1 for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]
            if 0 <= y+dy < MAZE_HEIGHT and 0 <= x+dx < MAZE_WIDTH
            and maze[y+dy][x+dx] == 0
        )

    for _ in range(2):  # 2 passes pour propager l'effet
        for y in range(1, MAZE_HEIGHT - 1):
            for x in range(1, MAZE_WIDTH - 1):
                if maze[y][x] == 0 and count_free_neighbors(y, x) == 1:
                    if random.random() < DEAD_END_OPEN_PROB:
                        # Cherche un mur adjacent ouvrable
                        walls = [
                            (y+dy, x+dx)
                            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]
                            if 0 < y+dy < MAZE_HEIGHT-1 and 0 < x+dx < MAZE_WIDTH-1
                            and maze[y+dy][x+dx] == 1
                        ]
                        if walls:
                            wy, wx = random.choice(walls)
                            maze[wy][wx] = 0

    # ── Bords extérieurs = murs (toujours) ──
    for x in range(MAZE_WIDTH):
        maze[0][x] = 1
        maze[MAZE_HEIGHT - 1][x] = 1
    for y in range(MAZE_HEIGHT):
        maze[y][0] = 1
        maze[y][MAZE_WIDTH - 1] = 1

    # ── Zone centrale vide (repaire des fantômes) ──
    cy, cx = MAZE_HEIGHT // 2, MAZE_WIDTH // 2
    for dy in range(-1, 2):
        for dx in range(-2, 3):
            maze[cy + dy][cx + dx] = 0

    # ── Place les points (2) sur les cellules libres ──
    for y in range(1, MAZE_HEIGHT - 1):
        for x in range(1, MAZE_WIDTH - 1):
            if maze[y][x] == 0:
                maze[y][x] = 2

    # ── Super-pastilles aux 4 coins accessibles ──
    corners = [
        (1, 1), (1, MAZE_WIDTH - 2),
        (MAZE_HEIGHT - 2, 1), (MAZE_HEIGHT - 2, MAZE_WIDTH - 2)
    ]
    for cy2, cx2 in corners:
        for r in range(3):
            found = False
            for dy in range(-r, r + 1):
                for dx in range(-r, r + 1):
                    ny, nx = cy2 + dy, cx2 + dx
                    if 0 <= ny < MAZE_HEIGHT and 0 <= nx < MAZE_WIDTH:
                        if maze[ny][nx] == 2:
                            maze[ny][nx] = 3
                            found = True
                            break
                if found:
                    break
            if found:
                break

    return maze


def find_free_cell(maze, exclude=None):
    """Retourne une position libre (pas mur) aléatoire."""
    exclude = exclude or []
    candidates = [
        (y, x)
        for y in range(1, MAZE_HEIGHT - 1)
        for x in range(1, MAZE_WIDTH - 1)
        if maze[y][x] in (0, 2, 3) and (y, x) not in exclude
    ]
    return random.choice(candidates) if candidates else (1, 1)


class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.speed = PLAYER_SPEED
        self.color = YELLOW
        self.direction = (0, 0)
        self.next_dir = (0, 0)
        self.mouth_angle = 45
        self.mouth_opening = True
        self.lives = 3

    def set_direction(self, dx, dy):
        self.next_dir = (dx, dy)

    def move(self, maze):
        # Essaie la prochaine direction demandée
        ndx, ndy = self.next_dir
        if ndx != 0 or ndy != 0:
            nx = self.x + ndx * self.speed
            ny = self.y + ndy * self.speed
            if (0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT
                    and maze[int(round(ny))][int(round(nx))] != 1):
                self.direction = self.next_dir

        dx, dy = self.direction
        if dx == 0 and dy == 0:
            return

        nx = self.x + dx * self.speed
        ny = self.y + dy * self.speed

        if (0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT
                and maze[int(round(ny))][int(round(nx))] != 1):
            self.x = nx
            self.y = ny
        else:
            # Bloqué → arrêt dans cette direction
            self.direction = (0, 0)

    def draw(self, screen):
        cx = int(self.x * CELL_SIZE + CELL_SIZE // 2) + MAZE_OFFSET_X
        cy = int(self.y * CELL_SIZE + CELL_SIZE // 2) + MAZE_OFFSET_Y
        r  = CELL_SIZE // 2 - 1
        pygame.draw.circle(screen, self.color, (cx, cy), r)
        


class Ghost:
    def __init__(self, x, y, color, name):
        self.x = float(x)
        self.y = float(y)
        self.color = color
        self.name = name
        self.speed = GHOST_SPEED
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.scared = False
        self.scared_timer = 0
        self.move_timer = 0
        self.move_interval = 1   # déplace toutes les N frames

    def scare(self):
        self.scared = True
        self.scared_timer = SCARED_DURATION

    def update_scared(self):
        if self.scared:
            self.scared_timer -= 1
            if self.scared_timer <= 0:
                self.scared = False

    def get_valid_dirs(self, maze):
        dirs = []
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = self.x + d[0] * self.speed * 2
            ny = self.y + d[1] * self.speed * 2
            if (0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT
                    and maze[int(round(ny))][int(round(nx))] != 1):
                dirs.append(d)
        return dirs

    def move(self, maze, player):
        self.move_timer += 1
        if self.move_timer < self.move_interval:
            return
        self.move_timer = 0

        spd = GHOST_SCARED_SPEED if self.scared else self.speed

        valid_dirs = self.get_valid_dirs(maze)
        if not valid_dirs:
            return

        # Évite de faire demi-tour sauf si bloqué
        opposite = (-self.direction[0], -self.direction[1])
        no_uturn = [d for d in valid_dirs if d != opposite]
        choices = no_uturn if no_uturn else valid_dirs

        if self.scared:
            # Fuit le joueur
            best = max(choices, key=lambda d: (
                (self.x + d[0] - player.x) ** 2 +
                (self.y + d[1] - player.y) ** 2
            ))
            if random.random() < 0.4:
                best = random.choice(choices)
            self.direction = best
        else:
            # 60% poursuite, 40% aléatoire
            if random.random() < 0.6:
                dx = player.x - self.x
                dy = player.y - self.y
                preferred = []
                if abs(dx) >= abs(dy):
                    preferred.append((1 if dx > 0 else -1, 0))
                    preferred.append((0, 1 if dy > 0 else -1))
                else:
                    preferred.append((0, 1 if dy > 0 else -1))
                    preferred.append((1 if dx > 0 else -1, 0))
                for p in preferred:
                    if p in choices:
                        self.direction = p
                        break
                else:
                    self.direction = random.choice(choices)
            else:
                self.direction = random.choice(choices)

        nx = self.x + self.direction[0] * spd
        ny = self.y + self.direction[1] * spd
        if (0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT
                and maze[int(round(ny))][int(round(nx))] != 1):
            self.x = nx
            self.y = ny
        else:
            valid = [d for d in valid_dirs if d != self.direction]
            if valid:
                self.direction = random.choice(valid)

    def draw(self, screen, frame):
        cx = int(self.x * CELL_SIZE + CELL_SIZE // 2) + MAZE_OFFSET_X
        cy = int(self.y * CELL_SIZE + CELL_SIZE // 2) + MAZE_OFFSET_Y
        r  = CELL_SIZE // 2 - 1

        if self.scared:
            # Clignote quand le temps est presque écoulé
            if self.scared_timer < 80 and (frame // 10) % 2 == 0:
                color = WHITE
            else:
                color = SCARED_COL
        else:
            color = self.color

        # Corps principal
        body_rect = pygame.Rect(cx - r, cy - r, r * 2, r * 2)
        pygame.draw.circle(screen, color, (cx, cy - 1), r)
        


def draw_maze(screen, maze, frame):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            rx = x * CELL_SIZE + MAZE_OFFSET_X
            ry = y * CELL_SIZE + MAZE_OFFSET_Y

            if maze[y][x] == 1:  # Mur
                pygame.draw.rect(screen, BLUE_WALL,
                                 (rx, ry, CELL_SIZE, CELL_SIZE))
                # Contour lumineux
                pygame.draw.rect(screen, BLUE_WALL2,
                                 (rx, ry, CELL_SIZE, CELL_SIZE), 1)
            elif maze[y][x] == 2:  # Point
                pygame.draw.circle(screen, DOT_COLOR,
                                   (rx + CELL_SIZE // 2, ry + CELL_SIZE // 2), 2)
            elif maze[y][x] == 3:  # Super-pastille (pulsante)
                pulse = 4 + int(2 * abs((frame % 40) / 20 - 1))
                pygame.draw.circle(screen, PELLET_COL,
                                   (rx + CELL_SIZE // 2, ry + CELL_SIZE // 2), pulse)


def draw_hud(screen, font, font_sm, score, high_score, lives, level):
    # Barre supérieure
    pygame.draw.rect(screen, (20, 20, 50), (0, 0, SCREEN_WIDTH, MAZE_OFFSET_Y - 4))

    title = font.render("PAC-MAN", True, YELLOW)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 8))

    sc_txt = font_sm.render(f"SCORE: {score}", True, UI_COLOR)
    screen.blit(sc_txt, (10, 10))

    hi_txt = font_sm.render(f"HI: {high_score}", True, ORANGE)
    screen.blit(hi_txt, (10, 32))

    lv_txt = font_sm.render(f"LVL {level}", True, CYAN)
    screen.blit(lv_txt, (SCREEN_WIDTH - 80, 10))

    # Vies (petits pacmans)
    for i in range(lives):
        lx = SCREEN_WIDTH - 80 + i * 22
        pygame.draw.circle(screen, YELLOW, (lx, 38), 7)
        pygame.draw.polygon(screen, DARK_BG, [(lx, 38), (lx + 7, 31), (lx + 7, 45)])


def reset_game(level=1):
    maze = generate_maze_dfs()

    # Spawn joueur : cellule libre proche du centre-bas
    py, px = MAZE_HEIGHT - 3, MAZE_WIDTH // 2
    while maze[py][px] == 1:
        px += 1

    used = [(py, px)]
    player = Player(px, py)
    maze[py][px] = 0  # pas de point sous le joueur au départ

    # Spawn fantômes : coins ou positions aléatoires
    ghost_data = [
        (RED,    "Blinky"),
        (PINK,   "Pinky"),
        (CYAN,   "Inky"),
        (ORANGE, "Clyde"),
    ]
    ghosts = []
    for color, name in ghost_data:
        gy, gx = find_free_cell(maze, exclude=used)
        used.append((gy, gx))
        g = Ghost(gx, gy, color, name)
        # Vitesse croissante avec le niveau
        g.speed = min(GHOST_SPEED + (level - 1) * 0.05, 0.8)
        ghosts.append(g)

    return maze, player, ghosts


import math

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PAC-MAN")
    clock = pygame.time.Clock()

    font    = pygame.font.SysFont("couriernew", 28, bold=True)
    font_sm = pygame.font.SysFont("couriernew", 20)
    font_lg = pygame.font.SysFont("couriernew", 42, bold=True)

    level      = 1
    high_score = 0
    score      = 0
    game_over  = False
    win        = False
    frame      = 0

    maze, player, ghosts = reset_game(level)

    while True:
        dt = clock.tick(30)
        frame += 1

        # ── EVENTS ──────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Restart fonctionne toujours avec R
                if event.key == K_r:
                    level      = 1
                    score      = 0
                    game_over  = False
                    win        = False
                    maze, player, ghosts = reset_game(level)
                    continue

                if not game_over and not win:
                    if event.key in (K_UP,    K_z, K_w): player.set_direction( 0, -1)
                    elif event.key in (K_DOWN,  K_s):    player.set_direction( 0,  1)
                    elif event.key in (K_LEFT,  K_q, K_a): player.set_direction(-1, 0)
                    elif event.key in (K_RIGHT, K_d):    player.set_direction( 1, 0)

        # ── LOGIQUE ─────────────────────────────────────────────
        if not game_over and not win:
            player.move(maze)

            px, py = int(round(player.x)), int(round(player.y))
            px = max(0, min(px, MAZE_WIDTH - 1))
            py = max(0, min(py, MAZE_HEIGHT - 1))

            # Mange un point
            if maze[py][px] == 2:
                maze[py][px] = 0
                score += 10

            # Mange une super-pastille
            elif maze[py][px] == 3:
                maze[py][px] = 0
                score += 50
                for g in ghosts:
                    g.scare()

            # Déplace les fantômes
            for ghost in ghosts:
                ghost.update_scared()
                ghost.move(maze, player)

                # Collision joueur-fantôme
                if (abs(ghost.x - player.x) < 0.8 and
                        abs(ghost.y - player.y) < 0.8):
                    if ghost.scared:
                        # Mange le fantôme
                        score += 200
                        gy, gx = find_free_cell(maze)
                        ghost.x, ghost.y = float(gx), float(gy)
                        ghost.scared = False
                    else:
                        player.lives -= 1
                        if player.lives <= 0:
                            game_over = True
                        else:
                            # Respawn joueur
                            ry, rx = MAZE_HEIGHT - 3, MAZE_WIDTH // 2
                            while maze[ry][rx] == 1:
                                rx += 1
                            player.x, player.y = float(rx), float(ry)
                            player.direction = (0, 0)

            # Victoire : plus de points
            remaining = sum(row.count(2) + row.count(3) for row in maze)
            if remaining == 0:
                win = True
                high_score = max(high_score, score)

            high_score = max(high_score, score)

        # ── DESSIN ──────────────────────────────────────────────
        screen.fill(DARK_BG)
        draw_maze(screen, maze, frame)
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen, frame)
        draw_hud(screen, font, font_sm, score, high_score, player.lives, level)

        # Overlay game over / win
        if game_over or win:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))

            if win:
                msg  = font_lg.render("YOU WIN!", True, YELLOW)
                msg2 = font_sm.render(f"Score: {score}   —   Appuyez sur R pour rejouer", True, WHITE)
            else:
                msg  = font_lg.render("GAME OVER", True, RED)
                msg2 = font_sm.render("Appuyez sur R pour recommencer", True, WHITE)

            screen.blit(msg,  (SCREEN_WIDTH // 2 - msg.get_width()  // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(msg2, (SCREEN_WIDTH // 2 - msg2.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
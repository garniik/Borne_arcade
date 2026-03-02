#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import sys

import pygame

from config import *


pygame.init()
pygame.mixer.init()


class Paddle:
    def __init__(self, screen_w: int, screen_h: int):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.width = int(screen_w * PADDLE_WIDTH_RATIO)
        self.height = PADDLE_HEIGHT
        self.speed = screen_w * PADDLE_SPEED_RATIO
        self.rect = pygame.Rect(
            (screen_w - self.width) // 2,
            int(screen_h * 0.88),
            self.width,
            self.height,
        )

    def update(self, dt: float, move_dir: float):
        self.rect.x += int(move_dir * self.speed * dt)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_w:
            self.rect.right = self.screen_w

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, WHITE, self.rect, border_radius=6)


class Ball:
    def __init__(self, screen_w: int, screen_h: int):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.radius = BALL_RADIUS
        self.base_speed = screen_w * BALL_SPEED_RATIO
        self.reset((screen_w // 2, int(screen_h * 0.70)))

    def reset(self, center):
        self.pos = pygame.Vector2(center[0], center[1])
        self.vel = pygame.Vector2(0, 0)

    def launch(self):
        angle = random.uniform(-0.85 * math.pi / 2, -0.15 * math.pi / 2)
        self.vel = pygame.Vector2(math.cos(angle), math.sin(angle)) * self.base_speed

    def update(self, dt: float):
        self.pos += self.vel * dt

    @property
    def rect(self):
        return pygame.Rect(
            int(self.pos.x - self.radius),
            int(self.pos.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, CYAN, (int(self.pos.x), int(self.pos.y)), self.radius)


class BreakoutGame:
    def __init__(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT

        if FULLSCREEN:
            info = pygame.display.Info()
            self.screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
            SCREEN_WIDTH = info.current_w
            SCREEN_HEIGHT = info.current_h
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Calibri", 28)
        self.font_big = pygame.font.SysFont("Calibri", 48, bold=True)

        self.screen_w = SCREEN_WIDTH
        self.screen_h = SCREEN_HEIGHT

        self.running = True
        self.paused = False

        self.reset_game()

    def reset_game(self):
        self.paddle = Paddle(self.screen_w, self.screen_h)
        self.ball = Ball(self.screen_w, self.screen_h)
        self.lives = LIVES_START
        self.score = 0
        self.state = "ready"  # ready | playing | life_lost | win | game_over
        self._create_bricks()
        self._stick_ball_to_paddle()

    def _create_bricks(self):
        self.bricks = []

        usable_w = self.screen_w - 2 * BRICK_SIDE_MARGIN
        total_gap = (BRICK_COLS - 1) * BRICK_GAP
        brick_w = int((usable_w - total_gap) / BRICK_COLS)
        brick_h = 26

        colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE]

        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = BRICK_SIDE_MARGIN + col * (brick_w + BRICK_GAP)
                y = BRICK_TOP_MARGIN + row * (brick_h + BRICK_GAP)
                rect = pygame.Rect(x, y, brick_w, brick_h)
                hp = 1
                color = colors[row % len(colors)]
                self.bricks.append({"rect": rect, "hp": hp, "color": color})

    def _stick_ball_to_paddle(self):
        self.ball.reset((self.paddle.rect.centerx, self.paddle.rect.top - self.ball.radius - 1))
        self.ball.vel.update(0, 0)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_ESCAPE, pygame.K_f):
            self.running = False
            return

        if event.key in (pygame.K_h,):
            self.paused = not self.paused
            return

        if event.key in (pygame.K_r,) and self.state in ("game_over", "win"):
            self.reset_game()
            return

        if event.key in (pygame.K_r, pygame.K_g, pygame.K_RETURN, pygame.K_SPACE):
            if self.state in ("ready", "life_lost"):
                self.ball.launch()
                self.state = "playing"

    def _paddle_input_dir(self):
        keys = pygame.key.get_pressed()
        move = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            move -= 1.0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move += 1.0
        return move

    def _ball_wall_collisions(self):
        if self.ball.pos.x - self.ball.radius <= 0:
            self.ball.pos.x = self.ball.radius
            self.ball.vel.x *= -1
        elif self.ball.pos.x + self.ball.radius >= self.screen_w:
            self.ball.pos.x = self.screen_w - self.ball.radius
            self.ball.vel.x *= -1

        if self.ball.pos.y - self.ball.radius <= 0:
            self.ball.pos.y = self.ball.radius
            self.ball.vel.y *= -1

    def _ball_paddle_collision(self):
        if not self.ball.rect.colliderect(self.paddle.rect):
            return

        if self.ball.vel.y > 0:
            self.ball.pos.y = self.paddle.rect.top - self.ball.radius - 1
            self.ball.vel.y *= -1

            hit = (self.ball.pos.x - self.paddle.rect.centerx) / (self.paddle.rect.width / 2)
            hit = max(-1.0, min(1.0, hit))

            speed = self.ball.vel.length()
            angle = hit * (0.75 * math.pi / 2)
            self.ball.vel.x = math.sin(angle) * speed
            self.ball.vel.y = -abs(math.cos(angle) * speed)

    def _ball_brick_collision(self):
        ball_rect = self.ball.rect

        for brick in self.bricks:
            rect = brick["rect"]
            if not ball_rect.colliderect(rect):
                continue

            overlap_left = ball_rect.right - rect.left
            overlap_right = rect.right - ball_rect.left
            overlap_top = ball_rect.bottom - rect.top
            overlap_bottom = rect.bottom - ball_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                self.ball.pos.x -= overlap_left
                self.ball.vel.x *= -1
            elif min_overlap == overlap_right:
                self.ball.pos.x += overlap_right
                self.ball.vel.x *= -1
            elif min_overlap == overlap_top:
                self.ball.pos.y -= overlap_top
                self.ball.vel.y *= -1
            else:
                self.ball.pos.y += overlap_bottom
                self.ball.vel.y *= -1

            brick["hp"] -= 1
            if brick["hp"] <= 0:
                self.bricks.remove(brick)
                self.score += 10

            break

    def update(self, dt: float):
        if self.paused:
            return

        move_dir = self._paddle_input_dir()
        self.paddle.update(dt, move_dir)

        if self.state in ("ready", "life_lost"):
            self._stick_ball_to_paddle()
            return

        if self.state != "playing":
            return

        self.ball.update(dt)
        self._ball_wall_collisions()
        self._ball_paddle_collision()
        self._ball_brick_collision()

        if self.ball.pos.y - self.ball.radius > self.screen_h:
            self.lives -= 1
            if self.lives <= 0:
                self.state = "game_over"
            else:
                self.state = "life_lost"
                self._stick_ball_to_paddle()

        if not self.bricks and self.state == "playing":
            self.state = "win"

    def _draw_hud(self):
        lives_text = self.font.render(f"Vies: {self.lives}", True, WHITE)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(lives_text, (20, 20))
        self.screen.blit(score_text, (20, 55))

        help_text = self.font.render("Gauche/Droite: déplacer | G/R/ESPACE: lancer | H: pause | F/ESC: quitter", True, GRAY)
        self.screen.blit(help_text, (20, self.screen_h - 40))

    def _draw_center_message(self, title: str, subtitle: str):
        title_surf = self.font_big.render(title, True, WHITE)
        sub_surf = self.font.render(subtitle, True, GRAY)
        title_rect = title_surf.get_rect(center=(self.screen_w // 2, self.screen_h // 2 - 30))
        sub_rect = sub_surf.get_rect(center=(self.screen_w // 2, self.screen_h // 2 + 20))
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(sub_surf, sub_rect)

    def draw(self):
        self.screen.fill(BLACK)

        for brick in self.bricks:
            pygame.draw.rect(self.screen, brick["color"], brick["rect"], border_radius=5)

        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self._draw_hud()

        if self.paused:
            self._draw_center_message("PAUSE", "Appuie sur H pour reprendre")
        elif self.state == "ready":
            self._draw_center_message("BREAKOUT", "Appuie sur G / R / ESPACE pour lancer")
        elif self.state == "life_lost":
            self._draw_center_message("PERDU UNE VIE", "Appuie sur G / R / ESPACE pour relancer")
        elif self.state == "game_over":
            self._draw_center_message("GAME OVER", "Appuie sur R pour rejouer")
        elif self.state == "win":
            self._draw_center_message("VICTOIRE !", "Appuie sur R pour rejouer")

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                self.handle_event(event)

            self.update(dt)
            self.draw()


if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
    pygame.quit()
    sys.exit()

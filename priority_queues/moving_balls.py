import random
import time

import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 400


class Ball():

    def __init__(self, px, py, vx, vy, r):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.r = r

    def move(self, t):
        if self.px + self.vx * t < self.r or self.px + self.vx * t + self.r > HEIGHT:
            self.vx = -self.vx
        if self.py + self.vy * t < self.r or self.py + self.vy * t + self.r > HEIGHT:
            self.vy = -self.vy
        self.px += self.vx * t
        self.py += self.vy * t


def handle(event):
    if event.type == QUIT:
        pygame.quit()
        quit()


if __name__ == '__main__':
    # TODO: Handle particles crashing with each other using priority queues

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()
    ball_color = (0, 0, 0)

    n = int(input('Enter amount of balls: '))

    balls = [Ball(px=random.randrange(0, HEIGHT), py=random.randrange(
        0, WIDTH), vx=10, vy=10, r=5) for _ in range(n)]

    while True:
        for event in pygame.event.get():
            handle(event)
        game_display.fill((255, 255, 255))
        for i in range(n):
            balls[i].move(0.5)
            pygame.draw.circle(game_display, ball_color,
                               (balls[i].px, balls[i].py), balls[i].r)
        pygame.display.update()
        time.sleep(0.01)

import random
import sys
import time

import pygame
from pygame.locals import QUIT

WIDTH = 400
HEIGHT = 400


class Ball():

    def __init__(self, pos_x, pos_y, vel_x, vel_y, radius):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius

    def move(self, dir_vect):
        if self.pos_x + self.vel_x * dir_vect < self.radius or self.pos_x + self.vel_x * dir_vect + self.radius > HEIGHT:
            self.vel_x = -self.vel_x
        if self.pos_y + self.vel_y * dir_vect < self.radius or self.pos_y + self.vel_y * dir_vect + self.radius > HEIGHT:
            self.vel_y = -self.vel_y
        self.pos_x += self.vel_x * dir_vect
        self.pos_y += self.vel_y * dir_vect


def handle(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    # TODO: Handle particles crashing with each other using priority queues

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()
    ball_color = (0, 0, 0)

    n = int(input('Enter amount of balls: '))

    balls = [Ball(pos_x=random.randrange(0, HEIGHT), pos_y=random.randrange(
        0, WIDTH), vel_x=10, vel_y=10, radius=5) for _ in range(n)]

    while True:
        for game_event in pygame.event.get():
            handle(game_event)
        game_display.fill((255, 255, 255))
        for i in range(n):
            balls[i].move(0.5)
            pygame.draw.circle(game_display, ball_color,
                               (balls[i].pos_x, balls[i].pos_y), balls[i].radius)
        pygame.display.update()
        time.sleep(0.01)

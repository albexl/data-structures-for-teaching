import random
import time

import pygame
from pygame.locals import *
from implementation import WeightedQuickUnion

WIDTH = 700
HEIGHT = 700


def map(pos, n):
    return (pos // n, pos % n)


def rmap(x, y, n):
    return x * n + y


def valid(x, y, n):
    return min(x, y) >= 0 and max(x, y) < n


def handle(event):
    if event.type == QUIT:
        pygame.quit()
        quit()


def draw(n, union_find, active):
    white_color = (255, 255, 255)
    blue_color = (0, 0, 255)
    black_color = (0, 0, 0)
    game_display.fill(black_color)

    for i in range(n):
        for j in range(n):
            pos = rmap(i, j, n)
            if active[pos]:
                rect = pygame.Rect(j * (HEIGHT // n), i *
                                   (HEIGHT // n), HEIGHT // n, HEIGHT // n)
                pygame.draw.rect(game_display, blue_color if union_find.connected(
                    n**2, pos) else white_color, rect)

    for i in range(n):
        pygame.draw.line(game_display, black_color,
                         (i * (HEIGHT // n), 0), (i * (HEIGHT // n), WIDTH), width=3)

    for i in range(n):
        pygame.draw.line(game_display, black_color,
                         (0, i * (WIDTH // n)), (HEIGHT, i * (WIDTH // n)), width=3)

    pygame.display.update()


if __name__ == '__main__':

    trials = int(input('Enter amount of trials: '))

    input_sizes = [random.randint(1, 50) for _ in range(trials)]

    sum = 0

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()
    game_display.fill((0, 0, 0))

    for n in input_sizes:

        print('Solving for input size: {0}'.format(n))

        union_find = WeightedQuickUnion(n**2 + 2)
        population = [i for i in range(n**2)]
        active = [False for _ in range(n**2)]
        random.shuffle(population)

        for i in range(n):
            union_find.union(n**2, rmap(0, i, n))
            union_find.union(n**2 + 1, rmap(n - 1, i, n))

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        count = 0
        for pos in population:
            count += 1
            x, y = map(pos, n)
            active[pos] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid(nx, ny, n) and active[rmap(nx, ny, n)]:
                    union_find.union(pos, rmap(nx, ny, n))

            for event in pygame.event.get():
                handle(event)
            draw(n, union_find, active)

            if union_find.connected(n**2, n**2 + 1):
                sum += count / n**2
                break

    print('Percolation threshold: {0}'.format(sum / trials))

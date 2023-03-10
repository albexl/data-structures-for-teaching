import random
import sys
import time

import pygame
from pygame.locals import QUIT

from .implementation import WeightedQuickUnion

WIDTH = 700
HEIGHT = 700


def map_pos(pos, board_size):
    return (pos // board_size, pos % board_size)


def reverse_map(x_cord, y_cord, board_size):
    return x_cord * board_size + y_cord


def valid(x_cord, y_cord, board_size):
    return min(x_cord, y_cord) >= 0 and max(x_cord, y_cord) < board_size


def handle(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()


def draw(size, disjoint_sets, active):
    white_color = (255, 255, 255)
    blue_color = (0, 0, 255)
    black_color = (0, 0, 0)
    game_display.fill(black_color)

    for row in range(size):
        for col in range(size):
            pos = reverse_map(row, col, size)
            if active[pos]:
                rect = pygame.Rect(
                    col * (HEIGHT // size),
                    row * (HEIGHT // size),
                    HEIGHT // size,
                    HEIGHT // size,
                )
                pygame.draw.rect(
                    game_display,
                    blue_color
                    if disjoint_sets.connected(size**2, pos)
                    else white_color,
                    rect,
                )

    for row in range(size):
        pygame.draw.line(
            game_display,
            black_color,
            (row * (HEIGHT // size), 0),
            (row * (HEIGHT // size), WIDTH),
            width=3,
        )

    for col in range(size):
        pygame.draw.line(
            game_display,
            black_color,
            (0, col * (WIDTH // size)),
            (HEIGHT, col * (WIDTH // size)),
            width=3,
        )

    pygame.display.update()


if __name__ == "__main__":

    trials = int(input("Enter amount of trials: "))

    input_sizes = [random.randint(1, 50) for _ in range(trials)]

    total = 0.0

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()
    game_display.fill((0, 0, 0))

    for input_size in input_sizes:

        print(f"Solving for input size: {input_size}")

        union_find = WeightedQuickUnion(input_size**2 + 2)
        population = list(range(input_size**2))
        active_pos = [False for _ in range(input_size**2)]
        random.shuffle(population)

        for i in range(input_size):
            union_find.union(input_size**2, reverse_map(0, i, input_size))
            union_find.union(
                input_size**2 + 1, reverse_map(input_size - 1, i, input_size)
            )

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        count = 0
        for position in population:
            count += 1
            x, y = map_pos(position, input_size)
            active_pos[position] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    valid(nx, ny, input_size)
                    and active_pos[reverse_map(nx, ny, input_size)]
                ):
                    union_find.union(position, reverse_map(nx, ny, input_size))

            for game_event in pygame.event.get():
                handle(game_event)
            draw(input_size, union_find, active_pos)

            if union_find.connected(input_size**2, input_size**2 + 1):
                total += count / input_size**2
                time.sleep(1)
                break

    print(f"Percolation threshold: {total / trials}")

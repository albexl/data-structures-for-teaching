"""Simulation of a Tower Defense-like game movements."""


import random
import sys
import time
from queue import Queue
from typing import List, Tuple

import pygame
from pygame.locals import QUIT

WIDTH = 630
HEIGHT = 630
MAX_ORIGINS = 30


def setup(size: int) -> Tuple[List[List[bool]], Tuple[int, int], List[Tuple[int, int]]]:
    """Sets up the board game. Generates random locations
    for origins and destination.

    Args:
        size (int): Size of the board.

    Returns:
        Tuple[List[List[bool]], Tuple[int, int], List[Tuple[int, int]]]: Board game, destination location, origin locations.
    """
    obstacles = min(size**2, random.randint(2 * size, 3 * size))
    board = [[False] * size for _ in range(size)]

    population = []
    for i in range(size):
        for j in range(size):
            population.append((i, j))

    random.shuffle(population)
    for i in range(obstacles):
        board[population[i][0]][population[i][1]] = True

    population = []
    for i in range(size):
        for j in range(size):
            if not board[i][j]:
                population.append((i, j))

    random.shuffle(population)
    destination = population[0]

    origin_size = min(len(population) - 1, MAX_ORIGINS)
    origins = []
    for i in range(1, origin_size):
        origins.append(population[i])

    return (board, destination, origins)


def _draw(board, destination, origins):

    black_color = (0, 0, 0)
    grey_color = (105, 105, 105)
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    game_display.fill(white_color)

    size = len(board)

    for i in range(size):
        for j in range(size):
            rect = pygame.Rect(
                j * (HEIGHT // size),
                i * (HEIGHT // size),
                HEIGHT // size,
                HEIGHT // size,
            )
            pygame.draw.rect(
                game_display, black_color if board[i][j] else white_color, rect
            )

            if destination == (i, j):
                pygame.draw.rect(game_display, green_color, rect)

            if (i, j) in origins:
                pygame.draw.rect(game_display, red_color, rect)

    for i in range(size + 1):
        pygame.draw.line(
            game_display,
            grey_color,
            (i * (HEIGHT // size), 0),
            (i * (HEIGHT // size), WIDTH),
            width=1,
        )

    for i in range(size + 1):
        pygame.draw.line(
            game_display,
            grey_color,
            (0, i * (WIDTH // size)),
            (HEIGHT, i * (WIDTH // size)),
            width=1,
        )

    pygame.display.update()


def _handle_events(board, destination, origins, size):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            i = pos[1] // (HEIGHT // size)
            j = pos[0] // (HEIGHT // size)

            if event.button == 3 and not board[i][j]:
                destination = (i, j)
            elif event.button == 1 and (i, j) != destination and (i, j) not in origins:
                board[i][j] = not board[i][j]

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    return destination


def _valid(x_coord, y_coord, size):
    return min(x_coord, y_coord) >= 0 and max(x_coord, y_coord) < size


def _bfs(board, destination, size):
    queue = Queue()
    queue.put(destination)
    distances = [[-1] * size for _ in range(size)]
    distances[destination[0]][destination[1]] = 0

    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]

    while not queue.empty():
        x_coord, y_coord = queue.get()
        for i in range(4):
            new_x = x_coord + dir_x[i]
            new_y = y_coord + dir_y[i]
            if (
                _valid(new_x, new_y, size)
                and (not board[new_x][new_y])
                and distances[new_x][new_y] == -1
            ):
                distances[new_x][new_y] = distances[x_coord][y_coord] + 1
                queue.put((new_x, new_y))

    return distances


def _update(board, destination, origins, distances, size):
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]

    updated_origins = []
    for (x_coord, y_coord) in origins:
        if distances[x_coord][y_coord] == -1:
            continue

        next_move, min_dist = (-1, -1), size**2
        for i in range(4):
            new_x = x_coord + dir_x[i]
            new_y = y_coord + dir_y[i]
            if _valid(new_x, new_y, size) and not board[new_x][new_y]:
                if distances[new_x][new_y] < min_dist:
                    next_move, min_dist = (new_x, new_y), distances[new_x][new_y]
        updated_origins.append(next_move)

    origins = []
    for pos in updated_origins:
        if pos != destination:
            origins.append(pos)

    population = []
    for i in range(size):
        for j in range(size):
            if not board[i][j] and (i, j) != destination and (i, j) not in origins:
                population.append((i, j))

    random.shuffle(population)
    idx = 0
    while len(origins) < MAX_ORIGINS and idx < len(population):
        origins.append(population[idx])
        idx += 1

    return origins


def simulate(
    board: List[List[bool]],
    destination: Tuple[int, int],
    origins: List[Tuple[int, int]],
    size: int,
):
    """Simulate the movements of a Tower Defense-like game.

    Args:
        board (List[List[bool]]): The game board.
        destination (Tuple[int, int]): Destination location.
        origins (List[Tuple[int, int]]): Origin locations.
        size (int): Size of the board.
    """
    while True:
        time.sleep(0.1)
        _draw(board, destination, origins)
        destination = _handle_events(board, destination, origins, size)
        distances = _bfs(board, destination, size)
        origins = _update(board, destination, origins, distances, size)


if __name__ == "__main__":
    board_size = int(input("Enter dimension of the system: "))
    game_board, dest_location, origin_locations = setup(board_size)

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()

    simulate(game_board, dest_location, origin_locations, board_size)

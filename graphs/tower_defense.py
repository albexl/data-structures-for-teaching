import random
import time

from queue import Queue

import pygame
from pygame.locals import *

WIDTH = 630
HEIGHT = 630
MAX_ORIGINS = 30


def setup(n):
    obstacles = min(n**2, random.randint(2 * n, 3 * n))
    board = [[False] * n for _ in range(n)]

    population = []
    for i in range(n):
        for j in range(n):
            population.append((i, j))

    random.shuffle(population)
    for i in range(obstacles):
        board[population[i][0]][population[i][1]] = True

    population = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                population.append((i, j))

    random.shuffle(population)
    destination = population[0]

    m = min(len(population) - 1, MAX_ORIGINS)
    origins = []
    for i in range(1, m):
        origins.append(population[i])

    return (board, destination, origins)


def draw(board, destination, origins):

    black_color = (0, 0, 0)
    grey_color = (105, 105, 105)
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    game_display.fill(white_color)

    n = len(board)

    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(j * (HEIGHT // n), i *
                               (HEIGHT // n), HEIGHT // n, HEIGHT // n)
            pygame.draw.rect(
                game_display, black_color if board[i][j] else white_color, rect)

            if destination == (i, j):
                pygame.draw.rect(game_display, green_color, rect)

            if (i, j) in origins:
                pygame.draw.rect(game_display, red_color, rect)

    for i in range(n + 1):
        pygame.draw.line(game_display, grey_color,
                         (i * (HEIGHT // n), 0), (i * (HEIGHT // n), WIDTH), width=1)

    for i in range(n + 1):
        pygame.draw.line(game_display, grey_color,
                         (0, i * (WIDTH // n)), (HEIGHT, i * (WIDTH // n)), width=1)

    pygame.display.update()


def handle_events(board, destination, origins, n):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            i = pos[1] // (HEIGHT // n)
            j = pos[0] // (HEIGHT // n)

            if event.button == 3 and not board[i][j]:
                destination = (i, j)
            elif event.button == 1 and (i, j) != destination and (i, j) not in origins:
                board[i][j] = not board[i][j]

        if event.type == QUIT:
            pygame.quit()
            quit()

    return destination


def valid(x, y, n):
    return min(x, y) >= 0 and max(x, y) < n


def bfs(board, destination, n):
    q = Queue()
    q.put(destination)
    distances = [[-1] * n for _ in range(n)]
    distances[destination[0]][destination[1]] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if valid(nx, ny, n) and (not board[nx][ny]) and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                q.put((nx, ny))

    return distances


def update(board, destination, origins, distances, n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    updated_origins = []
    for (x, y) in origins:
        if distances[x][y] == -1:
            continue

        next_move, min_dist = (-1, -1), n**2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if valid(nx, ny, n) and not board[nx][ny]:
                if distances[nx][ny] < min_dist:
                    next_move, min_dist = (nx, ny), distances[nx][ny]
        updated_origins.append(next_move)

    origins = []
    for pos in updated_origins:
        if pos != destination:
            origins.append(pos)

    population = []
    for i in range(n):
        for j in range(n):
            if not board[i][j] and (i, j) != destination and not (i, j) in origins:
                population.append((i, j))

    random.shuffle(population)
    idx = 0
    while len(origins) < MAX_ORIGINS and idx < len(population):
        origins.append(population[idx])
        idx += 1

    return origins


def simulate(board, destination, origins, n):
    while True:
        time.sleep(0.1)
        draw(board, destination, origins)
        destination = handle_events(board, destination, origins, n)
        distances = bfs(board, destination, n)
        origins = update(board, destination, origins, distances, n)


if __name__ == '__main__':
    n = int(input('Enter dimension of the system: '))
    board, destination, origins = setup(n)

    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()

    simulate(board, destination, origins, n)

import pygame
import numpy as np
from io import StringIO

zoom = 10


def draw_frame(screen, data):
    screen.fill((0, 0, 0))
    if np.count_nonzero(data > 0) == 0:
        return

    for x, y in np.nditer(np.where(data > 0)):
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(y * zoom, x * zoom, zoom, zoom))

    pygame.display.flip()


def game(data):
    pygame.init()

    done = False
    screen = pygame.display.set_mode((zoom * data.shape[1], zoom * data.shape[0]))

    while not done:
        pygame.time.delay(25)
        draw_frame(screen, data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


def day13():
    with open('day13.txt') as data:
        coords, folds = data.read().split('\n\n')
        folds = folds.splitlines()
        max_x = 0
        max_y = 0
        for fold in folds:
            if max_x > 0 and max_y > 0:
                break
            left, r = fold.split('=')
            if left.endswith('x') and max_x == 0:
                max_x = int(r) * 2 + 1
            if left.endswith('y') and max_y == 0:
                max_y = int(r) * 2 + 1

        coord_data = np.loadtxt(StringIO(coords), delimiter=',', dtype=int)
        data = np.zeros((max_x, max_y))
        for (x, y) in coord_data:
            data[x, y] = 1

        for fold in folds:
            print(fold)
            left, r = fold.split('=')
            if left.endswith('x'):
                x = int(r)
                left_part = data[0:x, :]
                right_part = data[x+1:, :]
                data = left_part + np.flip(right_part, axis=0)

            elif left.endswith('y'):
                y = int(r)
                top_part = data[:, 0:y]
                bottom_part = data[:, y+1:]
                data = top_part + np.flip(bottom_part, axis=1)

        print(np.count_nonzero(data))
        data = np.flip(np.rot90(data), axis=0)
        game(data)


if __name__ == '__main__':
    day13()



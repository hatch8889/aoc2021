import numpy as np
import pygame

zoom = 50


def get_color(i):
    return i*20, i*20, i*20


def paint(screen, data, i):
    screen.fill((0, 0, 0))

    if np.count_nonzero(data > 0) == 0:
        return

    for x, y in np.nditer(np.where(data > 0)):
        pygame.draw.rect(screen, get_color(data[x, y]), pygame.Rect(y * zoom, x * zoom, zoom, zoom))

    font = pygame.font.Font(None, 80)
    text = font.render(f"{i}", True, (200, 55, 20))
    tt = zoom * 10 - text.get_height() - 10
    screen.blit(text, (10, tt))

    pygame.display.flip()
    pygame.time.delay(250)


def day10():
    pygame.init()
    screen = pygame.display.set_mode((zoom*10, zoom*10))
    done = False
    pygame.display.flip()

    def get_data():
        return np.loadtxt('day11.txt', dtype=(int, int), converters={0: list}, encoding='latin1')

    data = get_data()
    all_flashes = 0

    def pos(n):
        return n if n >= 0 else 0

    i = 0
    while not done:
        i = i + 1
        data += 1
        while True:
            if np.count_nonzero(data >= 10):
                ii = list(np.nditer(np.where(data >= 10)))
                for x, y in ii:
                    sub_matrix = data[pos(x-1):x+2, pos(y-1):y+2]
                    sub_matrix += 1
                    data[x, y] = 0
                    sub_matrix[sub_matrix == 1] = 0
            else:
                break

        paint(screen, data, i)

        f = np.count_nonzero(data == 0)
        all_flashes += f
        if i == 100:
            print(f"part1: {all_flashes}")

        if f == 100:
            i = 0
            print(f"part2: {i}")
            data = get_data()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == '__main__':
    day10()

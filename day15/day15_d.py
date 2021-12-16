import numpy as np

import pygame

zoom = 7


def get_color(i):
    r = 0
    g = 0
    b = 0
    if i < 256:
        r = i
    elif i < 512:
        r = 255
        g = i - 256
    else:
        r = 255
        g = 255
        b = i % 255
    return r, g, b


def paint(nodes):
    pygame.init()
    screen = pygame.display.set_mode((zoom * 100, zoom*100))

    for coord in nodes.keys():
        color = get_color(nodes[coord])
        x = int(coord[0])
        y = int(coord[1])
        pygame.draw.rect(screen, color, pygame.Rect(y * zoom, x * zoom, zoom, zoom))

    pygame.display.flip()

    done = False
    while not done:
        for event in pygame.event.get():
            pygame.time.delay(100)
            if event.type == pygame.QUIT:
                done = True


def neighbours(data, node):
    ns = []
    x, y = node
    if x > 0:
        ns.append((x - 1, y))
    if y > 0:
        ns.append((x, y - 1))
    if x + 1 < data.shape[0]:
        ns.append((x + 1, y))
    if y + 1 < data.shape[1]:
        ns.append((x, y + 1))
    return ns


def shortest_path(data):
    priority_queue = [(0, (0, 0))]
    prev = {(0, 0): 0}
    visited = []

    while len(priority_queue) > 0:
        cost, node = priority_queue.pop()
        if visited.count(node) > 0:
            continue
        visited.append(node)

        for neighbour in neighbours(data, node):
            new_cost = cost + data[neighbour]

            p = prev.get(node)
            if p and new_cost < p:
                prev[node] = new_cost
            elif not p:
                prev[node] = new_cost

            priority_queue.append((new_cost, neighbour))
        priority_queue = list(reversed(sorted(priority_queue)))

    return prev


def day15():
    data = np.genfromtxt('day15.txt', delimiter=1, dtype=int)
    sp = shortest_path(data)
    print(sp)
    print(len(sp))
    paint(sp)


if __name__ == '__main__':
    day15()

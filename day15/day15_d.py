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


def paint(nodes, short_path):
    pygame.init()
    screen = pygame.display.set_mode((zoom * 100, zoom*100))

    for coord in nodes.keys():
        color = get_color(nodes[coord])
        x = int(coord[0])
        y = int(coord[1])
        pygame.draw.rect(screen, color, pygame.Rect(y * zoom, x * zoom, zoom, zoom))

    pygame.display.flip()

    for coord in short_path:
        color = (50, 50, 255)
        x = int(coord[0])
        y = int(coord[1])
        pygame.draw.rect(screen, color, pygame.Rect(y * zoom, x * zoom, zoom, zoom))

    done = False
    while not done:
        for event in pygame.event.get():
            pygame.time.delay(10)
            pygame.display.flip()
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


def get_next_neighbour(visited, current_node, data, nodes):
    nbs = neighbours(data, current_node)
    best = None
    for nb in nbs:
        if visited.count(nb) > 0:
            continue

        val = nodes[nb]
        if best is None:
            best = nb, val
            continue
        if val < best[1]:
            best = nb, val
    if best is None:
        return None
    return best[0]


def get_path(data, nodes):
    visited = []
    current_node = (99, 99)
    visited.append(current_node)
    while True:
        current_node = get_next_neighbour(visited, current_node, data, nodes)
        if not current_node:
            break
        visited.append(current_node)

    return visited


def day15():
    data = np.genfromtxt('day15.txt', delimiter=1, dtype=int)
    nodes = shortest_path(data)
    short_path = get_path(data, nodes)
    print(short_path)
    print(len(nodes))
    paint(nodes, short_path)


if __name__ == '__main__':
    day15()

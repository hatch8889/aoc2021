import numpy as np
import networkx as nx


def get_danger(data, sp):
    danger = 0
    for coord in sp:
        if coord != (0, 0):
            danger += data[coord]
    return danger


def get_weight(w1, fx, fy):
    c = w1 + fx + fy - 1
    return (c % 9) + 1


def build_graph(data):
    mx = data.shape[0]
    my = data.shape[1]
    # set to 1 for part 1
    f = 5

    new_data = np.zeros((mx*f, my*f))

    g = nx.DiGraph()

    for fx in range(0, f):
        for fy in range(0, f):
            for x, y in np.nditer(np.where(data > 0)):
                tx = fx * 100 + int(x)
                ty = fy * 100 + int(y)
                weight = get_weight(data[x, y], fx, fy)
                new_data[tx, ty] = weight

                g.add_node((tx, ty))
                if tx > 0:
                    g.add_edge((tx, ty), (tx - 1, ty), weight=weight)
                if ty > 0:
                    g.add_edge((tx, ty), (tx, ty - 1), weight=weight)
                if tx + 1 < mx*f:
                    g.add_edge((tx, ty), (tx + 1, ty), weight=weight)
                if ty + 1 < my*f:
                    g.add_edge((tx, ty), (tx, ty + 1), weight=weight)

    print(g)
    sp = nx.shortest_path(g, (f*mx-1, f*my-1), (0, 0), weight='weight', method='bellman-ford')
    print(sp)
    print(len(sp))
    danger = get_danger(new_data, sp)
    print(danger)


def day15():
    data = np.genfromtxt('day15.txt', delimiter=1, dtype=int)
    print(data)
    build_graph(data)


if __name__ == '__main__':
    day15()

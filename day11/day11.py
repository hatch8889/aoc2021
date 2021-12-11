import numpy as np


def day10():
    data = np.loadtxt('day11.txt', dtype=(int, int), converters={0: list}, encoding='latin1')
    all_flashes = 0

    def pos(n):
        return n if n >= 0 else 0

    for i in range(1, 1000):
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

        f = np.count_nonzero(data == 0)
        all_flashes += f
        if i == 100:
            print(f"part1: {all_flashes}")

        if f == 100:
            print(f"part2: {i}")
            break


if __name__ == '__main__':
    day10()

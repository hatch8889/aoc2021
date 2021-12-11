import numpy as np

data = np.genfromtxt('day11.txt', delimiter=1, dtype=int)
all_flashes = 0

for i in range(1, 1000):
    data += 1
    while np.count_nonzero(data >= 10):
        for x, y in np.nditer(np.where(data >= 10)):
            sub_matrix = data[np.clip(x-1, 0, 10):x+2, np.clip(y-1, 0, 10):y+2]
            sub_matrix[sub_matrix > 0] += 1
            data[x, y] = 0

    f = np.count_nonzero(data == 0)
    all_flashes += f
    if i == 100:
        print(f"part1: {all_flashes}")

    if f == 100:
        print(f"part2: {i}")
        break

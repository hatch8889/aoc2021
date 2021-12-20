from collections import Counter
import numpy as np

rm_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
rm_y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
rm_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

rotation_permutations = [
    # n*x, n*y, n*z
    (0, 0, 0),
    (0, 0, 1),
    (0, 0, 2),
    (0, 0, 3),
    (0, 1, 0),
    (0, 1, 1),
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 0),
    (0, 2, 1),
    (0, 2, 2),
    (0, 2, 3),
    (0, 3, 0),
    (0, 3, 1),
    (0, 3, 2),
    (0, 3, 3),
    (1, 0, 0),
    (1, 0, 1),
    (1, 0, 2),
    (1, 0, 3),
    (1, 2, 0),
    (1, 2, 1),
    (1, 2, 2),
    (1, 2, 3),
]


def rotate(n, rot):
    rots = rotation_permutations[rot]
    nn = n
    n_rx, n_ry, n_rz = rots

    for _ in range(0, n_rx):
        nn = np.inner(nn, rm_x)

    for _ in range(0, n_ry):
        nn = np.inner(nn, rm_y)

    for _ in range(0, n_rz):
        nn = np.inner(nn, rm_z)

    return nn


def apply_transpose(nn, transpose):
    x, y, z = transpose
    return nn + (x, y, z)


def get_diff(coord_1, coord_2):
    ax, ay, az = coord_1
    bx, by, bz = coord_2
    return ax-bx, ay-by, az-bz


def distances(n):
    out = []
    for d in n:
        tx, ty, tz = d
        out.append(abs(tx * ty * tz))
    return np.array(out)


def intersect_12(s, d):
    c = 0
    num = len(s)
    for s_1 in s:
        if num + c < 11:
            return c
        for d_1 in d:
            if d_1[0] == s_1[0] and d_1[1] == s_1[1] and d_1[2] == s_1[2]:
                c += 1
            if c >= 12:
                break
        num -= 1
    return c


def get_translation(src, target):
    for src_coord in src:
        for rr in range(0, len(rotation_permutations)):
            rotated = rotate(target, rr)
            for target_coord in rotated:
                transpose = get_diff(src_coord, target_coord)

                translated_target = apply_transpose(rotated, transpose)
                intersect = intersect_12(src, translated_target)
                if intersect >= 12:
                    print(rr)
                    return translated_target, transpose
    return None, None


def translate(n):
    queue = [0]
    translated_indices = []
    output = {0: n[0]}
    scanner_pos = {0: (0, 0, 0)}

    while len(queue) > 0:
        ii = queue.pop()
        if translated_indices.count(ii):
            continue
        translated_indices.append(ii)
        src = output[ii]
        for jj in range(0, len(n)):
            if ii == jj:
                continue
            if output.get(jj) is not None:
                continue

            trans, pos_diff = get_translation(src, n[jj])
            if trans is not None:
                queue.append(jj)
                output[jj] = trans
                scanner_pos[jj] = pos_diff
                print(queue)

    return output.values(), scanner_pos.values()


def get_counts(ss):
    c = Counter({})
    for s in ss:
        for it in s:
            x, y, z = it
            c[(x, y, z)] += 1
    return c


def get_distance(probes):
    largest = 0
    for p1 in probes:
        for p2 in probes:
            dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])
            if dist > largest:
                largest = dist
    print(largest)


if __name__ == "__main__":
    scanners = []
    current_scanner = []

    with open("day19_r.txt") as data:
        for line in data.read().splitlines():
            if line.startswith('--- scan'):
                continue
            if line == '':
                scanners.append(np.array(current_scanner))
                current_scanner = []
                continue
            x, y, z = line.split(',')
            current_scanner.append((int(x), int(y), int(z)))
        scanners.append(np.array(current_scanner))
        translated_scanners, scanner_positions = translate(scanners)
        print(translated_scanners)
        print(len(translated_scanners))
        counts = get_counts(translated_scanners)
        print(counts)
        print(len(counts))
        print(scanner_positions)
        get_distance(scanner_positions)


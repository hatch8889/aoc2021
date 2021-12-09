class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Basin:
    points = []
    # bounding box
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    def __init__(self):
        self.points = []

    def add_point(self, x: int, y: int):
        self.points.append(Point(x, y))
        if x < self.min_x:
            self.min_x = x
        if y < self.min_y:
            self.min_x = y
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

    def in_basin_adjacent(self, x: int, y: int):
        if self.max_y - 1 > y:
            return False
        if x < self.min_x - 1:
            return False

        for p in self.points:
            if p.x == x and p.y == y:
                return True
            if p.x == x - 1 and p.y == y:
                return True
            if p.x == x and p.y == y - 1:
                return True

        return False

    def in_basin(self, x: int, y: int):
        if y > self.max_y + 1:
            return False
        if x < self.min_x - 1:
            return False

        for p in self.points:
            if p.x == x and p.y == y:
                return True
        return False

    def size(self):
        return len(self.points)

    def __str__(self):
        return f"{len(self.points)}"


def find_point(basins, x: int, y: int):
    if x < 0 or y < 0:
        return None

    for b in basins:
        if b.min_x - 1 <= x <= b.max_x + 1 and b.min_y - 1 <= y <= b.max_y + 1 and b.in_basin_adjacent(x, y):
            yield b

    return None


def height_points(matrix: []):
    basins = []
    for y in range(0, len(matrix)):
        row = matrix[y]
        for x in range(0, len(row)):
            c = row[x]
            if c == 9:
                continue

            matched_basins = list(find_point(basins, x, y))
            if len(matched_basins) > 0:
                basin = matched_basins[0]

                # merge basins
                if len(matched_basins) > 1:
                    for b in matched_basins[1:]:
                        for p in b.points:
                            basin.add_point(p.x, p.y)
                        basins.remove(b)

                if not basin.in_basin(x, y):
                    basin.add_point(x, y)
                continue

            nb = Basin()
            nb.add_point(x, y)
            basins.append(nb)
    return basins


def day9():
    with open('day9.txt') as data:
        lines = data.read().splitlines()
        matrix = []
        for x in range(0, len(lines)):
            row = lines[x]
            yarr = []
            for y in range(0, len(row)):
                yarr.append(int(row[y]))
            matrix.append(yarr)

        basins = height_points(matrix)
        sizes = []
        for b in basins:
            sizes.append(b.size())

        bb = list(reversed(sorted(sizes)))
        print(f"{bb[0]}  {bb[1]} {bb[2]}")
        print(bb[0] * bb[1] * bb[2])


if __name__ == '__main__':
    day9()

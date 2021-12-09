import pygame


class Point:
    x: int = 0
    y: int = 0
    n: int = 0

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n


class Basin:
    points = []
    # bounding box
    min_x = None
    min_y = None
    max_x = None
    max_y = None

    def __init__(self, x, y, c):
        self.points = []
        self.min_y = y
        self.max_y = y
        self.min_x = x
        self.max_x = x
        self.add_point(x, y, c)

    def add_point(self, x: int, y: int, n: int):
        self.points.append(Point(x, y, n))
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
                            basin.add_point(p.x, p.y, c)
                        basins.remove(b)

                if not basin.in_basin(x, y):
                    basin.add_point(x, y, c)
                continue

            nb = Basin(x, y, c)
            basins.append(nb)
    return basins


color_map = {
    0: (51, 0, 0),
    1: (102, 0, 0),
    2: (153, 0, 0),
    3: (204, 0, 0),
    4: (255, 0, 0),
    5: (255, 51, 0),
    6: (255, 102, 0),
    7: (255, 153, 0),
    8: (255, 204, 0),
    9: (0, 0, 51)
}


def day9():
    pygame.init()
    zoom = 12
    screen = pygame.display.set_mode((zoom*100, zoom*100))
    done = False
    pygame.display.flip()

    with open('day9.txt') as data:
        lines = data.read().splitlines()
        matrix = []
        for col_index in range(0, len(lines)):
            row = lines[col_index]
            yarr = []
            for row_index in range(0, len(row)):
                c = int(row[row_index])
                yarr.append(c)
                pygame.draw.rect(screen, color_map[c], pygame.Rect(row_index * zoom, col_index * zoom, zoom, zoom))
            matrix.append(yarr)

        basins = height_points(matrix)
        sizes = []
        for b in basins:
            sizes.append(b.size())

        for xline in range(zoom, zoom*100, zoom):
            pygame.draw.line(screen, (0, 0, 0), (xline, 0), (xline, zoom*100), 1)
            pygame.draw.line(screen, (0, 0, 0), (0, xline), (zoom*100, xline), 1)

        bb = list(reversed(sorted(sizes)))

        for i in range(0, len(basins)):
            b = basins[i]

            rl = b.min_x * zoom + 1
            rt = b.min_y * zoom + 1
            rw = (b.max_x - b.min_x) * zoom + 7
            rh = (b.max_y - b.min_y) * zoom + 7

            font = pygame.font.Font(None, len(b.points))
            text = font.render(f"{len(b.points)}", True, (255, 122, 255))
            tl = rl + rw // 2 - text.get_width() // 2
            tt = rt + rh // 2 - text.get_height() // 2
            screen.blit(text, (tl, tt))

        print(f"{bb[0]}  {bb[1]} {bb[2]}")
        print(bb[0] * bb[1] * bb[2])

    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == '__main__':
    day9()

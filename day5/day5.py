class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"


class Segment:
    p: Point = 0
    q: Point = 0

    def max_x(self):
        if self.p.x > self.q.x:
            return self.p.x
        return self.q.x

    def max_y(self):
        if self.p.y > self.q.y:
            return self.p.y
        return self.q.y

    def __init__(self, line):
        s, d = line.split(' -> ')
        x1, y1 = s.split(',')
        self.p = Point(int(x1), int(y1))
        x2, y2 = d.split(',')
        self.q = Point(int(x2), int(y2))

    def __str__(self):
        return f"{self.p} -> {self.q}"


def parse_lines(lines: []):
    for segment in lines:
        yield Segment(segment)


def full_range(a: int, b: int):
    if a > b:
        return range(b, a + 1)
    return reversed(range(a, b + 1))


def create_matrix(segments: [Segment]):
    max_x = max(map(lambda s: s.max_x(), segments)) + 1
    max_y = max(map(lambda s: s.max_y(), segments)) + 1
    matrix = [[0 for _ in range(max_y)] for _ in range(max_x)]

    for seg in segments:
        if seg.p.x == seg.q.x:
            for y in full_range(seg.p.y, seg.q.y):
                matrix[seg.p.x][y] += 1
        elif seg.p.y == seg.q.y:
            for x in full_range(seg.p.x, seg.q.x):
                matrix[x][seg.p.y] += 1
        else:
            # comment-out for part 1
            i = 0
            y_range = list(full_range(seg.p.y, seg.q.y))
            for x in full_range(seg.p.x, seg.q.x):
                y = y_range[i]
                matrix[x][y] += 1
                i += 1

    return matrix


def print_matrix(matrix: []):
    out = ''
    for x in matrix:
        for y in x:
            out += str(y)
        out += '\n'

    print(out)


def day5():
    with open('day5.txt') as data:
        lines = list(parse_lines(data.read().splitlines()))
        matrix = create_matrix(lines)

        print_matrix(matrix)
        count = 0
        for x in matrix:
            for y in x:
                if y >= 2:
                    count += 1
        print(count)


if __name__ == '__main__':
    day5()

def height_points(matrix: []):
    for y in range(0, len(matrix)):
        row = matrix[y]
        for x in range(0, len(row)):
            c = row[x]
            adjacent_data = []
            if x > 0:
                adjacent_data.append(row[x-1])
            if y > 0:
                adjacent_data.append(matrix[y-1][x])
            if x < len(row) - 1:
                adjacent_data.append(row[x+1])
            if y < len(matrix) - 1:
                adjacent_data.append(matrix[y+1][x])
            if c < min(adjacent_data):
                yield c + 1


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

        points = list(height_points(matrix))

        print(points)
        print(sum(points))


if __name__ == '__main__':
    day9()

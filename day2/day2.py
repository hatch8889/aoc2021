def day2():
    y = 0
    x = 0

    with open('day2.txt') as data:
        inputs = data.read().splitlines()
        for i in inputs:
            move, rs = i.split()
            r = int(rs)
            if move == 'forward':
                y += r
            elif move == 'up':
                x -= r
            elif move == 'down':
                x += r

        print(x*y)


if __name__ == '__main__':
    day2()

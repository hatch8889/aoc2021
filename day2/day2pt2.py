def day2():
    y = 0
    x = 0
    aim = 0

    with open('day2.txt') as data:
        inputs = data.read().splitlines()
        for i in inputs:
            move, rs = i.split()
            r = int(rs)
            if move == 'forward':
                y += r
                x += aim * r
            elif move == 'up':
                aim -= r
            elif move == 'down':
                aim += r

        print(x*y)


if __name__ == '__main__':
    day2()
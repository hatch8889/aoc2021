def get_crabs(lines: []):
    return list(map(int, lines.split(',')))


def part2(c: int):
    return int(c * (c + 1) / 2)


def day7():
    with open('day7.txt') as data:
        crabs = get_crabs(data.read())

        least_fuel = None
        for i in range(min(crabs), max(crabs) + 1):
            fuel = 0
            for c in crabs:
                fuel += part2(abs(c - i))
            if least_fuel is None or fuel < least_fuel:
                least_fuel = fuel
        print(least_fuel)


if __name__ == '__main__':
    day7()

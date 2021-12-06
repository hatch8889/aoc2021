def create_school(data: []):
    return list(map(lambda s: int(s), data.split(',')))


def get_sum(index: {}):
    s = 0
    for i in range(0, 9):
        s += index[i]
    return s


def progress(index: {}):
    new_index = {}
    for i in range(0, 9):
        new_index[i] = 0

    for i in range(0, 9):
        num = index[i]

        if i == 0:
            new_index[6] += num
            new_index[8] += num
        else:
            new_index[i-1] += num
    return new_index


def day6():
    with open('day6.txt') as data:
        school_of_fish = create_school(data.read())

        index = {}
        for i in range(0, 9):
            index[i] = 0

        for fish in school_of_fish:
            index[fish] += 1

        for day in range(1, 257):
            index = progress(index)
            print(f"day {day}: {get_sum(index)}")


if __name__ == '__main__':
    day6()

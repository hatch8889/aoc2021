def day1pt1(inputs):
    result = 0
    for i in range(1, len(inputs)):
        if inputs[i] > inputs[i-1]:
            result += 1

    print(result)


def day1pt2(inputs):
    result = 0
    sums = []

    for i in range(2, len(inputs)):
        s = inputs[i-2] + inputs[i-1] + inputs[i]
        if len(sums) > 0 and s > sums[-1]:
            result += 1
        sums.append(s)

    print(result)


def day1():
    with open('day1.txt') as data:
        inputs = list(map(int, data.read().splitlines()))
        day1pt1(inputs)
        day1pt2(inputs)


if __name__ == '__main__':
    day1()

segments = {
    'a': 0b0000001,
    'b': 0b0000010,
    'c': 0b0000100,
    'd': 0b0001000,
    'e': 0b0010000,
    'f': 0b0100000,
    'g': 0b1000000
}


def to_segment(s: str):
    r = 0
    for x in s:
        r |= segments[x]
    return r


def bit_count(n: int):
    c = 0
    for i in range(0, 8):
        if n >> i & 1 == 1:
            c += 1
    return c


def segmentize(left: str, right: str):
    input_digits_r = list(map(lambda s: ''.join(sorted(s)), right.split(' ')))
    input_digits_l = list(map(lambda s: ''.join(sorted(s)), left.split(' ')))

    number_map = {}
    all_digits = set(map(to_segment, input_digits_l + input_digits_r))
    for d in all_digits:
        c = bit_count(d)
        if c == 2:
            number_map[1] = d
        if c == 4:
            number_map[4] = d
        if c == 3:
            number_map[7] = d
        if c == 7:
            number_map[8] = d

    bd = number_map[1] ^ number_map[4]
    eg = number_map[8] ^ (number_map[4] | (number_map[7] - number_map[1]))

    for d in all_digits:
        if bit_count(d) == 5:
            if eg & d == eg:
                number_map[2] = d
            elif bd & d == bd:
                number_map[5] = d
            else:
                number_map[3] = d
        elif bit_count(d) == 6:
            if bd & d != bd:
                number_map[0] = d
            elif eg & d == eg:
                number_map[6] = d
            else:
                number_map[9] = d

    idx = {}
    for ii in range(0, 10):
        dd = number_map[ii]
        idx[dd] = ii

    def mm(x: str):
        return str(idx[to_segment(x)])

    lo = ''.join(list(map(mm, input_digits_l)))
    ro = ''.join(list(map(mm, input_digits_r)))
    return [lo, ro]


def day8():
    with open('day8.txt') as data:
        lines = list(data.read().splitlines())

        s = 0
        for line in lines:
            i, o = line.split(' | ')
            results = segmentize(i, o)
            print(results)
            s += int(results[1])
        print(s)


if __name__ == '__main__':
    day8()

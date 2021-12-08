from itertools import permutations


segment_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def convert_to_digit(d: str):
    return segment_digit.get(''.join(sorted(d)), None)


def bruteforce(l: str, r: str):
    input_digits_r = r.split(' ')
    input_digits_l = l.split(' ')

    for guess in permutations(segments):
        segment_map = {}
        for ii in range(0, 7):
            segment_map[segments[ii]] = guess[ii]

        out_l = ''
        for digit in input_digits_l:
            mapped = ''.join(map(lambda d: segment_map[d], digit))
            out = convert_to_digit(mapped)
            if out is None:
                out_l = None
                break
            out_l += str(out)

        if out_l is None:
            # no luck this time, try again
            continue

        out_r = ''
        for digit in input_digits_r:
            mapped = ''.join(map(lambda d: segment_map[d], digit))
            out = convert_to_digit(mapped)
            if out is None:
                out_r = None
                break
            out_r += str(out)

        if out_r is None:
            # no luck this time, try again
            continue

        if out_l and out_r:
            return [out_l, out_r]


def day8():
    with open('day8.txt') as data:
        lines = list(data.read().splitlines())

        s = 0
        for line in lines:
            i, o = line.split(' | ')
            results = bruteforce(i, o)
            print(results)
            s += int(results[1])
        print(s)


if __name__ == '__main__':
    day8()

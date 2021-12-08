def is_match(fix: str, c: str):
    for f in fix:
        if c.count(f) == 0:
            return False
    return True


def remap(l: str, r: str):
    input_digits_r = list(map(lambda s: ''.join(sorted(s)), r.split(' ')))
    input_digits_l = list(map(lambda s: ''.join(sorted(s)), l.split(' ')))

    nums = {}
    for digit in input_digits_l + input_digits_r:
        if len(digit) == 2:
            nums[1] = digit
        elif len(digit) == 4:
            nums[4] = digit
        elif len(digit) == 7:
            nums[8] = digit
        elif len(digit) == 3:
            nums[7] = digit

    for digit in input_digits_l + input_digits_r:
        if len(digit) == 6:
            # 0, 6 or 9
            if is_match(nums[4], digit):
                nums[9] = digit
                break

    for digit in input_digits_l + input_digits_r:
        if nums[9] != digit and len(digit) == 6:
            # 0, 6
            if is_match(nums[1], digit):
                nums[0] = digit
            else:
                nums[6] = digit

    for digit in input_digits_l + input_digits_r:
        if len(digit) == 5:
            # 2, 5, 3
            if is_match(nums[1], digit):
                nums[3] = digit
                break

    for digit in input_digits_l + input_digits_r:
        if nums[3] != digit and len(digit) == 5:
            # 2, 5
            if is_match(digit, nums[6]):
                nums[5] = digit
            else:
                nums[2] = digit

    def map_digit(s: str):
        for ii in range(0, 10):
            if nums[ii] == s:
                return str(ii)

        print(s)

    lo = list(map(map_digit, input_digits_l))
    ro = list(map(map_digit, input_digits_r))

    return [''.join(lo), ''.join(ro)]


def day8():
    with open('day8.txt') as data:
        lines = list(data.read().splitlines())

        s = 0
        for line in lines:
            i, o = line.split(' | ')
            results = remap(i, o)
            print(results)
            s += int(results[1])
        print(s)


if __name__ == '__main__':
    day8()

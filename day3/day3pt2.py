def split_data(shift: int, data: []):
    return [
        list(filter(lambda x: (x >> shift) & 1 == 1, data)),
        list(filter(lambda x: (x >> shift) & 1 == 0, data))
    ]


def filter_ox(shift: int, data: []):
    bit_data, bit_data_neg = split_data(shift, data)

    if len(bit_data) >= len(data) / 2:
        return bit_data
    else:
        return bit_data_neg


def filter_co2(shift: int, data: []):
    bit_data, bit_data_neg = split_data(shift, data)

    if len(bit_data_neg) <= len(data) / 2:
        return bit_data_neg
    else:
        return bit_data


def day3():
    bits = 12
    with open('day3.txt') as data:
        data = list(map(lambda x: int(x, 2), data.read().splitlines()))
        oxygen_data = data
        co2_data = data

        for idx in range(bits):
            if len(oxygen_data) <= 1:
                break
            oxygen_data = filter_ox(bits - idx - 1, oxygen_data)

        for idx in range(bits):
            if len(co2_data) <= 1:
                break
            co2_data = filter_co2(bits - idx - 1, co2_data)

        print(oxygen_data)
        print(co2_data)
        print(oxygen_data[0] * co2_data[0])


if __name__ == '__main__':
    day3()

def day3():
    bit_count = {}

    with open('day3.txt') as data:
        inputs = data.read().splitlines()
        for line in inputs:
            for idx, n in enumerate(line):
                if n == '1':
                    if idx not in bit_count.keys():
                        bit_count[idx] = 0

                    bit_count[idx] += 1

        gamma = 0
        epsilon = 0
        for i in range(len(bit_count)):
            if bit_count[i] > len(inputs) / 2:
                gamma = gamma | 1
            else:
                epsilon = epsilon | 1
            gamma = gamma << 1
            epsilon = epsilon << 1

        gamma = gamma >> 1
        epsilon = epsilon >> 1

        print(gamma*epsilon)


if __name__ == '__main__':
    day3()

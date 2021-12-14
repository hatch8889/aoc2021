def day14():
    with open('day14.txt') as data:
        instructions = {}

        polymer, dd = data.read().split('\n\n')
        for instruction in dd.splitlines():
            l, r = instruction.split(' -> ')
            instructions[l] = r

        pairs = {p: polymer.count(p) for p in instructions}
        chars = {char: polymer.count(char) for char in instructions.values()}

        for i in range(40):
            for pair, value in pairs.copy().items():
                if value != 0:
                    pairs[pair] -= value
                    pairs[instructions[pair] + pair[1]] += value
                    pairs[pair[0] + instructions[pair]] += value
                    chars[instructions[pair]] += value

        print(pairs)
        print(polymer)
        print(instructions)
        print(max(chars.values()) - min(chars.values()))


if __name__ == '__main__':
    day14()
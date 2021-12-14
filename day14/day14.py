from collections import Counter

max_depth = 40


class Polymerization:
    elements: {}
    instructions: {}
    cache: {}

    def __init__(self, instructions):
        self.elements = {}
        self.instructions = instructions
        self.cache = {}

    def recursive_count(self, polymer, depth):
        if depth == max_depth:
            return self.do_count(polymer), ''
        if len(polymer) < 2:
            return Counter({}), polymer

        cache_key = f"{polymer}_{depth}"
        cache_entry = self.cache.get(cache_key)
        if cache_entry:
            return cache_entry

        count = Counter({})
        leftover = ''
        for r in range(len(polymer)):
            el = polymer[r:r+2]
            ins = self.instructions.get(el)
            if ins:
                c1, leftover = self.recursive_count(leftover + el[0] + ins, depth + 1)
                count += c1
            elif len(el) < 2:
                leftover += el
        if len(leftover) == 2:
            c, ll = self.recursive_count(leftover, depth + 1)
            self.cache[cache_key] = (count + c, ll)
            return count + c, ll

        self.cache[cache_key] = (count, leftover)
        return count, leftover

    def do_count(self, polymer):
        count = Counter({})
        for c in polymer:
            count[c] += 1
        return count


def day14():
    with open('day14.txt') as data:
        instructions = {}

        polymer, dd = data.read().split('\n\n')
        for instruction in dd.splitlines():
            l, r = instruction.split(' -> ')
            instructions[l] = r

        print(polymer)
        print(instructions)

        polymerization = Polymerization(instructions)
        counts, left = polymerization.recursive_count(polymer, 0)
        counts += polymerization.do_count(left)
        print(counts)
        srt = sorted(counts, key=counts.get, reverse=True)
        high = counts[srt[0]]
        low = counts[srt[-1]]
        print(high-low)


if __name__ == '__main__':
    day14()
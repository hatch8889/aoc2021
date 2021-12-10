def sanitize(ll):
    x = ll.replace('[]', '').replace('{}', '').replace('<>', '').replace('()', '')
    if x == ll:
        return ll
    return sanitize(x)


weights = {
    ']': 2,
    ')': 1,
    '}': 3,
    '>': 4
}


replaces = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}


def get_score(ll: str):
    c = 0
    for s in ll:
        c *= 5
        c += weights[s]
    return c


def get_count(ll: str):
    s = sanitize(ll)
    for x in s:
        if x == ')':
            return 3
        elif x == ']':
            return 57
        elif x == '}':
            return 1197
        elif x == '>':
            return 25137

    return 0


def get_replacements(ll: str):
    s = sanitize(ll)
    if get_count(s) > 0:
        return

    return ''.join(map(lambda x: replaces[x], reversed(s)))


def day10():
    with open('day10.txt') as data:
        lines = list(data.read().splitlines())
        s: int = 0
        scores = []
        for ll in lines:
            s += get_count(ll)
            x = get_replacements(ll)
            if x:
                scores.append(get_score(x))
        print(f"part1: {s}")
        ss = sorted(scores)
        idx = len(ss) // 2
        print(f"part2: {ss[idx]}")


if __name__ == '__main__':
    day10()

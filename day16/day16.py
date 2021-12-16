import io as io


def operation(a1: int, a2: int, typ: int) -> int:
    if typ == 0:
        return a1 + a2
    if typ == 1:
        return a1 * a2
    if typ == 2:
        return min(a1, a2)
    if typ == 3:
        return max(a1, a2)
    if typ == 5:
        if a1 > a2:
            return 1
        return 0
    if typ == 6:
        if a1 < a2:
            return 1
        return 0
    if typ == 7:
        if a1 == a2:
            return 1
        return 0

    raise Exception(f"Unknown type: {typ}")


def read_operator(f, typ):
    op_type = int(f.read(1), 2)
    bit_length = 15
    if op_type == 1:
        bit_length = 11

    n = int(f.read(bit_length), 2)
    if op_type == 0:
        s = f.read(n)
        tmp = io.StringIO(s)
        res, v_s = None, 0
        while True:
            r2, ver = level_1_read(tmp)
            if r2 is None:
                break
            if res is None:
                res = r2
            else:
                res = operation(res, r2, typ)
            v_s += ver
        return res, v_s

    res, v_s = None, 0
    for _ in range(0, n):
        r2, v2 = level_1_read(f)
        if r2 is None:
            continue
        if res is None:
            res = r2
        else:
            res = operation(res, r2, typ)

        v_s += v2
    return res, v_s


def read_literal(f, d=0):
    has_next = int(f.read(1), 2)
    data = f.read(4)
    if has_next:
        data += str(read_literal(f, d + 1))

    if d == 0:
        return int(data, 2)
    return data


def level_1_read(f):
    pos = f.tell()
    read_ahead = f.read(8)
    if not read_ahead or len(read_ahead) < 8:
        return None, 0
    f.seek(pos)

    b = f.read(3)
    ver = int(b, 2)
    typ = int(f.read(3), 2)
    if typ == 4:
        return read_literal(f), ver
    else:
        d2, v2 = read_operator(f, typ)
        return d2, ver + v2


def day16():
    f = io.StringIO('')

    with open("day16.txt") as data:
        while True:
            h = data.read(1)
            if not h:
                break
            f.write(bin(int(h, 16))[2:].zfill(4))

    f.seek(0)

    ver_sum = 0
    while True:
        read, ver = level_1_read(f)

        if read is None:
            break
        ver_sum += ver
        print(f"Result: {read}")

    print(f"version sum: {ver_sum}")


if __name__ == '__main__':
    day16()

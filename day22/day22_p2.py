orders = []


def parse_coords(txt):
    xx, yy, zz = txt.split(',')
    sx, tx = xx.split('..')
    sy, ty = yy.split('..')
    sz, tz = zz.split('..')

    return (int(sx[2:]), int(sy[2:]), int(sz[2:])), (int(tx), int(ty), int(tz))


def get_count(start: (int, int, int), end: (int, int, int)) -> int:
    return (end[0] - start[0] + 1) * (end[1] - start[1] + 1) * (end[2] - start[2] + 1)


class Order(object):
    lit = False
    start = (0, 0, 0)
    end = (0, 0, 0)
    line = 'x'

    def __init__(self, line):
        if line is None:
            return
        order, coords = line.split(' ')
        self.lit = order == 'on'
        self.start, self.end = parse_coords(coords)
        self.line = line

    def __repr__(self):
        return f"{self.lit} : {self.start} --> {self.end}"

    def count(self):
        return get_count(self.start, self.end)


def get_intersection(a: Order, b: Order) -> Order or None:
    # out of bounds
    scx = max(a.start[0], b.start[0])
    ecx = min(a.end[0], b.end[0])
    if ecx < scx:
        return None
    scy = max(a.start[1], b.start[1])
    ecy = min(a.end[1], b.end[1])
    if ecy < scy:
        return None

    scz = max(a.start[2], b.start[2])
    ecz = min(a.end[2], b.end[2])
    if ecz < scz:
        return None

    c = Order(None)
    c.start = (scx, scy, scz)
    c.end = (ecx, ecy, ecz)
    c.lit = b.lit
    return c


def get_intersections(order: Order, orders: [Order]) -> Order:
    for ii in range(0, len(orders)):
        bb = orders[ii]
        c = get_intersection(order, bb)
        if c:
            yield c


def get_non_intersective_count(input_order, start_index: int) -> int:
    _order = input_order
    if start_index >= len(orders):
        return _order.count()

    cnt = _order.count()
    for ii in range(start_index, len(orders)):
        target_box = orders[ii]
        bounding = get_intersection(_order, target_box)
        if bounding is None:
            continue
        cnt -= get_non_intersective_count(bounding, ii + 1)

    return cnt


if __name__ == '__main__':
    with open('test.txt') as data:
        orders = []
        for line in data.readlines():
            orders.append(Order(line))

        count = 0
        for ii in range(0, len(orders)):
            print(ii)
            order = orders[ii]
            if order.lit:
                count += get_non_intersective_count(order, ii + 1)
            print(count)
        print(count)


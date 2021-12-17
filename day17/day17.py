def step(position, velocity):
    x, y = position
    vx, vy = velocity
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return (x, y), (vx, vy)


def is_hit(position, target_area):
    x, y = position
    tx1, tx2, ty1, ty2 = target_area

    if tx1 <= x <= tx2 and ty1 <= y <= ty2:
        return 1
    if y < ty1:
        return -1
    if x > tx2:
        return -1

    return 0


def try_hit(velocity, target_area):
    pos = (0, 0)
    vel = velocity
    max_y = -100

    while True:
        hit = is_hit(pos, target_area)
        if pos[1] > max_y:
            max_y = pos[1]

        if hit != 0:
            break

        pos, vel = step(pos, vel)

    return hit, max_y


def day17():
    my_target_area = (155, 215, -132, -72)
    target_area = (20, 30, -10, -5)
    max_y = -500
    best_v = (0, 0)
    count = 0
    for vx in range(0, 400):
        for vy in range(-400, 400):
            h, my = try_hit((vx, vy), my_target_area)
            if h == 1:
                count += 1
                if my > max_y:
                    max_y = my
                    best_v = (vx, vy)
    print(f" max-y: {max_y} ---- best velocity: {best_v} --- count {count}")
    # target area: x=155..215, y=-132..-72
    # target area: x=20..30, y=-10..-5


if __name__ == '__main__':
    day17()

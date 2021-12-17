import asyncio
import concurrent.futures

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

    return hit, max_y, velocity


def inter(vx, target_area):
    ret = []
    for vy in range(-400, 400):
        hit, max_y, velocity = try_hit((vx, vy), target_area)
        if hit == 1:
            ret.append((hit, max_y, velocity))
    return ret


def day17():
    th_executor = concurrent.futures.ThreadPoolExecutor(max_workers=24)
    event_loop = asyncio.get_event_loop()

    my_target_area = (155, 215, -132, -72)
    target_area = (20, 30, -10, -5)
    max_y = -500
    best_v = (0, 0)
    count = 0
    tasks = []

    for vx in range(0, 400):
        task = event_loop.run_in_executor(th_executor, inter, vx, my_target_area)
        tasks.append(task)

    completed = asyncio.wait(tasks)
    event_loop.run_until_complete(completed)

    for t in tasks:
        for result in t.result():
            h, my, velocity = result
            if h == 1:
                count += 1
                if my > max_y:
                    max_y = my
                    best_v = velocity

    print(f" max-y: {max_y} ---- best velocity: {best_v} --- count {count}")

    # target area: x=155..215, y=-132..-72
    # target area: x=20..30, y=-10..-5


if __name__ == '__main__':
    day17()

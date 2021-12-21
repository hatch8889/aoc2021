p1_position = 1
p2_position = 2

p1_points = 0
p2_points = 0

die_state = 1
die_count = 0
p1_turn = True


def roll():
    global die_state
    global die_count
    n = die_state

    die_count += 1
    die_state += 1
    if die_state > 100:
        die_state = 1
    return n

def move(cur_pos, a):
    out = cur_pos + a
    if out % 10 == 0:
        return 10
    return out % 10


def turn():
    global p1_position
    global p1_points
    global p1_turn
    global p2_position
    global p2_points

    a = 0
    a += roll()
    a += roll()
    a += roll()

    if p1_turn:
        p1_position = move(p1_position, a)
        p1_points += p1_position
    else:
        p2_position = move(p2_position, a)
        p2_points += p2_position
    p1_turn = not p1_turn


def check_game_end():
    global p1_position
    global p1_points
    global p1_turn
    global p2_position
    global p2_points

    if p1_points >= 1000 or p2_points >= 1000:
        losing_player = min(p1_points, p2_points)

        print(f"result: {losing_player * die_count}")
        return False

    return True


def game():
    while check_game_end():
        turn()


game()

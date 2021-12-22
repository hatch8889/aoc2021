from collections import Counter
from functools import cache

# roll 1-3, 3 times
possible_outcomes = Counter({
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
})


def move(cur_pos, a):
    out = cur_pos + a
    if out % 10 == 0:
        return 10
    return out % 10


@cache
def play(p1_score, p2_score, p1_pos, p2_pos):
    if p2_score >= 21:
        return 0, 1
    win = 0
    lose = 0
    for roll, outcome in possible_outcomes.items():
        newpos = move(p1_pos, roll)
        new_lose, new_win = play(p2_score, p1_score + newpos, p2_pos, newpos)
        win += new_win * outcome
        lose += new_lose * outcome
    return win, lose


wins, loses = play(0, 0, 2, 4)
print(wins)
print(loses)

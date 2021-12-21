from collections import Counter
from functools import cache
from itertools import product

weights = Counter([sum(x) for x in product(range(1, 4), repeat=3)])

@cache
def play(pos, scores, turn):
    if scores[0] >= 21: return Counter({0: 1})
    if scores[1] >= 21: return Counter({1: 1})

    wins = Counter()
    next_turn = (turn + 1) % 2

    for delta, weight in weights.items():
        this_pos = (pos[turn] + delta - 1) % 10 + 1
        next_pos = pos[:turn] + (this_pos,) + pos[turn + 1:]

        this_score = scores[turn] + next_pos[turn]
        next_scores = scores[:turn] + (this_score,) + scores[turn + 1:]

        for p, p_wins in play(next_pos, next_scores, next_turn).items():
            wins[p] += p_wins * weight

    return wins

pos = tuple(int(input().split(": ")[1]) for _ in range(2))
scores = (0, 0)
print(play(pos, scores, 0).most_common(1)[0][1])

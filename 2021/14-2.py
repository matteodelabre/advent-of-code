from itertools import pairwise
from collections import Counter

rules = {}
poly = input()
pairs = Counter(pairwise(poly))
input()

try:
    while True:
        match, insert = input().split(" -> ")
        rules[tuple(match)] = insert
except EOFError:
    pass

def do(pairs):
    return sum((
        Counter({(pair[0], rules[pair]): count})
        + Counter({(rules[pair], pair[1]): count})
        for pair, count in pairs.items()
    ), start=Counter())

for _ in range(40):
    pairs = do(pairs)

elements = sum((
    Counter({pair[0]: count})
    + Counter({pair[1]: count})
    for pair, count in pairs.items()
), start=Counter())

elements[poly[0]] += 1
elements[poly[-1]] += 1

counts = elements.most_common()
print(counts[0][1] // 2 - counts[-1][1] // 2)

from itertools import pairwise
from collections import Counter

rules = {}
poly = input()
input()

try:
    while True:
        match, insert = input().split(" -> ")
        rules[tuple(match)] = insert
except EOFError:
    pass

def do(poly):
    return "".join([
        pair[0] + rules[pair]
        for pair in pairwise(poly)
    ]) + poly[-1]

for _ in range(10):
    poly = do(poly)

counts = Counter(poly).most_common()
print(counts[0][1] - counts[-1][1])

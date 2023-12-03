from collections import defaultdict
from itertools import product
from math import prod

total = 0
lines = open(0).read().splitlines()
all_gears = defaultdict(list)

for i in range(len(lines)):
    number_start = None
    number_gears = set()

    for j in range(len(lines[i]) + 1):
        if j < len(lines[i]) and lines[i][j].isdigit():
            if number_start is None:
                number_start = j

            for di, dj in product((-1, 0, 1), repeat=2):
                si = i + di
                sj = j + dj

                if 0 <= si < len(lines) and 0 <= sj < len(lines[si]):
                    if lines[si][sj] == "*":
                        number_gears.add((si, sj))
        else:
            if number_start is not None:
                for gear in number_gears:
                    all_gears[gear].append(int(lines[i][number_start:j]))

                number_start = None
                number_gears = set()

print(sum(prod(elts) for elts in all_gears.values() if len(elts) == 2))

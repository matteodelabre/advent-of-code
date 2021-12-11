from itertools import count, product
octopi = []

try:
    while True: octopi.append(list(map(int, input())))
except EOFError:
    pass

w = len(octopi[0])
h = len(octopi)

def sim():
    changed = True
    flashing = [[False] * w for _ in range(h)]

    for i, j in product(range(h), range(w)):
        octopi[i][j] += 1

    while changed:
        changed = False

        for i, j in product(range(h), range(w)):
            if octopi[i][j] > 9 and not flashing[i][j]:
                changed = True
                flashing[i][j] = True

                for ni, nj in product(range(-1, 2), repeat=2):
                    if 0 <= i + ni < h and 0 <= j + nj < w and \
                            (ni != 0 or nj != 0):
                        octopi[i + ni][j + nj] += 1

    for i, j in product(range(h), range(w)):
        if flashing[i][j]:
            octopi[i][j] = 0

    return all(all(row) for row in flashing)

print(next(step for step in count(1) if sim()))

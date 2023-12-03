from itertools import product

total = 0
lines = open(0).read().splitlines()

for i in range(len(lines)):
    number_start = None
    has_symbol = False

    for j in range(len(lines[i]) + 1):
        if j < len(lines[i]) and lines[i][j].isdigit():
            if number_start is None:
                number_start = j

            for di, dj in product((-1, 0, 1), repeat=2):
                si = i + di
                sj = j + dj

                if 0 <= si < len(lines) and 0 <= sj < len(lines[si]):
                    if lines[si][sj] not in ".0123456789":
                        has_symbol = True
        else:
            if number_start is not None:
                if has_symbol:
                    total += int(lines[i][number_start:j])

                number_start = None
                has_symbol = False

print(total)

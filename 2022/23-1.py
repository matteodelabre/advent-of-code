from collections import defaultdict

neighborhoods = {
    ( 0, -1): ((-1, -1), ( 0, -1), ( 1, -1)),
    ( 0,  1): ((-1,  1), ( 0,  1), ( 1,  1)),
    (-1,  0): ((-1, -1), (-1,  0), (-1,  1)),
    ( 1,  0): (( 1, -1), ( 1,  0), ( 1,  1)),
}
directions = list(neighborhoods.keys())

def move(elves, startdir):
    votes = defaultdict(int)
    moves = {(x, y): (x, y) for x, y in elves}

    for x, y in elves:
        if any(
            (x + dx, y + dy) in elves
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if dx != 0 or dy != 0
        ):
            for direction in (directions * 2)[startdir:startdir + 4]:
                if all(
                    (x + dx, y + dy) not in elves
                    for dx, dy in neighborhoods[direction]
                ):
                    dx, dy = direction
                    votes[(x + dx, y + dy)] += 1
                    moves[(x, y)] = (x + dx, y + dy)
                    break

    result = {}

    for (x, y), (tx, ty) in moves.items():
        if votes[(tx, ty)] == 1:
            result[(tx, ty)] = 1
        else:
            result[(x, y)] = 1

    return result

def count(elves):
    min_x = min(x for x, y in elves)
    max_x = max(x for x, y in elves)
    min_y = min(y for x, y in elves)
    max_y = max(y for x, y in elves)
    return sum(
        (x, y) not in elves
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    )

elves = {}

for y, line in enumerate(open(0)):
    for x, value in enumerate(line):
        if value == "#":
            elves[(x, y)] = 1

for rnd in range(10):
    elves = move(elves, rnd % 4)

print(count(elves))

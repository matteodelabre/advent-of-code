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

elves = {}

for y, line in enumerate(open(0)):
    for x, value in enumerate(line):
        if value == "#":
            elves[(x, y)] = 1

rnd = 0

while (result := move(elves, rnd % 4)) != elves:
    elves = result
    rnd += 1

print(rnd + 1)

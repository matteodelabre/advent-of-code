from itertools import cycle

width = 7

def ceiling(terrain):
    for i, row in enumerate(terrain):
        if row == ["."] * width:
            return i
    return len(terrain)

def collide(shape, terrain, left, up):
    if not (0 <= left and left + len(shape[0]) <= width):
        return True

    if up < 0:
        return True

    return any(
        (shape[dy][dx] == "#" and up + dy < len(terrain)
         and terrain[up + dy][left + dx] == "#")
        for dy in range(len(shape))
        for dx in range(len(shape[dy]))
    )

def fall(shape, terrain, jets):
    left = 2
    up = ceiling(terrain) + 3

    while len(terrain) <= up + len(shape):
        terrain.append(["."] * width)

    while True:
        direction = 1 if next(jets) == ">" else -1

        if not collide(shape, terrain, left + direction, up):
            left += direction

        if not collide(shape, terrain, left, up - 1):
            up -= 1
        else:
            break

    for dy in range(len(shape)):
        for dx in range(len(shape[dy])):
            if shape[dy][dx] == "#":
                terrain[up + dy][left + dx] = "#"

shapes = cycle((
    ("####",),
    (".#.", "###", ".#."),
    ("###", "..#", "..#"),
    ("#", "#", "#", "#"),
    ("##", "##"),
))
jets = cycle(open(0).read().strip())
terrain = []

for _ in range(2022):
    fall(next(shapes), terrain, jets)

print(ceiling(terrain))

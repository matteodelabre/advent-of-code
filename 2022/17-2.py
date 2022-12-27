from collections import deque
from itertools import cycle, chain

width = 7

def ceiling(terrain):
    for i, row in enumerate(terrain):
        if row == ["."] * width:
            return i
    return len(terrain)

def cross(terrain, start, seen):
    queue = deque([(0, start)])
    heights = {(0, start): start}

    while queue:
        x, y = queue.pop()

        for dx, dy in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
            tx, ty = x + dx, y + dy

            if (
                (tx, ty) not in seen
                and 0 <= tx < width
                and 0 <= ty < len(terrain)
                and terrain[ty][tx] == "#"
            ):
                heights[(tx, ty)] = min(heights[(x, y)], ty)
                queue.appendleft((tx, ty))
                seen.add((tx, ty))

    return max(
        (height for (x, y), height in heights.items() if x == width - 1),
        default=0
    )

def floor(terrain):
    seen = set()
    result = 0

    for y in range(len(terrain) - 1, -1, -1):
        if terrain[y][0] == "#":
            result = max(result, cross(terrain, y, seen))

    return result

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

def fall(shapes, terrain, jets):
    _, shape = next(shapes)
    left = 2
    up = ceiling(terrain) + 3

    while len(terrain) <= up + len(shape):
        terrain.append(["."] * width)

    while True:
        direction = 1 if next(jets)[1] == ">" else -1

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

    shift = floor(terrain)
    return terrain[shift:], shift

shapes = cycle(enumerate((
    ("####",),
    (".#.", "###", ".#."),
    ("###", "..#", "..#"),
    ("#", "#", "#", "#"),
    ("##", "##"),
)))
jets = cycle(enumerate(open(0).read().strip()))
terrain = []

step = 0
steps = 1_000_000_000_000
configs = {}
total = 0

while step < steps:
    shape_index, shape = next(shapes)
    jet_index, jet = next(jets)
    join_terrain = "".join("".join(row) for row in terrain)

    shapes = chain([(shape_index, shape)], shapes)
    jets = chain([(jet_index, jet)], jets)

    if (shape_index, jet_index, join_terrain) in configs:
        last_step, last_total = configs[(shape_index, jet_index, join_terrain)]

        delta_step = step - last_step
        jumps = (steps - step) // delta_step

        delta_total = total - last_total
        total += delta_total * jumps
        step += delta_step * jumps
    else:
        configs[(shape_index, jet_index, join_terrain)] = (step, total)

    terrain, shift = fall(shapes, terrain, jets)
    total += shift
    step += 1

print(total + ceiling(terrain))

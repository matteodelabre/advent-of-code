from itertools import product

grid = open(0).read().splitlines()

def at(pos):
    return grid[int(pos.imag)][int(pos.real)]

def in_grid(pos):
    return 0 <= int(pos.real) < len(grid[0]) and 0 <= int(pos.imag) < len(grid)

def find_start():
    for x, y in product(range(len(grid[0])), range(len(grid))):
        pos = complex(x, y)

        if at(pos) == "^":
            return pos

start = find_start()

def find_loops(block=None):
    pos = start
    velocity = -1j # vers le haut
    blocks = set()
    trail = set((pos, velocity))

    while True:
        if not in_grid(pos + velocity):
            return blocks

        if at(pos + velocity) == "#" or pos + velocity == block:
            velocity *= 1j # tourne à droite
        else:
            pos += velocity

            if block is None:
                blocks |= find_loops(pos)

            if (pos, velocity) in trail:
                return {block}

            trail.add((pos, velocity))

print(len(find_loops() - {start}))

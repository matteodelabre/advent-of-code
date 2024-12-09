from itertools import product

grid = open(0).read().splitlines()

def at(pos):
    return grid[int(pos.imag)][int(pos.real)]

def in_grid(pos):
    return 0 <= pos.real < len(grid[0]) and 0 <= pos.imag < len(grid)

def find_start():
    for x, y in product(range(len(grid[0])), range(len(grid))):
        pos = complex(x, y)

        if at(pos) == "^":
            return pos

pos = find_start()
velocity = -1j # vers le haut
trail = set()

while True:
    trail.add(pos)

    if not in_grid(pos + velocity):
        break

    if at(pos + velocity) == "#":
        velocity *= 1j # tourne à droite
    else:
        print(f"x={int(pos.real)} y={int(pos.imag)}")
        pos += velocity

print(len(trail))

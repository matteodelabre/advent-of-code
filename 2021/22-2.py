import re
from math import prod
from itertools import product

def empty(cube): return any(axis[0] > axis[1] for axis in cube)
def size(cube): return prod(axis[1] - axis[0] + 1 for axis in cube)
def clamp(source, operand):
    return tuple(
        (max(source_axis[0], operand_axis[0]),
         min(source_axis[1], operand_axis[1]))
        for source_axis, operand_axis in zip(source, operand)
    )

def subtract(source, operand):
    operand = clamp(source, operand)
    if empty(operand):
        return set((source,))
    else:
        return set(piece for piece in (
            ( # Front
                (source[0][0], operand[0][0] - 1),
                (source[1][0], source[1][1]),
                (source[2][0], source[2][1])
            ),
            ( # Back
                (operand[0][1] + 1, source[0][1]),
                (source[1][0], source[1][1]),
                (source[2][0], source[2][1])
            ),
            ( # Left
                (operand[0][0], operand[0][1]),
                (source[1][0], source[1][1]),
                (source[2][0], operand[2][0] - 1),
            ),
            ( # Right
                (operand[0][0], operand[0][1]),
                (source[1][0], source[1][1]),
                (operand[2][1] + 1, source[2][1]),
            ),
            ( # Down
                (operand[0][0], operand[0][1]),
                (source[1][0], operand[1][0] - 1),
                (operand[2][0], operand[2][1]),
            ),
            ( # Up
                (operand[0][0], operand[0][1]),
                (operand[1][1] + 1, source[1][1]),
                (operand[2][0], operand[2][1]),
            ),
        ) if not empty(piece))

regex = r"(on|off) x=([\d-]+)..([\d-]+),y=([\d-]+)..([\d-]+),z=([\d-]+)..([\d-]+)"
cubes = set()

try:
    while True:
        groups = re.match(regex, input()).groups()

        new_state = groups[0] == "on"
        x1, x2, y1, y2, z1, z2 = map(int, groups[1:])
        new_cube = ((x1, x2), (y1, y2), (z1, z2))

        # Subtract new cube from existing cubes
        next_cubes = set()
        for cube in cubes: next_cubes.update(subtract(cube, new_cube))

        # Add new cube if “on” state
        cubes = next_cubes
        if new_state: cubes.add(new_cube)
except EOFError:
    pass

print(sum(size(cube) for cube in cubes))

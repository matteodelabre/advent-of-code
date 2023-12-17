from itertools import chain

def beam_from(grid, start):
    stack = [start]
    seen = set()
    energized = set()

    while stack:
        pos, vel = stack.pop()
        i, j = int(pos.imag), int(pos.real)

        if (pos, vel) in seen:
            continue

        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            continue

        seen.add((pos, vel))
        energized.add(pos)

        match grid[i][j]:
            case "\\":
                if vel in (1, -1):
                    vel *= 1j
                else:
                    vel *= -1j

                stack.append((pos + vel, vel))

            case "/":
                if vel in (1, -1):
                    vel *= -1j
                else:
                    vel *= 1j

                stack.append((pos + vel, vel))

            case "|":
                if vel in (1, -1):
                    stack.append((pos + 1j, 1j))
                    stack.append((pos - 1j, -1j))
                else:
                    stack.append((pos + vel, vel))

            case "-":
                if vel in (1j, -1j):
                    stack.append((pos + 1, 1))
                    stack.append((pos - 1, -1))
                else:
                    stack.append((pos + vel, vel))

            case ".":
                stack.append((pos + vel, vel))

    return len(energized)

grid = open(0).read().splitlines()

print(max(
    beam_from(grid, start)
    for start in chain(
        chain.from_iterable(
            ((complex(0, i), 1), (complex(len(grid[0]) - 1, i), -1))
            for i in range(len(grid))
        ),
        chain.from_iterable(
            ((complex(j, 0), 1j), (complex(j, len(grid) - 1), -1j))
            for j in range(len(grid[0]))
        )
    )
))

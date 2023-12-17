grid = open(0).read().splitlines()

stack = [(0, 1)]
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

print(len(energized))

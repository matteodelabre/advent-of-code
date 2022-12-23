state = {}
floor = 0

for line in open(0):
    parts = line.split(" -> ")

    for start, end in zip(parts, parts[1:]):
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        floor = max(floor, y1, y2)

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                state[(x, y)] = 0

while (500, 0) not in state:
    pos = (500, 0)

    while True:
        down = (pos[0], pos[1] + 1)
        left = (pos[0] - 1, pos[1] + 1)
        right = (pos[0] + 1, pos[1] + 1)

        if down[1] == floor + 2: break
        elif down not in state: pos = down
        elif left not in state: pos = left
        elif right not in state: pos = right
        else: break

    state[pos] = 1

print(sum(state.values()))

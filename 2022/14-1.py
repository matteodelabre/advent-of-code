state = {}
oblivion = 0

for line in open(0):
    parts = line.split(" -> ")

    for start, end in zip(parts, parts[1:]):
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        oblivion = max(oblivion, y1, y2)

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                state[(x, y)] = 0

def grain():
    pos = (500, 0)

    while True:
        if pos[1] == oblivion:
            return False

        down = (pos[0], pos[1] + 1)
        left = (pos[0] - 1, pos[1] + 1)
        right = (pos[0] + 1, pos[1] + 1)

        if down not in state: pos = down
        elif left not in state: pos = left
        elif right not in state: pos = right
        else: break

    state[pos] = 1
    return True

while grain(): pass
print(sum(state.values()))

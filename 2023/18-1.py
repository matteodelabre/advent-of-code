pos = (0, 0)
edge = set([pos])
direcs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

extant_i = (0, 0)
extant_j = (0, 0)

for line in open(0):
    direc, count, color = line.split()
    direc = direcs[direc]
    count = int(count)

    for _ in range(count):
        pos = (pos[0] + direc[0], pos[1] + direc[1])
        extant_i = (min(extant_i[0], pos[0]), max(extant_i[1], pos[0] + 1))
        extant_j = (min(extant_j[0], pos[1]), max(extant_j[1], pos[1] + 1))
        edge.add(pos)

extant_i = (extant_i[0] - 1, extant_i[1] + 1)
extant_j = (extant_j[0] - 1, extant_j[1] + 1)

stack = [(extant_i[0], extant_j[0])]
seen = set()

while stack:
    i, j = stack.pop()

    for di, dj in direcs.values():
        ii = i + di
        jj = j + dj

        if (
            ii in range(*extant_i) and jj in range(*extant_j)
            and (ii, jj) not in edge and (ii, jj) not in seen
        ):
            stack.append((ii, jj))
            seen.add((ii, jj))

print(len(range(*extant_i)) * len(range(*extant_j)) - len(seen))

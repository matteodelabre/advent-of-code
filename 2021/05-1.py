lines = []

try:
    while True:
        (x1, y1), (x2, y2) = \
            map(lambda x: map(int, x.split(",")), input().split(" -> "))
        lines.append([[x1, y1], [x2, y2]])
except EOFError:
    pass

w = max(max(line[0][0], line[1][0]) + 1 for line in lines)
h = max(max(line[0][1], line[1][1]) + 1 for line in lines)
grid = [[0] * w for i in range(h)]

for line in lines:
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        continue

    dirx = 1 if line[0][0] < line[1][0] else -1
    diry = 1 if line[0][1] < line[1][1] else -1

    for x in range(line[0][0], line[1][0] + dirx, dirx):
        for y in range(line[0][1], line[1][1] + diry, diry):
            grid[y][x] += 1

print(sum(x > 1 for line in grid for x in line))

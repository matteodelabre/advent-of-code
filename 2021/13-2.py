points = set()

while line := input():
    points.add(tuple(map(int, line.split(","))))

try:
    while True:
        fold, divide = input().split("=")
        divide = int(divide)

        for x, y in points.copy():
            if fold == "fold along x" and x > divide:
                points.remove((x, y))
                points.add((divide - (x - divide), y))
            if fold == "fold along y" and y > divide:
                points.remove((x, y))
                points.add((x, divide - (y - divide)))
except EOFError:
    pass

min_x = min(x for x, y in points)
max_x = max(x for x, y in points)
min_y = min(y for x, y in points)
max_y = max(y for x, y in points)

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print("#" if (x, y) in points else ".", end="")
    print()

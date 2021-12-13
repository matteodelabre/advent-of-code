points = set()

while line := input():
    points.add(tuple(map(int, line.split(","))))

fold, divide = input().split("=")
divide = int(divide)

for x, y in points.copy():
    if fold == "fold along x" and x > divide:
        points.remove((x, y))
        points.add((divide - (x - divide), y))
    if fold == "fold along y" and y > divide:
        points.remove((x, y))
        points.add((x, divide - (y - divide)))

print(len(points))

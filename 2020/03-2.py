tree_map = []

try:
    while True:
        tree_map.append(input())
except EOFError:
    pass

w = len(tree_map[0])
result = 1

for (xdel, ydel) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    trees = 0
    x = 0
    y = 0

    while y < len(tree_map):
        if tree_map[y][x] == '#':
            trees += 1

        x = (x + xdel) % w
        y += ydel

    result *= trees

print(result)

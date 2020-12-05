tree_map = []

try:
    while True:
        tree_map.append(input())
except EOFError:
    pass

x = 0
w = len(tree_map[0])
trees = 0

for y in range(len(tree_map)):
    if tree_map[y][x] == '#':
        trees += 1

    x = (x + 3) % w

print(trees)

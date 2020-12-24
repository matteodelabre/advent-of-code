from collections import defaultdict
black_tiles = set()

try:
    while True:
        directions = input()
        q, r = 0, 0

        while directions:
            if directions[0] == 'w':
                q -= 1
                directions = directions[1:]
            elif directions[0] == 'e':
                q += 1
                directions = directions[1:]
            elif directions[:2] == 'nw':
                r -= 1
                directions = directions[2:]
            elif directions[:2] == 'se':
                r += 1
                directions = directions[2:]
            elif directions[:2] == 'sw':
                q -= 1
                r += 1
                directions = directions[2:]
            elif directions[:2] == 'ne':
                q += 1
                r -= 1
                directions = directions[2:]
            else:
                raise ValueError('Invalid direction')

        if (q, r) in black_tiles:
            black_tiles.remove((q, r))
        else:
            black_tiles.add((q, r))
except EOFError:
    pass

for i in range(100):
    next_black_tiles = set()
    black_neighbors = defaultdict(int)

    for q, r in black_tiles:
        black_neighbors[(q - 1, r)] += 1
        black_neighbors[(q + 1, r)] += 1
        black_neighbors[(q, r - 1)] += 1
        black_neighbors[(q, r + 1)] += 1
        black_neighbors[(q - 1, r + 1)] += 1
        black_neighbors[(q + 1, r - 1)] += 1

    for tile, neighbors in black_neighbors.items():
        if tile in black_tiles and neighbors in (1, 2) or \
                tile not in black_tiles and neighbors == 2:
            next_black_tiles.add(tile)

    black_tiles = next_black_tiles

print(len(black_tiles))

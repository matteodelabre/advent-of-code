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

print(len(black_tiles))

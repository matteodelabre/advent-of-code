seatmap = []

try:
    while True:
        seatmap.append(list(input().strip()))
except EOFError:
    pass

def iterate(seatmap):
    h = len(seatmap)
    w = len(seatmap[0])

    next_seatmap = [['.'] * w for r in range(h)]

    for r in range(h):
        for c in range(w):
            if seatmap[r][c] in ('L', '#'):
                active_neighbors = 0

                for y in range(r - 1, r + 2):
                    for x in range(c - 1, c + 2):
                        if (y != r or x != c) and y >= 0 and y < h \
                                and x >= 0 and x < w \
                                and seatmap[y][x] == '#':
                            active_neighbors += 1

                if seatmap[r][c] == 'L':
                    next_seatmap[r][c] = '#' if active_neighbors == 0 else 'L'
                else:
                    next_seatmap[r][c] = '#' if active_neighbors < 4 else 'L'

    return next_seatmap

next_seatmap = iterate(seatmap)

while seatmap != next_seatmap:
    seatmap = next_seatmap
    next_seatmap = iterate(seatmap)

print(sum(cell == '#' for row in seatmap for cell in row))

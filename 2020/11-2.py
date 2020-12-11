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

                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if y != 0 or x != 0:
                            d = 1

                            while r + d * y >= 0 and r + d * y < h \
                                    and c + d * x >= 0 and c + d * x < w \
                                    and seatmap[r + d * y][c + d * x] == '.':
                                d += 1

                            if r + d * y >= 0 and r + d * y < h \
                                    and c + d * x >= 0 and c + d * x < w \
                                    and seatmap[r + d * y][c + d * x] == '#':
                                active_neighbors += 1

                if seatmap[r][c] == 'L':
                    next_seatmap[r][c] = '#' if active_neighbors == 0 else 'L'
                else:
                    next_seatmap[r][c] = '#' if active_neighbors < 5 else 'L'

    return next_seatmap

next_seatmap = iterate(seatmap)

while seatmap != next_seatmap:
    seatmap = next_seatmap
    next_seatmap = iterate(seatmap)

print(sum(cell == '#' for row in seatmap for cell in row))

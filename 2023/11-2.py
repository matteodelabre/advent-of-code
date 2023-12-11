from itertools import combinations, starmap

def transpose(sky):
    return [
        "".join(sky[j][i] for j in range(len(sky)))
        for i in range(len(sky[0]))
    ]

def find_empty(sky):
    return {
        i
        for i in range(len(sky))
        if set(sky[i]) == {"."}
    }

sky = open(0).read().splitlines()
empty_lines = find_empty(sky)
empty_cols = find_empty(transpose(sky))
expansion = 1000000

def distance(start, end):
    si, ti = sorted((start[0], end[0]))
    sj, tj = sorted((start[1], end[1]))

    ei = sum(1 for di in range(si, ti + 1) if di in empty_lines)
    ej = sum(1 for dj in range(sj, tj + 1) if dj in empty_cols)

    return (
        ti - si - ei + ei * expansion
        + tj - sj - ej + ej * expansion
    )

stars = [
    (i, j)
    for i in range(len(sky))
    for j in range(len(sky[0]))
    if sky[i][j] == "#"
]

print(sum(starmap(distance, combinations(stars, r=2))))

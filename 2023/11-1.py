from itertools import combinations, starmap

def transpose(sky):
    return [
        "".join(sky[j][i] for j in range(len(sky)))
        for i in range(len(sky[0]))
    ]

def double(sky):
    i = 0
    
    while i < len(sky):
        if set(sky[i]) == {"."}:
            sky.insert(i, sky[i])
            i += 1

        i += 1

    return sky

sky = open(0).read().splitlines()
sky = double(transpose(double(sky)))

def distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

stars = [
    (i, j)
    for i in range(len(sky))
    for j in range(len(sky[0]))
    if sky[i][j] == "#"
]

print(sum(starmap(distance, combinations(stars, r=2))))

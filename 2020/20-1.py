import math
import numpy as np
from itertools import product
from collections import defaultdict

# Read available tiles
tiles = {}
current_id = None
current_tile = []

try:
    while True:
        line = input()

        if not line:
            tiles[current_id] = np.array(current_tile)
            current_id = None
            current_tile = []
        elif line[:4] == 'Tile':
            current_id = int(line[5:-1])
        else:
            current_tile.append(list(line))
except EOFError:
    pass

dir_up = 0
dir_right = 1
dir_down = 2
dir_left = 3
dirs = (dir_up, dir_right, dir_down, dir_left)
dir_vecs = {dir_up: (-1, 0), dir_right: (0, 1), dir_down: (1, 0), dir_left: (0, -1)}

rot_0 = 0
rot_90 = 1
rot_180 = 2
rot_270 = 3
rots = (rot_0, rot_90, rot_180, rot_270)

flip_0 = False
flip_lr = 0
flip_ud = 1
flips = (flip_0, flip_lr, flip_ud)

# Find tile neighbors
neighbors = defaultdict(lambda: defaultdict(set))
keys = list(tiles.keys())

for rot1, flip1, rot2, flip2 in product(rots, flips, repeat=2):
    for i in range(len(keys)):
        key1 = keys[i]
        tile1 = np.rot90(tiles[key1], k=rot1)
        if flip1 != False: tile1 = np.flip(tile1, axis=flip1)

        for j in range(i + 1, len(keys)):
            key2 = keys[j]
            tile2 = np.rot90(tiles[key2], k=rot2)
            if flip2 != False: tile2 = np.flip(tile2, axis=flip2)

            if np.array_equal(tile1[0, :], tile2[-1, :]):
                neighbors[key1][(rot1, flip1)].add((dir_up, key2, rot2, flip2))
                neighbors[key2][(rot2, flip2)].add((dir_down, key1, rot1, flip1))
            elif np.array_equal(tile1[:, -1], tile2[:, 0]):
                neighbors[key1][(rot1, flip1)].add((dir_right, key2, rot2, flip2))
                neighbors[key2][(rot2, flip2)].add((dir_left, key1, rot1, flip1))
            elif np.array_equal(tile1[-1, :], tile2[0, :]):
                neighbors[key1][(rot1, flip1)].add((dir_down, key2, rot2, flip2))
                neighbors[key2][(rot2, flip2)].add((dir_up, key1, rot1, flip1))
            elif np.array_equal(tile1[:, 0], tile2[:, -1]):
                neighbors[key1][(rot1, flip1)].add((dir_left, key2, rot2, flip2))
                neighbors[key2][(rot2, flip2)].add((dir_right, key1, rot1, flip1))

# Find corner tiles
corners = set()

for key in neighbors:
    for state in neighbors[key]:
        if len(neighbors[key][state]) == 2:
            corners.add(key)

assert len(corners) == 4
print(math.prod(corners))

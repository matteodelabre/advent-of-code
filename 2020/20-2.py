import math
import numpy as np
from random import shuffle
from itertools import product
from collections import defaultdict
import sys

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

print('Finding tile neighbors…')
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

print('Finding corners…')
corners = set()

for key in neighbors:
    for state in neighbors[key]:
        if len(neighbors[key][state]) == 2:
            corners.add(key)

# Perform brute force on possible tilings
def search(state, remaining, i, j):
    if i == len(state):
        return state

    if j == len(state[i]):
        return search(state, remaining, i + 1, 0)

    if (i == 0 and j == 0) \
            or (i == 0 and j == len(state[j]) - 1) \
            or (i == len(state) - 1 and j == 0) \
            or (i == len(state) - 1 and j == len(state[j]) - 1):
        remaining_rnd = list(remaining & corners)
    else:
        remaining_rnd = list(remaining)

    rot_flip_rnd = list(product(rots, flips))
    shuffle(remaining_rnd)
    shuffle(rot_flip_rnd)

    for rot, flip in rot_flip_rnd:
        for key in remaining_rnd:
            local_neighb = neighbors[key][(rot, flip)]
            valid = True

            for direc in dirs:
                di, dj = dir_vecs[direc]

                if i + di >= 0 and i + di < len(state) \
                        and j + dj >= 0 and j + dj < len(state[i]) \
                        and state[i + di][j + dj] is not None \
                        and (direc, *state[i + di][j + dj]) not in local_neighb:
                    valid = False
                    break

            if valid:
                state[i][j] = (key, rot, flip)
                remaining.remove(key)

                solution = search(state, remaining, i, j + 1)

                if solution is not None:
                    return solution

                remaining.add(key)
                state[i][j] = None

    return None

print('Searching for puzzle solution…')
side = int(math.sqrt(len(tiles)))
state = [[None] * side for i in range(side)]

solution = search(state, set(keys), 0, 0)

if solution is None:
    print('NO SOLUTION')
    sys.exit()

print('Assembling solution…')
rows, cols = next(iter(tiles.values())).shape
rows -= 2
cols -= 2
image = np.ndarray((side * rows, side * cols), dtype='U1')

for i, j in product(range(side), repeat=2):
    key, rot, flip = solution[i][j]
    tile = np.rot90(tiles[key], k=rot)
    if flip != False: tile = np.flip(tile, axis=flip)
    image[i * rows:(i + 1) * rows, j * cols:(j + 1) * cols] = tile[1:-1, 1:-1]

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]

def is_monster(array):
    if array.shape[0] < len(monster):
        return False

    if array.shape[1] < len(monster[0]):
        return False

    for i in range(len(monster)):
        for j in range(len(monster[i])):
            if monster[i][j] == '#' and array[i][j] != '#':
                return False

    return True

print('Finding monsters…')

for rot, flip in product(rots, flips):
    cur_image = np.rot90(image, k=rot)
    if flip != False: cur_image = np.flip(cur_image, axis=flip)

    monsterless_image = np.copy(cur_image)
    has_monsters = False

    for i in range(cur_image.shape[0]):
        for j in range(cur_image.shape[1]):
            if is_monster(cur_image[i:, j:]):
                has_monsters = True

                for di in range(len(monster)):
                    for dj in range(len(monster[di])):
                        if monster[di][dj] == '#':
                            monsterless_image[i + di, j + dj] = '.'

    if has_monsters:
        break

unique, counts = np.unique(monsterless_image, return_counts=True)
chars_count = dict(zip(unique, counts))

print(chars_count['#'])

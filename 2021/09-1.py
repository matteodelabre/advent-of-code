hmap = []

try:
    while True:
        hmap.append(input())
except EOFError:
    pass

w = len(hmap[0])
h = len(hmap)
t = 0

def low(i, j):
    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if hmap[ni][nj] <= hmap[i][j]: return False
    return True

for i in range(h):
    for j in range(w):
        if low(i, j):
            t += int(hmap[i][j]) + 1

print(t)

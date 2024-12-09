grid = open(0).read().splitlines()

def at(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    else:
        return " "

total = 0
pattern = "XMAS"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                scan = "".join(
                    at(i + di * k, j + dj * k)
                    for k in range(4)
                )
                total += (scan == pattern)

print(total)

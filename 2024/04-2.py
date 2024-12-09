grid = open(0).read().splitlines()

def at(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    else:
        return " "

total = 0
pattern = {"M", "S"}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        total += (
            at(i, j) == "A"
            and {at(i - 1, j - 1), at(i + 1, j + 1)} == pattern
            and {at(i - 1, j + 1), at(i + 1, j - 1)} == pattern
        )

print(total)

total = 0

for line in open(0):
    _, data = line.split(": ")
    winning, actual = data.split(" | ")

    winning = set(map(int, winning.split()))
    actual = set(map(int, actual.split()))

    count = len(winning & actual)

    if count > 0:
        total += 2 ** (count - 1)

print(total)

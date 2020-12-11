from collections import Counter

jolts = []

try:
    while True:
        jolts.append(int(input()))
except EOFError:
    pass

jolts.sort()
jolts = [0] + jolts + [jolts[-1] + 3]
counts = Counter()

for i in range(1, len(jolts)):
    counts[jolts[i] - jolts[i - 1]] += 1

assert len(counts) == 2
assert 1 in counts
assert 3 in counts

print(counts[1] * counts[3])

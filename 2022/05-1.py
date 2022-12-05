from collections import defaultdict
from re import findall

lines = open(0).read().splitlines()
split = lines.index("")
stacks = defaultdict(list)

for line in lines[:split - 1][::-1]:
    for i in range(1, len(line), 4):
        if line[i] != " ":
            stacks[i // 4 + 1].append(line[i])

for line in lines[split + 1:]:
    count, start, end = map(int, findall("\d+", line))

    for _ in range(count):
        item = stacks[start].pop()
        stacks[end].append(item)

print("".join([stacks[i][-1] for i in range(1, len(stacks) + 1)]))

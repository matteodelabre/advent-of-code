from functools import cache

@cache
def count(line, groups):
    if not groups:
        return int("#" not in line)

    group = groups[0]
    rest = groups[1:]
    ways = 0

    for i in range(len(line) - group + 1):
        candidate = line[i:i + group]

        if (
            candidate.replace("?", "#") == "#" * group
            and (i + group == len(line) or line[i + group] in "?.")
        ):
            ways += count(line[i + group + 1:], rest)

        if candidate.startswith("#"):
            break

    return ways

total = 0

for line in open(0):
    pattern, groups = line.split()
    pattern = "?".join((pattern,) * 5)

    groups = tuple(map(int, groups.split(",")))
    groups *= 5

    total += count(pattern, groups)

print(total)

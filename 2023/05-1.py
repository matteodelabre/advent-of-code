seeds = list(map(int, input().split(": ")[1].split()))

# Read rulesets
rulesets = []
end = False
input()

while not end:
    input()
    rules = []

    try:
        while (line := input()):
            rules.append(tuple(map(int, line.split())))
    except EOFError:
        end = True

    rulesets.append(rules)

# Apply rulesets
for rules in rulesets:
    for i in range(len(seeds)):
        for target_start, map_start, size in rules:
            if map_start <= seeds[i] < map_start + size:
                seeds[i] = seeds[i] - map_start + target_start
                break

print(min(seeds))

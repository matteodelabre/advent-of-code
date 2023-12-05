# Read initial seeds
data = list(map(int, input().split(": ")[1].split()))
intervals = [
    (start, start + length)
    for start, length in zip(data[::2], data[1::2])
]

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
def add(data, start, end):
    if start < end:
        data.append((start, end))

for rules in rulesets:
    mapped = []

    for target_start, map_start, size in rules:
        j = 0
        map_shift = target_start - map_start

        while j < len(intervals):
            start, end = intervals[j]

            if start <= map_start <= map_start + size <= end:
                del intervals[j]
                add(intervals, start, map_start)
                add(intervals, map_start + size, end)
                add(mapped, target_start, target_start + size)

            elif map_start <= start < map_start + size <= end:
                del intervals[j]
                add(intervals, map_start + size, end)
                add(mapped, start + map_shift, target_start + size)

            elif start <= map_start < end <= map_start + size:
                del intervals[j]
                add(intervals, start, map_start)
                add(mapped, target_start, end + map_shift)
            
            elif map_start <= start <= end <= map_start + size:
                del intervals[j]
                add(mapped, start + map_shift, end + map_shift)

            else:
                j += 1

    intervals += mapped
    print(intervals)

print(min(low for low, high in intervals))

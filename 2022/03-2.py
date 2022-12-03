def priority(item):
    return (
        ord(item) - ord("a") + 1 if "a" <= item <= "z"
        else ord(item) - ord("A") + 27 if "A" <= item <= "Z"
        else 0
    )

total = 0
lines = iter(open(0))

for l1, l2, l3 in zip(lines, lines, lines):
    shared = set(l1) & set(l2) & set(l3)
    total += sum(map(priority, shared))

print(total)

def priority(item):
    return (
        ord(item) - ord("a") + 1 if "a" <= item <= "z"
        else ord(item) - ord("A") + 27 if "A" <= item <= "Z"
        else 0
    )

total = 0

for line in open(0):
    half = len(line) // 2
    share = set(line[:half]) & set(line[half:])
    total += sum(map(priority, share))

print(total)

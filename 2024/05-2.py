from functools import cmp_to_key

rules, updates = open(0).read().strip().split("\n\n")
rules = [rule.split("|") for rule in rules.split("\n")]

def compare(i, j):
    if [i, j] in rules: return -1
    elif [j, i] in rules: return 1
    else: return 0

total = 0

for update in updates.split("\n"):
    pages = update.split(",")
    ordered = sorted(pages, key=cmp_to_key(compare))

    if pages != ordered:
        total += int(ordered[len(ordered) // 2])

print(total)

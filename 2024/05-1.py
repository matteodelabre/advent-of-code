rules, updates = open(0).read().strip().split("\n\n")
rules = [rule.split("|") for rule in rules.split("\n")]

total = 0

for update in updates.split("\n"):
    pages = update.split(",")

    if all(
        [pages[i], pages[j]] in rules
        for i in range(len(pages))
        for j in range(i + 1, len(pages))
    ):
        total += int(pages[len(pages) // 2])

print(total)

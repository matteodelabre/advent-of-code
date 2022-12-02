total = 0

for line in open(0).readlines():
    them, us = line.split()
    them = ord(them) - ord("A")
    us = ord(us) - ord("X")

    total += us + 1

    if us == them:
        total += 3
    elif us == (them + 1) % 3:
        total += 6

print(total)

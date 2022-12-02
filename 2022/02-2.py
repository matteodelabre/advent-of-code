total = 0

for line in open(0).readlines():
    them, action = line.split()
    them = ord(them) - ord("A")

    match action:
        case "X":
            us = (them + 2) % 3
        case "Y":
            total += 3
            us = them
        case "Z":
            total += 6
            us = (them + 1) % 3

    total += us + 1

print(total)

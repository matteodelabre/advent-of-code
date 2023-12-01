total = 0

for line in open(0):
    for first in line:
        if first.isdigit():
            break

    for last in reversed(line):
        if last.isdigit():
            break
    
    total += int(first + last)

print(total)

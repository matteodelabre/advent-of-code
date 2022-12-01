current = 0
elves = []

try:
    while True:
        line = input()

        if line:
            current += int(line)
        else:
            elves.append(current)
            current = 0
except EOFError:
    pass

elves.append(current)
print(sum(sorted(elves)[::-1][:3]))

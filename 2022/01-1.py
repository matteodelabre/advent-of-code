current = 0
best = 0

try:
    while True:
        line = input()

        if line:
            current += int(line)
            best = max(current, best)
        else:
            current = 0
except EOFError:
    pass

print(best)

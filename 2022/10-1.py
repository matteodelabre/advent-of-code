register = 1
total = 0
cycle = 0

for line in open(0):
    instr = line.split()

    match instr:
        case ["addx", value]: duration = 2
        case ["noop"]: duration = 1

    for _ in range(duration):
        cycle += 1

        if cycle % 40 == 20:
            total += cycle * register

    match instr:
        case ["addx", value]:
            register += int(value)

print(total)

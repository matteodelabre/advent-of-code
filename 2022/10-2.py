register = 1
scan_len = 40
screen = [["."] * scan_len for _ in range(6)]
cur_x = cur_y = 0

for line in open(0):
    instr = line.split()

    match instr:
        case ["addx", value]: duration = 2
        case ["noop"]: duration = 1

    for _ in range(duration):
        if register <= cur_x + 1 < register + 3:
            screen[cur_y][cur_x] = "#"

        cur_x += 1
        cur_y += cur_x // scan_len
        cur_x %= scan_len

    match instr:
        case ["addx", value]:
            register += int(value)

for line in screen:
    print("".join(line))

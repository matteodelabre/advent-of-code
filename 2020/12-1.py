x = 0
y = 0
d = 0

def angle_vec(d):
    if d == 0:
        return (1, 0)
    elif d == 90:
        return (0, 1)
    elif d == 180:
        return (-1, 0)
    elif d == 270:
        return (0, -1)
    else:
        raise ValueError(f'Invalid angle {d}')

try:
    while True:
        line = input().strip()
        cmd = line[0]
        data = int(line[1:])

        if cmd == 'N':
            y += data
        elif cmd == 'S':
            y -= data
        elif cmd == 'E':
            x += data
        elif cmd == 'W':
            x -= data
        elif cmd == 'L':
            d = (d + data) % 360
        elif cmd == 'R':
            d = (d + 360 - data) % 360
        elif cmd == 'F':
            dx, dy = angle_vec(d)
            x += dx * data
            y += dy * data
        else:
            raise ValueError(f'Invalid command {cmd}')
except EOFError:
    pass

print(abs(x) + abs(y))

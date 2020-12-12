x = 0
y = 0
wx = 10
wy = 1

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
            wy += data
        elif cmd == 'S':
            wy -= data
        elif cmd == 'E':
            wx += data
        elif cmd == 'W':
            wx -= data
        elif cmd in 'LR':
            if cmd == 'L': d = data
            else: d = 360 - data

            dx, dy = angle_vec(d)
            wx, wy = dx * wx - dy * wy, dy * wx + dx * wy
        elif cmd == 'F':
            x += wx * data
            y += wy * data
        else:
            raise ValueError(f'Invalid command {cmd}')
except EOFError:
    pass

print(abs(x) + abs(y))

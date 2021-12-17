from math import inf
import re

regex = r"target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)"
target = tuple(map(int, re.match(regex, input()).groups()))

def works(vx, vy):
    x, y = 0, 0

    while x <= target[1] and y >= target[2]:
        x += vx
        y += vy

        if vx != 0: vx -= vx // abs(vx)
        vy -= 1

        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return True

    return False

x_amp = max(map(abs, target[:2]))
y_amp = max(map(abs, target[2:]))

print(sum(
    works(vx, vy)
    for vx in range(1, x_amp + 1)
    for vy in range(-y_amp, y_amp + 1)
))

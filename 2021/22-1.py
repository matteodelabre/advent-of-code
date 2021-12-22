import re
from itertools import product

regex = r"(on|off) x=([\d-]+)..([\d-]+),y=([\d-]+)..([\d-]+),z=([\d-]+)..([\d-]+)"
reactor = set()

try:
    while True:
        state, x1, x2, y1, y2, z1, z2 = re.match(regex, input()).groups()

        for point in product(
            range(max(int(x1), -50), min(int(x2), 50) + 1),
            range(max(int(y1), -50), min(int(y2), 50) + 1),
            range(max(int(z1), -50), min(int(z2), 50) + 1),
        ):
            if state == "on": reactor.add(point)
            else: reactor.discard(point)
except EOFError:
    pass

print(len(reactor))

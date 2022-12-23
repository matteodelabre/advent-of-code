import re
from math import inf
digit = re.compile("\d+")

sensors = {}
beacons = set()
# seen = set()
min_x = inf
max_x = -inf

for line in open(0):
    sx, sy, bx, by = map(int, digit.findall(line))
    beacons.add((bx, by))

    ranging = abs(bx - sx) + abs(by - sy)
    sensors[(sx, sy)] = ranging
    min_x = min(min_x, sx)
    max_x = max(max_x, sx)


max_ranging = max(sensors.values())

#     for dx in range(sx - ranging, sx + ranging + 1):
#         for dy in range(sy - ranging, sy + ranging + 1):
#             if abs(dx - sx) + abs(dy - sy) <= ranging:
#                 seen.add((dx, dy))

qy = 2_000_000
print(sum(
    1
    for qx in range(min_x - max_ranging, max_x + max_ranging + 1)
    if (qx, qy) not in beacons and any(
        abs(qx - sx) + abs(qy - sy) <= ranging
        for ((sx, sy), ranging) in sensors.items()
    )
))


    # 1 for (x, y) in seen if y == 2000000 and (x, y) not in beacons))
# for x in range(min_x - max_range, max_x + max_range + 1):
#     for y in range


# print(sensors)

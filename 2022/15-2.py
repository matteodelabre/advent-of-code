import re
from bisect import bisect_left, bisect_right

project_low = lambda interval: interval[0]
project_high = lambda interval: interval[1]

def insert_interval(total, interval):
    if interval[0] >= interval[1]:
        return

    size = len(total)
    index_low = bisect_left(total, interval[0], key=project_high)
    index_high = bisect_right(total, interval[1], key=project_low) - 1

    if 0 <= index_low < size and interval[0] <= total[index_low][1]:
        interval = (
            min(interval[0], total[index_low][0]),
            interval[1],
        )

    if 0 <= index_high < size and interval[1] > total[index_high][0]:
        interval = (
            interval[0],
            max(interval[1], total[index_high][1]),
        )

    del total[index_low:index_high + 1]
    total.insert(index_low, interval)

digit = re.compile("[-\d]+")
size = 4_000_000

covers = [[] for _ in range(size + 1)]

for line in open(0):
    sx, sy, bx, by = map(int, digit.findall(line))
    span = abs(bx - sx) + abs(by - sy)

    for delta in range(-span, span + 1):
        width = span - abs(delta)
        cy = sy + delta
        cxs = max(0, sx - width)
        cxe = min(size, sx + width + 1)

        if 0 <= cy <= size:
            insert_interval(covers[cy], (cxs, cxe))

for y in range(size + 1):
    if len(covers[y]) > 1:
        x = covers[y][0][1]
        print(x * size + y)
        break

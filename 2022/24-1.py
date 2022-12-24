from math import inf, lcm
from collections import deque, defaultdict
from functools import lru_cache

initial = list(list(map(set, line[1:-2])) for line in open(0))[1:-1]
width = len(initial[0])
height = len(initial)
period = lcm(width, height)

@lru_cache(maxsize=None)
def state(step):
    result = [[set() for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if initial[y][x] == set("#"):
                result[y][x].add("#")
            elif ">" in initial[y][x]:
                result[y][(x + step) % width].add(">")
            elif "<" in initial[y][x]:
                result[y][(x - step) % width].add("<")
            elif "v" in initial[y][x]:
                result[(y + step) % height][x].add("v")
            elif "^" in initial[y][x]:
                result[(y - step) % height][x].add("^")

    return result

def escape(start, end):
    queue = deque([(*start, 0)])
    depth = defaultdict(int)
    depth[(*start, 0)] = 0

    while queue:
        x, y, step = queue.popleft()
        next_step = (step + 1) % period
        next_state = state(next_step)

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)):
            nx, ny = x + dx, y + dy

            if (nx, ny) == end:
                return depth[(x, y, step)] + 1

            if (
                0 <= nx < width
                and 0 <= ny < height
                and not next_state[ny][nx]
                and (nx, ny, next_step) not in depth
            ):
                depth[(nx, ny, next_step)] = depth[(x, y, step)] + 1
                queue.append((nx, ny, next_step))

    return inf

print(escape((0, -1), (width - 1, height)))

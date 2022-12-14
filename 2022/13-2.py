from json import loads
from functools import cmp_to_key

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if not isinstance(a, list): a = [a]
    if not isinstance(b, list): b = [b]

    for x, y in zip(a, b):
        if (result := compare(x, y)) != 0:
            return result

    return len(a) - len(b)

div1 = [[2]]
div2 = [[6]]

packets = [[], div1, div2] + [loads(line) for line in open(0) if line != "\n"]
packets.sort(key=cmp_to_key(compare))
print(packets.index(div1) * packets.index(div2))

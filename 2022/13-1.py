from json import loads

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if not isinstance(a, list): a = [a]
    if not isinstance(b, list): b = [b]

    for x, y in zip(a, b):
        if (result := compare(x, y)) != 0:
            return result

    return len(a) - len(b)

print(sum(
    i + 1
    for i, pair in enumerate(open(0).read().split("\n\n"))
    if compare(*map(loads, pair.split())) < 0
))

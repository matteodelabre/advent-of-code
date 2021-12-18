import json

def convert(n):
    if isinstance(n, list): return list(map(convert, n))
    else: return {"value": n}

def read(line): return convert(json.loads(line))

def find_first(n):
    if not isinstance(n, list): return n
    else: return find_first(n[0])

def find_last(n):
    if not isinstance(n, list): return n
    else: return find_last(n[1])

def explode(n, depth=0, prec=None, succ=None):
    if not isinstance(n, list):
        return (n, False)

    if depth < 4 or isinstance(n[0], list) or isinstance(n[1], list):
        n[0], exploded = explode(n[0], depth + 1, prec=prec, succ=n[1])
        if exploded: return (n, True)

        n[1], exploded = explode(n[1], depth + 1, prec=n[0], succ=succ)
        return (n, exploded)
    else:
        prec = find_last(prec)
        if prec is not None: prec["value"] += n[0]["value"]

        succ = find_first(succ)
        if succ is not None: succ["value"] += n[1]["value"]

        return ({"value": 0}, True)

def split(n):
    if not isinstance(n, list):
        value = n["value"]
        if value >= 10:
            return ([
                {"value": value // 2},
                {"value": value - value // 2}
            ], True)
        else:
            return (n, False)
    else:
        n[0], splitted = split(n[0])
        if splitted: return (n, True)

        n[1], splitted = split(n[1])
        return (n, splitted)

def reduce(n):
    exploded, splitted = True, True

    while exploded or splitted:
        n, exploded = explode(n)
        if not exploded: n, splitted = split(n)

    return n

def add(n1, n2): return reduce([n1, n2])

def mag(n):
    if not isinstance(n, list): return n["value"]
    else: return mag(n[0]) * 3 + 2 * mag(n[1])

n = add(read(input()), read(input()))

try:
    while True: n = add(n, read(input()))
except EOFError:
    pass

print(mag(n))

pos = list(map(int, input().split(",")))

def fuel(d):
    return d * (d + 1) // 2

def total(x):
    return sum(fuel(abs(pos[i] - x)) for i in range(len(pos)))

print(min(total(x) for x in range(min(pos), max(pos) + 1)))

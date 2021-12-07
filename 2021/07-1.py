pos = list(map(int, input().split(",")))

def total(x):
    return sum(abs(pos[i] - x) for i in range(len(pos)))

print(min(total(x) for x in range(min(pos), max(pos) + 1)))

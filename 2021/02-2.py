x = 0
d = 0
a = 0

try:
    while True:
        ins, dist = input().split()
        dist = int(dist)

        if ins == "forward":
            x += dist
            d += a * dist
        elif ins == "down":
            a += dist
        elif ins == "up":
            a -= dist
except EOFError:
    pass

print(x * d)

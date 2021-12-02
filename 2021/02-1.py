x = 0
d = 0

try:
    while True:
        ins, dist = input().split()
        dist = int(dist)

        if ins == "forward":
            x += dist
        elif ins == "down":
            d += dist
        elif ins == "up":
            d -= dist
except EOFError:
    pass

print(x * d)

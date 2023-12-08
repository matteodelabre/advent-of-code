from itertools import cycle

# Read network
instrs = cycle(input())
network = {}
input()

try:
    while True:
        start, targets = input().split(" = ")
        left, right = targets[1:-1].split(", ")
        network[start] = (left, right)
except EOFError:
    pass

# Compute number of steps needed to reach ZZZ
node = "AAA"
steps = 0

while node != "ZZZ":
    direction = "LR".index(next(instrs))
    node = network[node][direction]
    steps += 1

print(steps)

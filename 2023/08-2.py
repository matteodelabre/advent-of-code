from math import lcm
from itertools import cycle

# Read network
instrs = input()
network = {}
input()

try:
    while True:
        start, targets = input().split(" = ")
        left, right = targets[1:-1].split(", ")
        network[start] = (left, right)
except EOFError:
    pass

# Compute number of steps needed to reach a Z-node
def reach(node):
    steps = 0
    instrs_cycle = cycle(instrs)

    while not node.endswith("Z"):
        direction = "LR".index(next(instrs_cycle))
        node = network[node][direction]
        steps += 1

    return steps

print(lcm(*(
    reach(node)
    for node in network
    if node.endswith("A")
)))

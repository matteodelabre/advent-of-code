from itertools import product
from functools import reduce

def evaluate(res, op):
    match op:
        case ("+", value):
            return res + value

        case ("*", value):
            return res * value

total = 0

for line in open(0):
    target, values = line.split(": ")
    target = int(target)
    values = list(map(int, values.split()))

    for ops in product("+*", repeat=len(values) - 1):
        if target == reduce(evaluate, zip(ops, values[1:]), values[0]):
            total += target
            break

print(total)

from collections import Counter
from math import prod
import re

digit = re.compile("\d+")

# Parse input
items = {}
instrs = {}

for data in open(0).read().split("\n\n"):
    lines = data.splitlines()
    monkey = int(digit.search(lines[0]).group(0))

    items[monkey] = list(map(int, digit.findall(lines[1])))
    operation = lines[2].split(" = ")[1]
    instrs[monkey] = {
        "operation": eval("lambda old: " + operation),
        "test": int(digit.search(lines[3]).group(0)),
        "true": int(digit.search(lines[4]).group(0)),
        "false": int(digit.search(lines[5]).group(0)),
    }

# Simulate monkey dance
mod = prod(instr["test"] for instr in instrs.values())
activity = Counter()

for _ in range(10_000):
    for monkey, instr in instrs.items():
        for worry in items[monkey]:
            worry = instr["operation"](worry)
            worry %= mod

            if worry % instr["test"] == 0:
                items[instr["true"]].append(worry)
            else:
                items[instr["false"]].append(worry)

            activity[monkey] += 1

        items[monkey] = []

print(prod(value for monkey, value in activity.most_common(2)))

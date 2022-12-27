from collections import defaultdict
from fractions import Fraction
import re

sep = re.compile(r"[ :]+")
preds = {}
ops = {}

for line in open(0):
    target, *sources = sep.split(line.strip())

    if len(sources) == 3:
        preds[target] = [sources[0], sources[2]]
        ops[target] = sources[1]
    else:
        preds[target] = []
        ops[target] = int(sources[0])

def root_terms():
    seen = set()
    variables = set(["humn"])

    while len(seen) < len(preds):
        for monkey, pred in preds.items():
            if monkey not in seen and all(dep in seen for dep in pred):
                seen.add(monkey)

                if not isinstance(ops[monkey], int):
                    if pred[0] in variables or pred[1] in variables:
                        variables.add(monkey)

    pred = preds["root"]
    return pred if pred[0] in variables else pred[::-1]

def valueof(term, human):
    values = {"humn": human}

    while term not in values:
        for monkey, pred in preds.items():
            if monkey not in values and all(dep in values for dep in pred):
                op = ops[monkey]

                if isinstance(op, int):
                    values[monkey] = op
                else:
                    pred1, pred2 = pred
                    match op:
                        case "+": values[monkey] = values[pred1] + values[pred2]
                        case "-": values[monkey] = values[pred1] - values[pred2]
                        case "*": values[monkey] = values[pred1] * values[pred2]
                        case "/": values[monkey] = Fraction(values[pred1], values[pred2])

    return values[term]

variable, constant = root_terms()
base = valueof(variable, 0)
step = valueof(variable, 1) - base
target = valueof(constant, 0)
print((target - base) / step)

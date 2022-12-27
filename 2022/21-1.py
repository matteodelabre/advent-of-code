from collections import defaultdict
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

values = {}

while len(values) < len(preds):
    for monkey, pred in preds.items():
        if all(dep in values for dep in pred):
            op = ops[monkey]

            if isinstance(op, int):
                values[monkey] = op
            else:
                pred1, pred2 = pred
                match op:
                    case "+": values[monkey] = values[pred1] + values[pred2]
                    case "-": values[monkey] = values[pred1] - values[pred2]
                    case "*": values[monkey] = values[pred1] * values[pred2]
                    case "/": values[monkey] = values[pred1] // values[pred2]

print(values["root"])

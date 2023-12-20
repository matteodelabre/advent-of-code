maxvalue = 4001

workflows, parts = open(0).read().split("\n\n")
workflows = {
    workflow.split("{")[0]: workflow.split("{")[1][:-1].split(",")
    for workflow in workflows.splitlines()
}

def tighten(bounds, variable, low, high):
    result = bounds.copy()
    result[variable] = (max(result[variable][0], low), min(result[variable][1], high))
    return result

def reach(cur, bounds):
    if cur == "A":
        return [bounds]

    if cur == "R":
        return []

    workflow = workflows[cur]
    total = []

    for step in workflow:
        if ":" in step:
            cond, foll = step.split(":")

            if "<" in cond:
                kind, high = cond.split("<")
                high = int(high)
                current = tighten(bounds, kind, 1, high)
                bounds = tighten(bounds, kind, high, maxvalue)
            else:
                kind, low = cond.split(">")
                low = int(low) + 1
                current = tighten(bounds, kind, low, maxvalue)
                bounds = tighten(bounds, kind, 1, low)

            total += reach(foll, current)
        else:
            total += reach(step, bounds)

    return total

from math import prod

bounds = {kind: (1, maxvalue) for kind in "xmas"}
print(sum(
    prod(hi - low for low, hi in line.values())
    for line in reach("in", bounds)
))

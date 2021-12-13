from itertools import product
from collections import defaultdict
graph = defaultdict(set)

try:
    while True:
        in_node, out_node = input().split("-")
        graph[in_node].add(out_node)
        graph[out_node].add(in_node)
except EOFError:
    pass

paths = {node: set() for node in graph}
paths["start"].add(("start",))

def max_small_repeats(path):
    return max(path.count(node)
        for node in graph if node.islower())

changed = True

while changed:
    changed = False

    for in_node in graph:
        if in_node == "end":
            continue

        for path, out_node in product(paths[in_node], graph[in_node]):
            if out_node in ("start", "end") and out_node in path:
                continue

            if out_node.islower() and path.count(out_node) >= 1 and \
                    max_small_repeats(path) >= 2:
                continue

            new_path = path + (out_node,)

            if new_path not in paths[out_node]:
                changed = True
                paths[out_node].add(new_path)

print(len(paths["end"]))

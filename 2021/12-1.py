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

changed = True

while changed:
    changed = False

    for in_node in graph:
        for path, out_node in product(paths[in_node], graph[in_node]):
            if out_node.islower() and out_node in path:
                continue

            new_path = path + (out_node,)

            if new_path not in paths[out_node]:
                changed = True
                paths[out_node].add(new_path)

print(len(paths["end"]))

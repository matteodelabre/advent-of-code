class Node:
    def __init__(self, label, before, after):
        self.label = label
        self.before = before
        self.after = after

    def __repr__(self):
        return f'{self.label}'

# Build the circular list and the lookup table
line = input()
first = Node(int(line[0]), None, None)
last = first
lookup = {first.label: first}

for label in line[1:]:
    node = Node(int(label), last, None)
    lookup[int(label)] = node
    last.after = node
    last = node

for i in range(10, 1_000_001):
    node = Node(i, last, None)
    lookup[i] = node
    last.after = node
    last = node

first.before = last
last.after = first
cur = first

for i in range(10_000_000):
    if i % 1_000_000 == 0 and i > 0:
        print(f'Progress: {i} moves…')

    # Splice the next three cups
    splice_start = cur.after
    splice_end = splice_start.after.after

    cur.after = splice_end.after
    splice_end.after.before = cur

    # Find the destination cup
    goal = cur.label - 1 if cur.label != 1 else 1_000_000

    while goal not in lookup \
            or goal == splice_start.label \
            or goal == splice_start.after.label \
            or goal == splice_start.after.after.label:
        goal = goal - 1 if goal != 1 else 1_000_000

    dest = lookup[goal]

    # Place the three cups after the destination
    dest.after.before = splice_end
    splice_end.after = dest.after
    dest.after = splice_start
    splice_start.before = dest

    # Advance to the next cup
    cur = cur.after

print(lookup[1].after.label * lookup[1].after.after.label)

class Node:
    def __init__(self, label, before, after):
        self.label = label
        self.before = before
        self.after = after

    def __repr__(self):
        return f'{self.label}'

# Build the circular list
line = input()
first = Node(int(line[0]), None, None)
last = first

for label in line[1:]:
    node = Node(int(label), last, None)
    last.after = node
    last = node

first.before = last
last.after = first
cur = first

for i in range(100):
    # Splice the next three cups
    splice_start = cur.after
    splice_end = splice_start.after.after

    cur.after = splice_end.after
    splice_end.after.before = cur

    # Find the destination cup
    dest = cur.after
    goal = cur.label - 1 if cur.label != 1 else 9

    while dest.label != goal:
        dest = dest.after

        if dest.label != goal and dest == cur:
            goal = goal - 1 if goal != 1 else 9

    # Place the three cups after the destination
    dest.after.before = splice_end
    splice_end.after = dest.after
    dest.after = splice_start
    splice_start.before = dest

    # Advance to the next cup
    cur = cur.after

# Display the list after cup one
cup_one = first

while cup_one.label != 1:
    cup_one = cup_one.after

cur = cup_one.after

while cur != cup_one:
    print(cur.label, end='')
    cur = cur.after

print()

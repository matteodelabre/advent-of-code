import re

field_regex = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')
valid_values = [False] * 1000
field_types = {}

# field types
line = input()

while line:
    name, s1, e1, s2, e2 = field_regex.match(line).groups()

    for i in range(int(s1), int(e1) + 1):
        valid_values[i] = True

    for i in range(int(s2), int(e2) + 1):
        valid_values[i] = True

    field_types[name] = (int(s1), int(e1), int(s2), int(e2))
    line = input()

# my ticket
input()
ticket = list(map(int, input().split(',')))
input()

# guess types positions
input()
possible_types = [set(field_types.keys()) for i in range(len(ticket))]

try:
    while True:
        vals = list(map(int, input().split(',')))

        if all(map(lambda val: valid_values[val], vals)):
            for i in range(len(vals)):
                possible_types[i] = {
                    typ
                    for typ in possible_types[i]
                    if (vals[i] >= field_types[typ][0] and
                        vals[i] <= field_types[typ][1]) or
                    (vals[i] >= field_types[typ][2] and
                        vals[i] <= field_types[typ][3])
                }
except EOFError:
    pass

# resolve
active = True

while active:
    active = False

    for i in range(len(ticket)):
        if type(possible_types[i]) == set and len(possible_types[i]) == 1:
            active = True
            possible_types[i] = next(iter(possible_types[i]))

            for j in range(len(ticket)):
                if i != j and type(possible_types[j]) == set:
                    possible_types[j].remove(possible_types[i])

# extract result
result = 1

for i in range(len(ticket)):
    if possible_types[i].startswith('departure'):
        result *= ticket[i]

print(result)

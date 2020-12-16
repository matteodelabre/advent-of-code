import re

field_regex = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')
valid_values = [False] * 1000

line = input()

while line:
    name, s1, e1, s2, e2 = field_regex.match(line).groups()

    for i in range(int(s1), int(e1) + 1):
        valid_values[i] = True

    for i in range(int(s2), int(e2) + 1):
        valid_values[i] = True

    line = input()

# ignore my ticket
input()
input()
input()

input()

invalid = 0

try:
    while True:
        vals = list(map(int, input().split(',')))

        for val in vals:
            if not valid_values[val]:
                invalid += val
except EOFError:
    pass

print(invalid)

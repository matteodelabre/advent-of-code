import re

rules = {}
line = input()

while line:
    colon = line.find(':')
    rules[int(line[:colon])] = list(map(
        lambda branch: branch.strip().split(' '),
        line[colon + 2:].split('|')
    ))

    line = input()

patterns = {}

def build_pattern(root):
    if root in patterns:
        return patterns[root]

    subpatterns = []

    for branch in rules[root]:
        subpattern = ''

        for item in branch:
            if item.isdigit():
                subpattern += build_pattern(int(item))
            else:
                subpattern += item[1]

        subpatterns.append(subpattern)

    if len(subpatterns) == 1:
        result = subpatterns[0]
    else:
        result = f'({"|".join(subpatterns)})'

    patterns[root] = result
    return result

pattern = re.compile(build_pattern(0))
valid = 0

try:
    while True:
        valid += pattern.fullmatch(input()) is not None
except EOFError:
    pass

print(valid)

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

regexes = []
pattern_l = build_pattern(42)
pattern_r = build_pattern(31)

for i in range(1, 100):
    regexes.append(re.compile(
        f'({pattern_l})+({pattern_l}){{{i}}}({pattern_r}){{{i}}}'
    ))

valid = 0

try:
    while True:
        line = input()

        for regex in regexes:
            if regex.fullmatch(line) is not None:
                valid += 1
                break
except EOFError:
    pass

print(valid)

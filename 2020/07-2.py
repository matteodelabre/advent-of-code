import re
from collections import defaultdict

rule_regex = re.compile(r'(.+) bags contain (.*).')
item_regex = re.compile(r'(\d+) (.+) bags?')

containing = defaultdict(list)

try:
    while True:
        line = input()
        container, contents_list = rule_regex.match(line).groups()

        if contents_list != 'no other bags':
            containing[container] = list(map(
                lambda item_str: item_regex.match(item_str).groups(),
                contents_list.split(', ')
            ))
except EOFError:
    pass

def count(root):
    global containing
    total = 0

    for multiplicity, item in containing[root]:
        total += int(multiplicity) * count(item)

    return 1 + total

print(count('shiny gold') - 1)

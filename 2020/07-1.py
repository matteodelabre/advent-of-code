import re
from collections import defaultdict

rule_regex = re.compile(r'(.+) bags contain (.*).')
item_regex = re.compile(r'\d+ (.+) bags?')

contained_by = defaultdict(list)

try:
    while True:
        line = input()
        container, contents_list = rule_regex.match(line).groups()

        if contents_list != 'no other bags':
            for item in map(
                    lambda item_str: item_regex.match(item_str).group(1),
                    contents_list.split(', ')
                ):
                contained_by[item].append(container)
except EOFError:
    pass

stack = ['shiny gold']
visited = set()

while stack:
    cur = stack.pop()
    visited.add(cur)

    for container in contained_by[cur]:
        if container not in visited:
            stack.append(container)

print(len(visited) - 1)

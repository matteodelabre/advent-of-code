import re

line_regex = re.compile(r'(.+) \(contains (.+)\)')
rules = []
all_ingreds = set()
all_allergs = set()

try:
    while True:
        ingreds_str, allergs_str = line_regex.match(input()).groups()
        ingreds = ingreds_str.split()
        allergs = allergs_str.split(', ')

        all_ingreds.update(ingreds)
        all_allergs.update(allergs)

        rules.append((ingreds, allergs))
except EOFError:
    pass

def check_rules(assign_allerg):
    for ingreds, allergs in rules:
        for allerg in allergs:
            if allerg in assign_allerg and assign_allerg[allerg] not in ingreds:
                return False

    return True

def search(assign_allerg, next_allergs, remain_ingred):
    if not next_allergs:
        return [assign_allerg]

    allerg = next_allergs[0]
    solutions = []

    for ingred in remain_ingred:
        assign_allerg[allerg] = ingred

        if check_rules(assign_allerg):
            solutions += search(
                assign_allerg.copy(),
                next_allergs[1:],
                remain_ingred - set((ingred,)))

    return solutions


solutions = search({}, list(all_allergs), all_ingreds)
assert len(solutions) == 1
solution = solutions[0]

print(','.join(map(lambda x: x[1], sorted(list(solution.items())))))

import re

fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
data = re.compile(r'([a-z]{3}):\S+')

current_fields = set()
valid = 0

try:
    while True:
        line = input().strip()

        if not line:
            if fields <= current_fields:
                valid += 1

            current_fields = set()
        else:
            for field in data.findall(line):
                current_fields.add(field)
except EOFError:
    pass

if fields <= current_fields:
    valid += 1

print(valid)

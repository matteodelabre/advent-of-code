import re

line_format = re.compile(r'([1-9][0-9]*)-([1-9][0-9]*) ([a-z]): ([a-z]*)')
valid = 0

try:
    while True:
        line = input()
        l, r, letter, pwd = line_format.match(line).groups()

        l = int(l) - 1
        r = int(r) - 1

        if (pwd[l] == letter) + (pwd[r] == letter) == 1:
            valid += 1
except EOFError:
    pass

print(valid)

import re
from collections import Counter

line_format = re.compile(r'([1-9][0-9]*)-([1-9][0-9]*) ([a-z]): ([a-z]*)')
valid = 0

try:
    while True:
        line = input()
        mini, maxi, letter, pwd = line_format.match(line).groups()

        mini = int(mini)
        maxi = int(maxi)
        hash_pwd = Counter(pwd)

        if hash_pwd[letter] >= mini and hash_pwd[letter] <= maxi:
            valid += 1
except EOFError:
    pass

print(valid)

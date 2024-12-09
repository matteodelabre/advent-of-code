import re
pattern = re.compile(r"mul\((\d+),(\d+)\)")
line = open(0).read()
print(sum(
    int(a) * int(b)
    for a, b in pattern.findall(line)
))

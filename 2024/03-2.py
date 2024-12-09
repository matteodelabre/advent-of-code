import re
pattern = re.compile(r"mul\((\d+),(\d+)\)|(do|don't)\(\)")
line = open(0).read()

enable = True
total = 0

for a, b, instr in pattern.findall(line):
    if instr == "do":
        enable = True
    elif instr == "don't":
        enable = False
    elif enable:
        total += int(a) * int(b)

print(total)

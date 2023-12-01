total = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract(line, index):
    if line[index].isdigit():
        return int(line[index])

    for value, digit in enumerate(digits):
        if line[index:].startswith(digit):
            return value + 1

    return None

for line in open(0):
    for index in range(len(line)):
        if (value := extract(line, index)) is not None:
            first = value
            break

    for index in range(len(line) - 1, -1, -1):
        if (value := extract(line, index)) is not None:
            last = value
            break
    
    total += int(str(first) + str(last))

print(total)

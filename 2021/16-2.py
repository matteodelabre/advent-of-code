from math import prod

def parse_literal(bits, i):
    result = ""

    while True:
        result += bits[i + 1 : i + 5]
        i += 5
        if bits[i - 5] == "0": break

    return i, int(result, 2)

def parse_operator(bits, i):
    ltype = bits[i]
    operands = []
    i += 1

    if ltype == "0":
        sublen = int(bits[i : i + 15], 2)
        i += 15
        end = i + sublen

        while i < end:
            i, value = parse(bits, i)
            operands.append(value)
    else:
        subpackets = int(bits[i : i + 11], 2)
        i += 11

        for _ in range(subpackets):
            i, value = parse(bits, i)
            operands.append(value)

    return i, operands

def parse(bits, i=0):
    version = int(bits[i : i + 3], 2)
    ptype = int(bits[i + 3 : i + 6], 2)
    i += 6

    if ptype == 4:
        i, value = parse_literal(bits, i)
        return i, value
    else:
        i, operands = parse_operator(bits, i)
        if ptype == 0: value = sum(operands)
        elif ptype == 1: value = prod(operands)
        elif ptype == 2: value = min(operands)
        elif ptype == 3: value = max(operands)
        elif ptype == 5: value = int(operands[0] > operands[1])
        elif ptype == 6: value = int(operands[0] < operands[1])
        else: value = int(operands[0] == operands[1])

    return i, value

bits = "".join(
    bin(int(digit, 16))[2:].zfill(4)
    for digit in input()
)
print(parse(bits)[1])

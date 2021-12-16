def parse_literal(bits, i):
    while bits[i] == "1":
        i += 5
    return i + 5

def parse_operator(bits, i):
    ltype = bits[i]
    total_version = 0
    i += 1

    if ltype == "0":
        sublen = int(bits[i : i + 15], 2)
        i += 15
        end = i + sublen

        while i < end:
            i, subver = parse(bits, i)
            total_version += subver
    else:
        subpackets = int(bits[i : i + 11], 2)
        i += 11

        for _ in range(subpackets):
            i, subver = parse(bits, i)
            total_version += subver

    return i, total_version

def parse(bits, i=0):
    version = int(bits[i : i + 3], 2)
    ptype = int(bits[i + 3 : i + 6], 2)
    i += 6

    if ptype == 4:
        i = parse_literal(bits, i)
        return i, version
    else:
        i, total_version = parse_operator(bits, i)
        return i, version + total_version

bits = "".join(
    bin(int(digit, 16))[2:].zfill(4)
    for digit in input()
)
print(parse(bits)[1])

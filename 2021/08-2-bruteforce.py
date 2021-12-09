digit_values = ("abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg")

def all_mappings(rem_from, rem_to):
    if not rem_from:
        yield {}
        return

    for to in rem_to:
        for mapping in all_mappings(rem_from[1:], rem_to - {to}):
            yield {**mapping, rem_from[0]: to}

def decode_one(output, mapping):
    return str(digit_values.index(
        "".join(sorted(min(mapping[segm]) for segm in output))
    ))

def is_valid(outputs, mapping):
    try:
        for output in observs + outputs:
            decode_one(output, mapping)
        return True
    except ValueError:
        return False

def decode_all(outputs, mapping):
    return int("".join(decode_one(output, mapping) for output in outputs))

result = 0

try:
    while True:
        observs, outputs = map(lambda x: x.split(), input().split(" | "))
        for mapping in all_mappings("abcdefg", set("abcdefg")):
            if is_valid(observs + outputs, mapping):
                result += decode_all(outputs, mapping)
except EOFError:
    pass

print(result)

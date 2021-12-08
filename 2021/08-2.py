# Possible mappings of a segment based on occurrences
segm_occurs = {
    4: set("e"), 6: set("b"), 7: set("dg"),
    8: set("ac"), 9: set("f"),
}

# Digits w/ unique number of segments
digit_lengths = {2: set("cf"), 3: set("acf"), 4: set("bcdf")}

# Map “normal” segment combinations to digit value
digit_values = (
    "abcefg", "cf", "acdeg", "acdfg", "bcdf",
    "abdfg", "abdefg", "acf", "abcdefg", "abcdfg",
)

all_segms = set("abcdefg")
result = 0

def deduce_mapping(observs, outputs):
    mapping = {segm: all_segms.copy() for segm in all_segms}

    # Map “easy” digits
    for observ in observs + outputs:
        if len(observ) in digit_lengths:
            choices = digit_lengths[len(observ)]
            for segm in observ:
                mapping[segm] &= choices

    # Use segment occurrences
    occurs = {
        segm: sum(observ.count(segm) for observ in observs)
        for segm in all_segms
    }

    for segm in all_segms:
        if occurs[segm] in segm_occurs:
            mapping[segm] &= segm_occurs[occurs[segm]]

    # Use uniqueness constraint
    changed = True

    while changed:
        changed = False

        for segm in all_segms:
            if len(mapping[segm]) == 1:
                mapped = min(mapping[segm])

                for other_segm in all_segms:
                    if segm != other_segm and mapped in mapping[other_segm]:
                        mapping[other_segm].remove(mapped)
                        changed = True

    return mapping

def decode_output(outputs, mapping):
    return int("".join(
        str(digit_values.index(
            "".join(sorted(min(mapping[segm]) for segm in output))
        ))
        for output in outputs
    ))

try:
    while True:
        observs, outputs = map(lambda x: x.split(), input().split(" | "))
        mapping = deduce_mapping(observs, outputs)
        result += decode_output(outputs, mapping)
except EOFError:
    pass

print(result)

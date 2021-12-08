digit_segms = tuple(map(set, (
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
)))
digit_unique_counts = {2: 1, 3: 7, 4: 4, 7: 8}
all_segms = "abcdefg"

def map_observ(mapping, observ):
    return digit_segms.index(set(sorted(min(mapping[segm]) for segm in observ)))

def mapping_copy(mapping):
    return {segm: choices.copy() for segm, choices in mapping.items()}

def search_mapping(mapping, observs):
    changed = True

    # Enforce unicity
    while changed:
        changed = False

        for segm in mapping:
            if len(mapping[segm]) == 1:
                mapped = min(mapping[segm])

                for other_segm in mapping:
                    if segm != other_segm and mapped in mapping[other_segm]:
                        mapping[other_segm].remove(mapped)

                        # Exhausted options
                        if not mapping[other_segm]:
                            return None

                        changed = True

    # Make choices if needed
    for segm in mapping:
        if len(mapping[segm]) > 1:
            for choice in mapping[segm]:
                try_mapping = mapping_copy(mapping)
                try_mapping[segm] = {choice}

                if (result := search_mapping(try_mapping, observs)) is not None:
                    return result

    # Check consistency with observations
    for observ in observs:
        try:
            map_observ(mapping, observ)
        except ValueError:
            return None

    return mapping

def make_direct_mapping(observs):
    mapping = {segm: set(all_segms) for segm in all_segms}

    for observ in observs:
        if len(observ) in digit_unique_counts:
            observ_segms = digit_segms[digit_unique_counts[len(observ)]]

            for choice in observ:
                mapping[choice] &= observ_segms

    return mapping

result = 0

try:
    while True:
        observs, outputs = map(lambda x: x.split(), input().split(" | "))
        mapping = make_direct_mapping(observs + outputs)
        mapping = search_mapping(mapping, observs + outputs)
        result += int("".join(
            str(map_observ(mapping, output))
            for output in outputs
        ))
except EOFError:
    pass

print(result)

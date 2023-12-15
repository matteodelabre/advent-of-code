def sort_segment(segment):
    return "O" * segment.count("O") + "." * segment.count(".")

def sort_line(line):
    return "#".join(sort_segment(segment) for segment in line.split("#"))

def sort(dish):
    return tuple(map(sort_line, dish))

def rotate_left(dish):
    return tuple(
        "".join(dish[j][len(dish[0]) - i - 1] for j in range(len(dish)))
        for i in range(len(dish[0]))
    )

def rotate_right(dish):
    return tuple(
        "".join(dish[len(dish) - j - 1][i] for j in range(len(dish)))
        for i in range(len(dish[0]))
    )

dish = tuple(map(tuple, open(0).read().splitlines()))
dish = rotate_right(sort(rotate_left(dish)))

print(sum(
    (len(dish) - index) * sum(cell == "O" for cell in line)
    for index, line in enumerate(dish)
))

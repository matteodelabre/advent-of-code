def sort_segment(segment):
    return "O" * segment.count("O") + "." * segment.count(".")

def sort_line(line):
    return "#".join(sort_segment(segment) for segment in line.split("#"))

def sort_dish(dish):
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

def cycle(dish):
    for _ in range(4):
        dish = sort_dish(dish)
        dish = rotate_right(dish)

    return dish

dish = tuple(map(tuple, open(0).read().splitlines()))
dish = rotate_left(dish)

seen = {}
max_cycles = 1_000_000_000

for i in range(max_cycles):
    if dish in seen:
        break

    seen[dish] = i
    dish = cycle(dish)

loop_start = seen[dish]
loop_end = i

for _ in range((max_cycles - loop_start) % (loop_end - loop_start)):
    dish = cycle(dish)

dish = rotate_right(dish)
print(sum(
    (len(dish) - index) * sum(cell == "O" for cell in line)
    for index, line in enumerate(dish)
))

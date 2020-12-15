numbers = list(map(int, input().split(',')))

i = 0
last_occs = {}
last_number = -1

while i < 2020:
    if i < len(numbers):
        if last_number >= 0:
            last_occs[last_number] = i

        last_number = numbers[i]
    else:
        if last_number in last_occs:
            next_number = i - last_occs[last_number]
            last_occs[last_number] = i
            last_number = next_number
        else:
            last_occs[last_number] = i
            last_number = 0

    i += 1

print(last_number)

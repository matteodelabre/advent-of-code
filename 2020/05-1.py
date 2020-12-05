def decode(desc, min_x=0, max_x=7, min_y=0, max_y=127):
    if min_x == max_x and min_y == max_y:
        return (min_x, min_y)

    if not desc:
        return (-1, -1)

    med_x = (min_x + max_x) // 2
    med_y = (min_y + max_y) // 2

    if desc[0] == 'F':
        return decode(desc[1:], min_x, max_x, min_y, med_y)
    elif desc[0] == 'B':
        return decode(desc[1:], min_x, max_x, med_y + 1, max_y)
    elif desc[0] == 'L':
        return decode(desc[1:], min_x, med_x, min_y, max_y)
    else:
        return decode(desc[1:], med_x + 1, max_x, min_y, max_y)

maxi = 0

try:
    while True:
        x, y = decode(input())
        maxi = max(maxi, y * 8 + x)
except EOFError:
    pass

print(maxi)

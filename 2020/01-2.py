rows = []

try:
    while True:
        rows.append(int(input()))
except EOFError:
    pass

rows.sort()
goal = 2020

l = 0
m = 1
r = len(rows) - 1

while l < len(rows) - 1:
    m = l + 1
    r = len(rows) - 1

    while rows[l] + rows[m] + rows[r] != goal and m < r:
        if rows[l] + rows[m] + rows[r] < goal:
            m += 1
        else:
            r -= 1

    if rows[l] + rows[m] + rows[r] == goal:
        break

    l += 1

if rows[l] + rows[m] + rows[r] == goal:
    print(rows[l] * rows[m] * rows[r])
else:
    print('FAIL')

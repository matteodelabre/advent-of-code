rows = []

try:
    while True:
        rows.append(int(input()))
except EOFError:
    pass

rows.sort()
goal = 2020

l = 0
r = len(rows) - 1

while rows[l] + rows[r] != goal and l < r:
    if rows[l] + rows[r] < goal:
        l += 1
    else:
        r -= 1

if rows[l] + rows[r] == goal:
    print(rows[l] * rows[r])
else:
    print('FAIL')

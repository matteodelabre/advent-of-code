from collections import deque
import sys

last_25 = deque()

for i in range(25):
    last_25.append(int(input()))

try:
    while True:
        nxt = int(input())

        i = 0
        j = 1

        while i < 25 and last_25[i] + last_25[j] != nxt:
            if j + 1 == 25:
                j = 0
                i += 1
            else:
                j += 1

        if i == 25:
            print(nxt)
            sys.exit()

        last_25.append(nxt)
        last_25.popleft()
except EOFError:
    pass

print('not found')

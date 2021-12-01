last = (100000, 100000, 100000)
result = 0

try:
    while True:
        cur = int(input())

        if sum(last) < sum(last[1:]) + cur:
            result += 1

        last = last[1:] + (cur,)
except EOFError:
    pass

print(result)

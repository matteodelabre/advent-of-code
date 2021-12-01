last = 100000
result = 0

try:
    while True:
        cur = int(input())

        if last < cur:
            result += 1

        last = cur
except EOFError:
    pass

print(result)

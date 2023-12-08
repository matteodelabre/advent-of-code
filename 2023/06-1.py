from math import sqrt, ceil, floor

times = list(map(int, input().split(":")[1].strip().split()))
records = list(map(int, input().split(":")[1].strip().split()))

result = 1

for time, record in zip(times, records):
    delta = sqrt(time ** 2 - 4 * record - 4)
    low = ceil((time - delta) / 2)
    high = floor((time + delta) / 2)
    result *= high - low + 1

print(result)

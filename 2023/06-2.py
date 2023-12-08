from math import sqrt, ceil, floor

time = int(input().split(":")[1].replace(" ", ""))
record = int(input().split(":")[1].replace(" ", ""))

delta = sqrt(time ** 2 - 4 * record - 4)
low = ceil((time - delta) / 2)
high = floor((time + delta) / 2)

print(high - low + 1)

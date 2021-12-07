from statistics import median_low, mean
from math import floor, ceil
pos = list(map(int, input().split(",")))
avg = ceil(mean(pos)) if mean(pos) < median_low(pos) else floor(mean(pos))
print(sum(abs(i - avg) * (abs(i - avg) + 1) // 2 for i in pos))

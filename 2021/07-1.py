from statistics import median_low
pos = list(map(int, input().split(",")))
med = median_low(pos)
print(sum(abs(i - med) for i in pos))

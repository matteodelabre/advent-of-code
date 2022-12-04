total = 0

for line in open(0):
    range1, range2 = line.split(",")
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    total += start1 <= end2 and end1 >= start2

print(total)

total = 0

for l in open(0):
    range1, range2 = l.split(",")
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    total += start1 <= start2 <= end2 <= end1 or start2 <= start1 <= end1 <= end2

print(total)

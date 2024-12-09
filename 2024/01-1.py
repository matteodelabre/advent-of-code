la, lb = zip(*(map(int, line.split()) for line in open(0)))
la = sorted(la)
lb = sorted(lb)
print(sum(abs(a - b) for a, b in zip(la, lb)))

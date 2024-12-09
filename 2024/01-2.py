la, lb = zip(*(map(int, line.split()) for line in open(0)))
print(sum(a * lb.count(a) for a in la))

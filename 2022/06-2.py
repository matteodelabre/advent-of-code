line = open(0).read()
size = 14

for i in range(len(line) - size):
    if len(set(line[i : i + size])) == size:
        print(i + size)
        break

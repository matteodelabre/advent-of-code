area = 0
boundary = 0
pos = 0

for line in open(0):
    color = line.split()[-1]
    count = int(color[2:-2], 16)
    boundary += count

    direc = (1j) ** int(color[-2])
    pos += count * direc

    if direc.real != 0:
        area += count * direc.real * pos.imag

print(abs(int(area)) + boundary // 2 + 1)

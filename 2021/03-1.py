zeroes = [0] * 12
ones = [0] * 12
digits = 0

try:
    while True:
        num = input()
        digits = len(num)

        for i, d in enumerate(num):
            zeroes[i] += d == "0"
            ones[i] += d == "1"
except EOFError:
    pass

gamma = ""
epsilon = ""

for i in range(digits):
    if zeroes[i] > ones[i]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

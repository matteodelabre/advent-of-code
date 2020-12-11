jolts = set()
max_jolt = 0

try:
    while True:
        num = int(input())
        max_jolt = max(max_jolt, num)
        jolts.add(num)
except EOFError:
    pass

target_jolt = max_jolt + 3
jolts.add(target_jolt)

arrs = [0] * (target_jolt + 1)
arrs[0] = 1

for i in range(1, target_jolt + 1):
    if i in jolts:
        arrs[i] = arrs[i - 1] + arrs[i - 2] + arrs[i - 3]

print(arrs[target_jolt])

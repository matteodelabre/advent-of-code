fishies = [0] * 9

for days in map(int, input().split(",")):
    fishies[days] += 1

for i in range(256):
    breed = fishies[0]
    fishies = fishies[1:] + [fishies[0]]
    fishies[6] += breed

print(sum(fishies))

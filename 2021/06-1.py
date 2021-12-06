fishies = list(map(int, input().split(",")))

def sim(fishies):
    for i in range(len(fishies)):
        if fishies[i] > 0:
            fishies[i] -= 1
        elif fishies[i] == 0:
            fishies.append(8)
            fishies[i] = 6

for i in range(80):
    sim(fishies)

print(len(fishies))

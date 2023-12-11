from itertools import accumulate

def predict(values):
    trail = []

    while not all(value == 0 for value in values):
        trail.append(values[0])
        values = [cur - prev for prev, cur in zip(values, values[1:])]

    values.append(0)

    for start in trail[::-1]:
        values = list(accumulate([start] + values))

    return values[-1]

print(sum(
    predict(list(map(int, line.split()))[::-1])
    for line in open(0)
))

import math

time = int(input())
buses = list(map(int, filter(lambda x: x != 'x', input().split(','))))

next_id = None
next_depart = float('inf')

for id in buses:
    depart = math.ceil(time / id) * id

    if depart < next_depart:
        next_id = id
        next_depart = depart

print(next_id * (next_depart - time))

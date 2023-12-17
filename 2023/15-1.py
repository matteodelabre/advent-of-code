from functools import reduce

def hash(data):
    return reduce(lambda prev, cur: ((prev + ord(cur)) * 17) % 256, data, 0)

print(sum(map(hash, input().split(","))))

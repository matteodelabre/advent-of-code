from functools import reduce

def hash(data):
    return reduce(lambda prev, cur: ((prev + ord(cur)) * 17) % 256, data, 0)

boxes = {i: {} for i in range(256)}

for instr in input().split(","):
    if instr.endswith("-"):
        name = instr[:-1]
        boxes[hash(name)].pop(name, None)
    else:
        name, length = instr.split("=")
        boxes[hash(name)][name] = int(length)

print(sum(
    (key + 1) * (slot + 1) * length
    for key, box in boxes.items()
    for slot, length in enumerate(box.values())
))

head = [0, 0]
tail = [0, 0]
visit = set()

for line in open(0):
    direct, dist = line.split()

    for _ in range(int(dist)):
        # Move head
        match direct:
            case "L": head[0] -= 1
            case "R": head[0] += 1
            case "U": head[1] += 1
            case "D": head[1] -= 1

        # Adjust tail position
        dx = abs(tail[0] - head[0])
        dy = abs(tail[1] - head[1])

        if dy > 1 or dx + dy > 2:
            tail[1] += (head[1] - tail[1]) / dy

        if dx > 1 or dx + dy > 2:
            tail[0] += (head[0] - tail[0]) / dx

        # Remember tail position
        visit.add(tuple(tail))

print(len(visit))

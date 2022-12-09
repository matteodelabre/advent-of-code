knots = [[0, 0] for i in range(10)]
visit = set()

for line in open(0):
    direct, dist = line.split()

    for _ in range(int(dist)):
        # Move head
        match direct:
            case "L": knots[0][0] -= 1
            case "R": knots[0][0] += 1
            case "U": knots[0][1] += 1
            case "D": knots[0][1] -= 1

        # Adjust trailing knots
        for i in range(len(knots) - 1):
            head = knots[i]
            tail = knots[i + 1]

            dx = abs(tail[0] - head[0])
            dy = abs(tail[1] - head[1])

            if dy > 1 or dx + dy > 2:
                tail[1] += (head[1] - tail[1]) / dy

            if dx > 1 or dx + dy > 2:
                tail[0] += (head[0] - tail[0]) / dx

        # Remember tail position
        visit.add(tuple(knots[-1]))

print(len(visit))

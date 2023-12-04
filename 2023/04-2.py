from collections import deque

cards = []
queue = deque()

for line in open(0):
    _, data = line.split(": ")
    winning, actual = data.split(" | ")

    winning = set(map(int, winning.split()))
    actual = set(map(int, actual.split()))

    cards.append(len(winning & actual))
    queue.append(len(cards))

total = 0

while queue:
    current = queue.popleft()
    size = cards[current - 1]
    queue.extend(range(current + 1, current + size + 1))
    total += 1

print(total)

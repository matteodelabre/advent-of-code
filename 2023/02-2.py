power = 0

for line in open(0):
    prefix, record = line.split(": ")
    _, game_id = prefix.split(" ")

    game_id = int(game_id)
    counts = {"red": 0, "green": 0, "blue": 0}

    for draw in record.split("; "):
        for record in draw.split(", "):
            count, color = record.split(" ")
            count = int(count)
            color = color.strip()
            counts[color] = max(counts[color], int(count))

    power += counts["red"] * counts["green"] * counts["blue"]

print(power)

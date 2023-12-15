def transpose(sky):
    return [
        "".join(sky[j][i] for j in range(len(sky)))
        for i in range(len(sky[0]))
    ]

def split(sky, i):
    span = min(i, len(sky) - i)
    return sky[i - span:i], sky[i:i + span][::-1]

def diff(sky1, sky2):
    return sum(
        sum(char1 != char2 for char1, char2 in zip(line1, line2))
        for line1, line2 in zip(sky1, sky2)
    )

def find(sky):
    return sum(i for i in range(len(sky)) if diff(*split(sky, i)) == 1)

images = [
    image.splitlines()
    for image in open(0).read().split("\n\n")
]

print(sum(
    100 * find(image) + find(transpose(image))
    for image in images
))

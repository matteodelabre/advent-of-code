def transpose(sky):
    return [
        "".join(sky[j][i] for j in range(len(sky)))
        for i in range(len(sky[0]))
    ]

def split(sky, i):
    span = min(i, len(sky) - i)
    return sky[i - span:i], sky[i:i + span][::-1]

def eq(sky1, sky2):
    return sky1 == sky2

def find(sky):
    return sum(i for i in range(len(sky)) if eq(*split(sky, i)))

images = [
    image.splitlines()
    for image in open(0).read().split("\n\n")
]

print(sum(
    100 * find(image) + find(transpose(image))
    for image in images
))

pos = {}
scores = {1: 0, 2: 0}
pos[1] = int(input().split(": ")[1])
pos[2] = int(input().split(": ")[1])

turn = 1
next_dice = 1
rolls = 0

def roll():
    global next_dice, rolls
    dice = next_dice
    next_dice = next_dice % 1000 + 1
    rolls += 1
    return dice

def move(p, delta):
    pos[p] = (pos[p] + delta - 1) % 10 + 1

while scores[1] < 1000 and scores[2] < 1000:
    move(turn, roll() + roll() + roll())
    scores[turn] += pos[turn]
    turn = turn % 2 + 1

if scores[1] >= 1000: print(scores[2] * rolls)
else: print(scores[1] * rolls)

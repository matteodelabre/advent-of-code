from collections import deque
import sys

deck_1 = deque()
input()
line = input()

while line:
    deck_1.appendleft(int(line))
    line = input()

deck_2 = deque()
input()

try:
    while True:
        deck_2.appendleft(int(input()))
except EOFError:
    pass

while deck_1 and deck_2:
    card_1 = deck_1.pop()
    card_2 = deck_2.pop()

    if card_1 < card_2:
        deck_2.appendleft(card_2)
        deck_2.appendleft(card_1)
    elif card_1 > card_2:
        deck_1.appendleft(card_1)
        deck_1.appendleft(card_2)
    else:
        print('DRAW')
        sys.exit()

winning_deck = deck_1 if deck_1 else deck_2
score = 0

for i, card in enumerate(winning_deck):
    score += (i + 1) * card

print(score)

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

def play(deck_1, deck_2):
    seen = set()

    while deck_1 and deck_2:
        if (tuple(deck_1), tuple(deck_2)) in seen:
            return 1, deck_1
        else:
            seen.add((tuple(deck_1), tuple(deck_2)))

        card_1 = deck_1.pop()
        card_2 = deck_2.pop()

        if card_1 <= len(deck_1) and card_2 <= len(deck_2):
            winner, _ = play(
                deque(list(deck_1)[-card_1:]),
                deque(list(deck_2)[-card_2:]))
        elif card_1 < card_2:
            winner = 2
        elif card_1 > card_2:
            winner = 1
        else:
            print('DRAW')
            sys.exit()

        if winner == 2:
            deck_2.appendleft(card_2)
            deck_2.appendleft(card_1)
        else:
            deck_1.appendleft(card_1)
            deck_1.appendleft(card_2)

    if not deck_1:
        return 2, deck_2
    else:
        return 1, deck_1

_, winning_deck = play(deck_1, deck_2)
score = 0

for i, card in enumerate(winning_deck):
    score += (i + 1) * card

print(score)

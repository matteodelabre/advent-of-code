from collections import Counter

values = "J23456789TQKA"

def strength(hand):
    counts = Counter(hand)
    jokers = counts.pop("J", 0)
    signature = [count for _, count in counts.most_common()] or [0]

    match signature:
        case [n]          if n == 5 - jokers: return 6
        case [n, 1]       if n == 4 - jokers: return 5
        case [n, 2]       if n == 3 - jokers: return 4
        case [n, 1, 1]    if n == 3 - jokers: return 3
        case [2, 2, 1]:                       return 2
        case [n, 1, 1, 1] if n == 2 - jokers: return 1
        case _:                               return 0

def hand_key(hand):
    return (strength(hand[0]), *(values.index(value) for value in hand[0]))

hands = [line.split() for line in open(0)]
hands.sort(key=hand_key)
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(hands)))

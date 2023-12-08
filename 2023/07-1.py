from collections import Counter

values = "23456789TJQKA"

def kind(hand):
    signature = [count for _, count in Counter(hand).most_common()]

    match signature:
        case [5]:          return 6
        case [4, 1]:       return 5
        case [3, 2]:       return 4
        case [3, 1, 1]:    return 3
        case [2, 2, 1]:    return 2
        case [2, 1, 1, 1]: return 1
        case _:            return 0

def hand_key(hand):
    return (kind(hand[0]), *(values.index(value) for value in hand[0]))

hands = [line.split() for line in open(0)]
hands.sort(key=hand_key)
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(hands)))

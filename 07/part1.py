letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def classify(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])

def calculate_winnings(hands_with_bids):
    sorted_hands = sorted(hands_with_bids, key=lambda x: strength(x[0]))
    total_winnings = sum(bid * (i + 1) for i, (_, bid) in enumerate(sorted_hands))
    return total_winnings

plays = []

for line in open('input.txt'):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

total_winnings = calculate_winnings(plays)
print(total_winnings)
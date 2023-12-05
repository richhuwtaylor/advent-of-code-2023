def calculate_points(card):
    _, numbers_str = card.split(":")
    winning_numbers, your_numbers = numbers_str.split("|")

    winning_numbers = set(map(int, winning_numbers.split()))
    your_numbers = list(map(int, your_numbers.split()))
    n_overlap = len(winning_numbers.intersection(your_numbers))
    
    if n_overlap == 0:
        return 0
    else:
        return 2 ** (n_overlap - 1)

def total_points(cards):
    total = 0
    for card in cards:
        total += calculate_points(card)
    return total

with open('input.txt') as f:
    cards = f.readlines()

total_points_value = total_points(cards)
print(total_points_value)
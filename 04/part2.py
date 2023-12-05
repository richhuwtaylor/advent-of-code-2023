scratchcards = {}

for i, card_line in enumerate(open('input.txt')):
    if i not in scratchcards:
        scratchcards[i] = 1

    card_numbers = card_line.split(":")[1].strip()
    winning_numbers, your_numbers = [list(map(int, numbers.split())) for numbers in card_numbers.split(" | ")]
    matches = sum(num in winning_numbers for num in your_numbers)

    for j in range(i + 1, i + matches + 1):
        scratchcards[j] = scratchcards.get(j, 1) + scratchcards[i]

total_scratchcards = sum(scratchcards.values())
print(total_scratchcards)
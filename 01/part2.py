import re

numbers = "one two three four five six seven eight nine".split()

pattern = "(?=(" + "|".join(numbers) + "|\\d))"

def convert_number(x):
    if x in numbers:
        return str(numbers.index(x) + 1)
    return x

with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = [*map(convert_number, re.findall(pattern, line))]
    total += int(digits[0] + digits[-1])

print(total)
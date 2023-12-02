with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = [i for i in line if i.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)
with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line_number, line in enumerate(lines):
    reveals = line.strip().split(": ")[1].split("; ")
    for reveal in reveals:
        color_counts = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for color_count in reveal.split(', '):
            count, color = color_count.split()
            color_counts[color] = int(count)
        if color_counts['red'] > 12 or color_counts['green'] > 13 or color_counts['blue'] > 14:
            break
    else:
        total += line_number + 1

print(total)

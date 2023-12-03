with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line_number, line in enumerate(lines):
    reveals = line.strip().split(": ")[1].split("; ")
    min_color_counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for reveal in reveals:
        color_counts = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for color_count in reveal.split(', '):
            count, color = color_count.split()
            color_counts[color] = int(count)
        for key in min_color_counts:
            min_color_counts[key] = max(min_color_counts[key], color_counts[key])
    
    total += min_color_counts['red'] * min_color_counts['green'] * min_color_counts['blue']
     
print(total)

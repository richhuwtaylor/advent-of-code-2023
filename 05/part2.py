input_data, *blocks = open('input.txt').read().split("\n\n")

initial_ranges = list(map(int, input_data.split(":")[1].split()))

seeds = []

for i in range(0, len(initial_ranges), 2):
    seeds.append((initial_ranges[i], initial_ranges[i] + initial_ranges[i + 1]))

for block in blocks:
    conversion_ranges = []
    for line in block.splitlines()[1:]:
        conversion_ranges.append(list(map(int, line.split())))
    new_seeds = []
    while seeds:
        start, end = seeds.pop()
        for dest_start, source_start, length in conversion_ranges:
            overlap_start = max(start, source_start)
            overlap_end = min(end, source_start + length)
            if overlap_start < overlap_end:
                new_seeds.append((overlap_start - source_start + dest_start, overlap_end - source_start + dest_start))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            new_seeds.append((start, end))
    seeds = new_seeds

print(min(seeds)[0])
input_data = open('input.txt').read().split("\n\n")

initial_seeds = list(map(int, input_data[0].split(":")[1].split()))

for block in input_data[1:]:
    conversion_ranges = []
    for line in block.splitlines()[1:]:
        conversion_ranges.append(list(map(int, line.split())))
    new_seeds = []
    for seed in initial_seeds:
        for dest_start, source_start, length in conversion_ranges:
            if source_start <= seed < source_start + length:
                new_seeds.append(seed - source_start + dest_start)
                break
        else:
            new_seeds.append(seed)
    initial_seeds = new_seeds

print(min(initial_seeds))
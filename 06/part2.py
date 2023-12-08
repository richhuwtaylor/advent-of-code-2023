def ways_to_beat_record(time, record_distance):
    ways = 0
    for hold_time in range(time):
        distance = hold_time * (time - hold_time)
        if distance > record_distance:
            ways += 1
    return ways

with open('input.txt', 'r') as file:
    lines = file.readlines()

race_times_concatenated = ''.join(lines[0].split()[1:])
record_distances_concatenated = ''.join(lines[1].split()[1:])

total_ways = ways_to_beat_record(int(race_times_concatenated), int(record_distances_concatenated))

print(total_ways)

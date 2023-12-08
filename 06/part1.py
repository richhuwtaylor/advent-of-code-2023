def ways_to_beat_record(time, record_distance):
    ways = 0
    for hold_time in range(time):
        distance = hold_time * (time - hold_time)
        if distance > record_distance:
            ways += 1
    return ways

with open('input.txt', 'r') as file:
    lines = file.readlines()

race_times = [int(x) for x in lines[0].split()[1:]]
record_distances = [int(x) for x in lines[1].split()[1:]]

total_ways = 1
for i in range(len(race_times)):
    ways = ways_to_beat_record(race_times[i], record_distances[i])
    total_ways *= ways

print(total_ways)

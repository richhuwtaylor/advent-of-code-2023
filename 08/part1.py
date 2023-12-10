def process_instructions(instructions, network):
    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        instruction = instructions[steps % len(instructions)]

        if instruction == "L":
            current_node = network[current_node][0]
        elif instruction == "R":
            current_node = network[current_node][1]

        steps += 1

    return steps

with open('input.txt', 'r') as file:
    lines = file.readlines()

instructions = lines[0].strip()
network = {}
for line in lines[2:]:
    parts = line.strip().split(" = ")
    node, connections = parts[0], parts[1][1:-1].split(", ")
    network[node] = tuple(connections)

result = process_instructions(instructions, network)
print(result)

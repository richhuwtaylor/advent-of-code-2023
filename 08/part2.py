from math import gcd

def parse_input(input_text):
    instructions, _, *rest = input_text.strip().splitlines()
    network = {}
    for line in rest:
        pos, targets = line.split(" = ")
        network[pos] = targets[1:-1].split(", ")
    return instructions, network

def find_lcm(nums):
    lcm = nums.pop()
    for num in nums:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

def find_steps_to_Z(steps, network):
    positions = [key for key in network if key.endswith("A")]
    cycles = []

    for current in positions:
        cycle = []

        current_steps = steps
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
                step_count += 1
                current = network[current][0 if current_steps[0] == "L" else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    return find_lcm([cycle[0] for cycle in cycles])

with open('input.txt', 'r') as file:
    input = file.read()

steps, network = parse_input(input)
result = find_steps_to_Z(steps, network)
print(result)
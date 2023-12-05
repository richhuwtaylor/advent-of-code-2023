with open('input.txt') as f:
    engine_schematic = f.read().splitlines()

total_gear_ratio = 0

for row_index, row in enumerate(engine_schematic):
    for col_index, char in enumerate(row):
        if char != "*":
            continue

        adjacent_part_positions = set()
        
        for neighbor_row in [row_index - 1, row_index, row_index + 1]:
            for neighbor_col in [col_index - 1, col_index, col_index + 1]:
                if (
                    neighbor_row < 0
                    or neighbor_row >= len(engine_schematic)
                    or neighbor_col < 0
                    or neighbor_col >= len(engine_schematic[neighbor_row])
                    or not engine_schematic[neighbor_row][neighbor_col].isdigit()
                ):
                    continue
                while neighbor_col > 0 and engine_schematic[neighbor_row][neighbor_col - 1].isdigit():
                    neighbor_col -= 1
                adjacent_part_positions.add((neighbor_row, neighbor_col))
                
        if len(adjacent_part_positions) != 2:
            continue

        gear_numbers = []

        for neighbor_row, neighbor_col in adjacent_part_positions:
            number_str = ""
            while neighbor_col < len(engine_schematic[neighbor_row]) and engine_schematic[neighbor_row][neighbor_col].isdigit():
                number_str += engine_schematic[neighbor_row][neighbor_col]
                neighbor_col += 1
            gear_numbers.append(int(number_str))
        
        total_gear_ratio += gear_numbers[0] * gear_numbers[1]

print(total_gear_ratio)
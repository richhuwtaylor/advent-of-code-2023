with open('input.txt') as f:
    engine_schematic = f.read().splitlines()

part_positions = set()

for row_index, row in enumerate(engine_schematic):
    for col_index, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue
        for neighbor_row in range(row_index - 1, row_index + 2):
            for neighbor_col in range(col_index - 1, col_index + 2):
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
                part_positions.add((neighbor_row, neighbor_col))

part_numbers = []

for row, col in part_positions:
    number_str = ""
    while col < len(engine_schematic[row]) and engine_schematic[row][col].isdigit():
        number_str += engine_schematic[row][col]
        col += 1
    part_numbers.append(int(number_str))

print(sum(part_numbers))
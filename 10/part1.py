from collections import deque

def explore_connected_cells(grid, start_row, start_col):
    visited_cells = set()
    queue = deque([(start_row, start_col)])

    while queue:
        current_row, current_col = queue.popleft()
        current_char = grid[current_row][current_col]

        if (current_row, current_col) not in visited_cells:
            visited_cells.add((current_row, current_col))

            # Explore upward
            if current_row > 0 and current_char in "S|JL" and grid[current_row - 1][current_col] in "|7F":
                queue.append((current_row - 1, current_col))

            # Explore downward
            if current_row < len(grid) - 1 and current_char in "S|7F" and grid[current_row + 1][current_col] in "|JL":
                queue.append((current_row + 1, current_col))

            # Explore leftward
            if current_col > 0 and current_char in "S-J7" and grid[current_row][current_col - 1] in "-LF":
                queue.append((current_row, current_col - 1))

            # Explore rightward
            if current_col < len(grid[current_row]) - 1 and current_char in "S-LF" and grid[current_row][current_col + 1] in "-J7":
                queue.append((current_row, current_col + 1))

    return visited_cells

grid = open('input.txt').read().strip().splitlines()

for row_index, row in enumerate(grid):
    for col_index, char in enumerate(row):
        if char == "S":
            start_row, start_col = row_index, col_index
            break
    else:
        continue
    break

connected_cells = explore_connected_cells(grid, start_row, start_col)
result = len(connected_cells) // 2

print(result)
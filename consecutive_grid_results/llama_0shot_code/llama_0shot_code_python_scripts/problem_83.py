
def solve_grid(grid):
    possible_numbers = list(range(36, 86))
    replacements = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                possible_numbers_for_cell = []
                if i > 0 and j > 0: # Not in first row or first column
                    previous_row_value = grid[i-1][j]
                    previous_column_value = grid[i][j-1]
                    if grid[i-1][j-1] < previous_row_value and grid[i-1][j-1] < previous_column_value:
                        possible_numbers_for_cell = [num for num in possible_numbers if num > previous_row_value and num > previous_column_value]
                elif i > 0: # Not in first row
                    possible_numbers_for_cell = [num for num in possible_numbers if num > int(grid[i-1][j])]
                elif j > 0: # Not in first column
                    possible_numbers_for_cell = [num for num in possible_numbers if num > int(grid[i][j-1])]
                
                if len(possible_numbers_for_cell) > 0:
                    min_value = min(possible_numbers_for_cell)
                    replacements.append((i, j, min_value))
                    possible_numbers.remove(min_value)

    return replacements

grid = [['x', 'x', '58', 'x'], ['44', '54', '59', 'x'], ['43', 'x', '63', '75'], ['x', 'x', 'x', '84']]
print(solve_grid(grid))

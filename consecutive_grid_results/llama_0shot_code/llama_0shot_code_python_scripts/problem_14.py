
def solve_grid(grid):
    available_numbers = list(range(11, 49))
    replacements = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                replacement = min(available_numbers)
                replacements.append((i, j, replacement))
                available_numbers.remove(replacement)
                grid[i][j] = replacement
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2]
    min_sum = top_row_sum + right_col_sum + diagonal_sum
    return replacements, min_sum

grid = [['41', 'x', '21'], ['x', 'x', 'x'], ['12', 'x', '42']]
replacements, min_sum = solve_grid(grid)
print(replacements)
print(min_sum)


def solve_grid():
    grid = [['x', '32', '37'], ['29', 'x', 'x'], ['x', '46', 'x']]
    numbers = list(range(20, 53))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'x':
                for num in numbers:
                    if row == 0 or num > int(grid[row-1][col]):
                        if col == 0 or num > int(grid[row][col-1]):
                            grid[row][col] = num
                            break
    sum_top_row = sum(int(i) for i in grid[0] if i != 'x')
    sum_right_col = sum(int(grid[i][-1]) for i in range(len(grid)))
    sum_diagonal = sum(int(grid[i][i]) for i in range(len(grid)))
    total_sum = sum_top_row + sum_right_col + sum_diagonal
    replacements = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'x':
                for num in numbers:
                    if row == 0 or num > int(grid[row-1][col]):
                        if col == 0 or num > int(grid[row][col-1]):
                            grid[row][col] = num
                            replacements.append((row, col, num))
                            total_sum -= num
                            break
    return replacements, total_sum

replacements, total_sum = solve_grid()
print(f"Replacements: {replacements}")
print(f"Minimized sum: {total_sum}")

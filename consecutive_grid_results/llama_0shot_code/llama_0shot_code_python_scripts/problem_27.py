
def solve_grid():
    grid = [['52', 'x', 'x'], ['50', 'x', 'x'], ['x', 'x', '69']]
    possible_numbers = list(range(46, 89))
    top_row_sum = int(grid[0][0])
    right_col_sum = int(grid[2][2])
    diagonal_sum = top_row_sum + right_col_sum - int(grid[0][0])
    total_sum = top_row_sum + right_col_sum + diagonal_sum
    sorted_numbers = sorted(possible_numbers, reverse=True)
    replacements = []

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in sorted_numbers:
                    if num < total_sum:
                        replacements.append((i, j, num))
                        total_sum -= num
                        sorted_numbers.remove(num)
                        break

    return replacements

print(solve_grid())

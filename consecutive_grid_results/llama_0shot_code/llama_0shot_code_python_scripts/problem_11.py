
def solve_grid():
    grid = [['x', 'x', '55'], ['50', 'x', '56'], ['40', '43', 'x']]
    used_numbers = set()
    replacements = []

    # Fill in the missing values
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in range(33, 71):
                    if num not in used_numbers:
                        grid[i][j] = num
                        used_numbers.add(num)
                        replacements.append((i, j, num))
                        break

    # Ensure that the numbers in each row and column are in strictly increasing order
    for i in range(3):
        grid[i] = sorted(grid[i], key=int)
        if grid[i][0] > grid[i][1] or grid[i][1] > grid[i][2]:
            grid[i][1], grid[i][2] = grid[i][2], grid[i][1]

    for j in range(3):
        column = [grid[i][j] for i in range(3)]
        column = sorted(column, key=int)
        for i in range(3):
            grid[i][j] = column[i]
            if grid[i][j] != replacements[i * 3 + j][2]:
                replacements[i * 3 + j] = (i, j, column[i])

    # Calculate the sum of the numbers in the topmost row, the rightmost column, and the diagonal
    top_row_sum = sum(int(num) for num in grid[0] if num != 'x')
    right_column_sum = sum(int(num) for num in grid[i][2] for i in range(3))
    diagonal_sum = int(grid[0][0]) + int(grid[1][1]) + int(grid[2][2])

    print("Minimal possible sum:", top_row_sum + right_column_sum + diagonal_sum)
    print("Replacements:", replacements)

solve_grid()


def solve_grid():
    grid = [['30', 'x', 'x'], ['28', '33', '43'], ['x', 'x', '51']]
    possible_numbers = list(range(15, 58))
    replacements = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'x':
                for num in possible_numbers:
                    if row == 0 or num > int(grid[row][col-1]):  # Check if number is greater than the previous in row
                        if col == 0 or num > int(grid[row-1][col]):  # Check if number is greater than the above in column
                            if row == 0 and col == 0 or num > int(grid[row-1][col-1]):  # Check if number is greater than the top-left diagonal
                                if row == 2 and col == 2 or num < int(grid[row-1][col+1]):  # Check if number is less than the bottom-right diagonal
                                    grid[row][col] = str(num)
                                    replacements.append((row, col, num))
                                    possible_numbers.remove(num)
                                    break

    return replacements

print(solve_grid())

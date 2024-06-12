
def find_replacements(grid):
    replacements = []
    possible_numbers = list(range(49, 101))

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                max_row = max(int(num) for num in grid[i] if num != 'x')
                max_col = max(int(num) for row in grid for num in row[j] if num != 'x')
                max_diag = max(int(grid[min(i, j)][k]) for k in range(min(i, j), 3) if grid[min(i, j)][k] != 'x')
                for num in possible_numbers:
                    if num <= max_row and num <= max_col and num <= max_diag:
                        replacements.append((i, j, num))
                        possible_numbers.remove(num)
                        grid[i][j] = num
                        break

    return replacements

grid = [['57', 'x', '86'], ['x', '75', 'x'], ['x', '76', '90']]
print(find_replacements(grid))

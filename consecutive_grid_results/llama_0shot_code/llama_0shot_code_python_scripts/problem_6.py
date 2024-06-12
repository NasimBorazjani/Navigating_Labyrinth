
def solve_grid():
    available_numbers = list(range(41, 74))
    grid = [['41', '48', 'x'], ['x', 'x', '63'], ['x', 'x', '67']]
    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                value = available_numbers.pop(0)
                replacements.append((i, j, value))
                grid[i][j] = value

    return replacements

print(solve_grid())


def solve_grid():
    grid = [['x', '40', 'x', '65'],
            ['34', 'x', '53', 'x'],
            ['x', 'x', 'x', '63'],
            ['x', '56', 'x', '62']]

    possible_numbers = list(range(25, 70))

    replacements = []

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                grid[i][j] = possible_numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    for i in range(4):
        for j in range(4):
            if i < 3 and grid[i][j] > grid[i + 1][j]:
                grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]
                replacements.append((i, j, grid[i][j]))
                replacements.append((i + 1, j, grid[i + 1][j]))
            if j < 3 and grid[i][j] > grid[i][j + 1]:
                grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
                replacements.append((i, j, grid[i][j]))
                replacements.append((i, j + 1, grid[i][j + 1]))

    return replacements

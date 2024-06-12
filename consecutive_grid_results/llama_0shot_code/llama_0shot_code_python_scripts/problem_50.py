
def solve_grid(grid):
    available_numbers = list(range(36, 75))
    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                grid[i][j] = available_numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        for j in range(len(grid[i])):
            if grid[i][j] != 'x':
                grid[j][i] = grid[i][j]

    for i in range(len(grid)):
        grid[i][i] = min(grid[i][i], grid[-1-i][-1-i])
        grid[-1-i][-1-i] = grid[i][i]

    return replacements

grid = [['x', 'x', 'x', '60'], ['47', 'x', '62', '65'], ['x', '58', '67', '68'], ['54', 'x', '74', 'x']]
print(solve_grid(grid))

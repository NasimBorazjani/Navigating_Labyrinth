
def solve_grid():
    grid = [['27', '37', 'x', 'x'],
            ['30', 'x', 'x', 'x'],
            ['32', '44', '53', '61'],
            ['33', '54', 'x', '64']]

    numbers = list(range(27, 67))

    replacements = []

    for i in range(4):
        row = [int(x) for x in grid[i] if x != 'x']
        col = [int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']

        if row:
            if row[0] < row[-1]:
                for j in range(4):
                    if grid[i][j] == 'x':
                        replacements.append((i, j, numbers.pop(0)))
            else:
                for j in range(3, -1, -1):
                    if grid[i][j] == 'x':
                        replacements.append((i, j, numbers.pop(0)))

        if col:
            if col[0] < col[-1]:
                for i in range(4):
                    if grid[i][i] == 'x':
                        replacements.append((i, i, numbers.pop(0)))
            else:
                for i in range(3, -1, -1):
                    if grid[i][i] == 'x':
                        replacements.append((i, i, numbers.pop(0)))

    diagonal = [int(x) for x in grid[0] if x != 'x'] + [int(grid[i][i]) for i in range(1, 4)]

    if diagonal:
        if diagonal[0] < diagonal[-1]:
            for i in range(3):
                if grid[i][i] == 'x':
                    replacements.append((i, i, numbers.pop(0)))
        else:
            for i in range(3, -1, -1):
                if grid[i][i] == 'x':
                    replacements.append((i, i, numbers.pop(0)))

    return replacements

print(solve_grid())

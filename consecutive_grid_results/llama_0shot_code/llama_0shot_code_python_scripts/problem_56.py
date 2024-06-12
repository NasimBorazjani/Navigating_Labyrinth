
def solve_grid():
    grid = [['x', 'x', '63', 'x'],
            ['x', '53', '57', '73'],
            ['x', 'x', '56', 'x'],
            ['42', 'x', 'x', '68']]

    possible_numbers = list(range(41, 80))

    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                for num in possible_numbers:
                    if (i > 0 and grid[i-1][j] < num < grid[i][j]) or (i > 0 and grid[i-1][j] > num > grid[i][j]):
                        if (j > 0 and grid[i][j-1] < num < grid[i][j]) or (j > 0 and grid[i][j-1] > num > grid[i][j]):
                            if i == j and grid[i-1][j-1] < num < grid[i][j]:
                                replacements.append((i, j, num))
                                possible_numbers.remove(num)
                                break
                            elif i == len(grid)-1-j and grid[i-1][j+1] < num < grid[i][j]:
                                replacements.append((i, j, num))
                                possible_numbers.remove(num)
                                break
    return replacements

print(solve_grid())


def solve_grid():
    grid = [['x', 'x', '85'], ['58', 'x', '84'], ['x', '74', '59']]
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                positions.append((i, j))
    for i, j in positions:
        grid[i][j] = str(48)
    for i in range(len(grid)):
        grid[i] = [int(x) for x in grid[i]]
    for i in range(len(grid)):
        if grid[i][0] > grid[i][1] or grid[i][1] > grid[i][2]:
            grid[i] = sorted(grid[i])
    for i in range(len(grid)):
        grid[i] = [str(x) for x in grid[i]]
    result = []
    for i, j in positions:
        result.append((i, j, int(grid[i][j])))
    return result

print(solve_grid())

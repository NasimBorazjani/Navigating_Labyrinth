
def solve_grid():
    grid = [['10', '25', 'x'], ['x', 'x', '45'], ['x', '7', 'x']]
    numbers = list(range(5, 53))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                grid[i][j] = str(numbers.pop(0))
    while True:
        if all(grid[i][0] < grid[i][1] < grid[i][2] for i in range(len(grid))) and \
           all(grid[0][i] < grid[1][i] < grid[2][i] for i in range(len(grid))) and \
           grid[0][0] < grid[1][1] < grid[2][2]:
            break
        min_val = min(map(int, [n for sub in grid for n in sub if n != 'x']))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'x':
                    grid[i][j] = str(min_val)
                    numbers.remove(min_val)
                    break
            else:
                continue
            break
    return [(i, j, int(grid[i][j])) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] != 'x']

print(solve_grid())

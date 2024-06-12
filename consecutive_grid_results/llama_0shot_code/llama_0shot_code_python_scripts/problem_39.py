
def solve_grid():
    grid = [['x', '60', 'x'], ['x', 'x', '53'], ['52', '39', '20']]
    numbers = list(range(18, 71))
    for num in numbers:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    grid[i][j] = num
                    if is_valid(grid):
                        return [(i, j, num)]
                    else:
                        grid[i][j] = 'x'
    return []

def is_valid(grid):
    for row in grid:
        if row[0] >= row[1] or row[1] >= row[2]:
            return False
    for col in range(3):
        if grid[0][col] >= grid[1][col] or grid[1][col] >= grid[2][col]:
            return False
    if grid[0][0] >= grid[1][1] or grid[1][1] >= grid[2][2]:
        return False
    if grid[0][2] >= grid[1][1] or grid[1][1] >= grid[2][0]:
        return False
    return True

print(solve_grid())

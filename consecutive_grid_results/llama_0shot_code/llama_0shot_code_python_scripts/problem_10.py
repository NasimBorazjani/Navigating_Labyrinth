
def solve_grid():
    grid = [['x', '59', 'x'], ['47', 'x', '62'], ['x', '50', '63']]
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in range(41, 79):
                    if i > 0 and num <= int(grid[i-1][j]) or i < 2 and num >= int(grid[i+1][j]) or j > 0 and num <= int(grid[i][j-1]) or j < 2 and num >= int(grid[i][j+1]):
                        if i == j or i == 2 - j:
                            if num <= int(grid[1][1]):
                                grid[i][j] = num
                                break
                        else:
                            grid[i][j] = num
                            break
    return grid

def get_sum(grid):
    sum = 0
    for i in range(3):
        sum += grid[i][i]
    for i in range(3):
        sum += grid[i][2-i]
    return sum

def minimize_sum(grid):
    min_sum = get_sum(grid)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in range(41, 79):
                    grid[i][j] = num
                    new_sum = get_sum(grid)
                    if new_sum < min_sum:
                        min_sum = new_sum
    return min_sum

def get_replacements(grid):
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                replacements.append((i, j, grid[i][j]))
    return replacements

grid = solve_grid()
min_sum = minimize_sum(grid)
replacements = get_replacements(grid)

print(f"Minimum sum: {min_sum}")
print(f"Replacements: {replacements}")

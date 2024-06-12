
# Function to check if the grid is valid
def is_valid(grid):
    for row in grid:
        if row[0] > row[1] > row[2] or row[0] < row[1] < row[2]:
            continue
        else:
            return False
    for col in range(len(grid)):
        if grid[0][col] > grid[1][col] > grid[2][col] or grid[0][col] < grid[1][col] < grid[2][col]:
            continue
        else:
            return False
    if grid[0][0] > grid[1][1] > grid[2][2] or grid[0][0] < grid[1][1] < grid[2][2]:
        return True
    else:
        return False

# Function to calculate the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers on the diagonal
def calculate_sum(grid):
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][2] for i in range(3))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2]
    return top_row_sum + right_col_sum + diagonal_sum

# Function to solve the problem
def solve_problem():
    grid = [['x', '51', 'x'], ['48', '50', 'x'], ['x', 'x', 'x']]
    remaining_numbers = list(range(22, 75))
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = remaining_numbers.pop(0)
    while not is_valid(grid):
        min_sum = calculate_sum(grid)
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for num in remaining_numbers:
                        grid[i][j] = num
                        if is_valid(grid) and calculate_sum(grid) < min_sum:
                            min_sum = calculate_sum(grid)
                            break
                        else:
                            grid[i][j] = 'x'
        remaining_numbers.insert(0, grid[i][j])
    return [(i, j, grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] != 'x']

print(solve_problem())

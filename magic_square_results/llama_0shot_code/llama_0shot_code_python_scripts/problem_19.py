
from itertools import permutations

# Function to check if a number is valid in a position
def is_valid(grid, row, col, num):
    # Check the number is not in the same row, column or diagonal
    for i in range(3):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    if row == col:
        if grid[0][0] == num or grid[1][1] == num or grid[2][2] == num:
            return False
    if row + col == 2:
        if grid[0][2] == num or grid[1][1] == num or grid[2][0] == num:
            return False
    return True

# Function to solve the magic square
def solve_magic_square(grid):
    best_grid = None
    best_sum = float('inf')
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'x':
                for num in range(50, 85):
                    if is_valid(grid, row, col, num):
                        new_grid = [[grid[i][j] if i != row or j != col else num for j in range(3)] for i in range(3)]
                        row_sums = [sum(new_grid[i]) for i in range(3)]
                        col_sums = [sum(new_grid[i][j] for i in range(3)) for j in range(3)]
                        diag_sum = sum(new_grid[i][i] for i in range(3))
                        if row_sums.count(201) == 1 and col_sums.count(234) == 1 and diag_sum == 213:
                            new_sum = sum(num for row in new_grid for num in row)
                            if new_sum < best_sum:
                                best_grid = new_grid
                                best_sum = new_sum
    return best_grid

# The initial grid
grid = [['64', '78', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# Convert the elements to integer
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            grid[i][j] = int(grid[i][j])

# Solve the magic square
solution = solve_magic_square(grid)

# Convert the solution to the required format
solution = [(i, j, num) for i in range(3) for j in range(3) if solution[i][j] != 'x' and grid[i][j] == 'x']

print(solution)

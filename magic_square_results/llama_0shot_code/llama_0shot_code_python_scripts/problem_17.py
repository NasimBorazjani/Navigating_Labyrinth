
from itertools import permutations

# The initial grid with missing values represented as 'x'
grid = [['x', '52', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The required sums for each row, column, and diagonal
row_sums = [192, 166, 184]
col_sums = [166, 192, 184]
diag_sum = 184

# Function to check if a number can be placed in a certain position
def is_valid(num, pos, grid, row_sums, col_sums, diag_sum):
    # Update the grid
    grid[pos[0]][pos[1]] = num
    
    # Check if the grid fulfills the magic square requirements
    for i in range(3):
        if sum(grid[i]) != row_sums[i] or sum(grid[j][i] for j in range(3)) != col_sums[i]:
            return False
    if grid[0][0] + grid[1][1] + grid[2][2] != diag_sum or grid[0][2] + grid[1][1] + grid[2][0] != diag_sum:
        return False
    
    return True

# Function to generate all possible combinations
def generate_combinations():
    return permutations(range(48, 78), 3)

# The main function to solve the problem
def solve_magic_square():
    min_sum = float('inf')
    min_combination = None
    
    for combination in generate_combinations():
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    if is_valid(combination[0], (i, j), grid, row_sums, col_sums, diag_sum):
                        combination = combination[1:]
                        break
            else:
                continue
            break
        
        if combination:
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 'x':
                        if is_valid(combination[0], (i, j), grid, row_sums, col_sums, diag_sum):
                            combination = combination[1:]
                            break
                    else:
                        continue
                else:
                    continue
                
            if combination and is_valid(combination[0], (2, 1), grid, row_sums, col_sums, diag_sum):
                sum_grid = sum(sum(row) for row in grid)
                if sum_grid < min_sum:
                    min_sum = sum_grid
                    min_combination = [(i, j, num) for i, j, num in zip(range(3), range(3), ['x', '52', 'x']) if num == 'x']
    
    return min_combination

print(solve_magic_square())

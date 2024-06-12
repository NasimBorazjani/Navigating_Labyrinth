
from itertools import product

def magic_square(grid):
    # All possible combinations of numbers to fill 'x'
    nums = list(range(40, 90))
    
    # All possible combinations to fill the grid
    combinations = list(product(nums, repeat=3))
    
    # Function to check if a combination is valid
    def is_valid(combination):
        # Fill the grid with the current combination
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    grid[i][j] = combination[i * 3 + j]
        
        # Check the sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        diag_sums = [grid[0][0] + grid[1][1] + grid[2][2], grid[0][2] + grid[1][1] + grid[2][0]]
        
        # Check if all sums are correct
        if row_sums[0] != 194 or row_sums[1] != 194 or row_sums[2] != 194 or \
           col_sums[0] != 183 or col_sums[1] != 183 or col_sums[2] != 183 or \
           diag_sums[0] != 161 or diag_sums[1] != 161:
            return False
        
        return True
    
    # List to store all valid combinations and their sums
    valid_combinations = []
    
    # Try every combination
    for combination in combinations:
        if is_valid(combination):
            valid_combinations.append((combination, sum(combination)))
    
    # Return the combination with the smallest sum
    return min(valid_combinations, key=lambda x: x[1])

# The initial grid
grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['40', 'x', '71']]

# Convert the numbers in the grid from string to int
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            grid[i][j] = int(grid[i][j])

# Find and print the solution
solution = magic_square(grid)
print(solution)

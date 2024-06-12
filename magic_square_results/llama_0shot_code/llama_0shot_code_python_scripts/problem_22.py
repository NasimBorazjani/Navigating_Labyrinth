
from itertools import permutations

# Function to check if a grid satisfies the conditions
def is_valid(grid, row_sums, col_sums, diag_sum):
    for i in range(3):
        if sum(grid[i]) != row_sums[i] or sum(grid[i][j] for j in range(3)) != col_sums[i] or \
                grid[i][i] != diag_sum:
            return False
    return True

# Function to solve the problem
def magic_square(grid, row_sums, col_sums, diag_sum):
    # Get the indices of 'x' in the grid
    x_indices = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 'x']
    
    # Generate all permutations of numbers within the given range
    nums = list(range(12, 47))
    
    # Initialize the result set
    results = []
    
    # For each permutation
    for perm in permutations(nums, len(x_indices)):
        # Create a copy of the grid
        new_grid = [row.copy() for row in grid]
        
        # Replace 'x' with the numbers in the permutation
        for (i, j), num in zip(x_indices, perm):
            new_grid[i][j] = num
        
        # If the grid satisfies the conditions
        if is_valid(new_grid, row_sums, col_sums, diag_sum):
            # Add the permutation to the result set
            results.append(((i, j, num) for i, j, num in zip(x_indices, perm)))
    
    # Return the result set
    return results

# Test the function
grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '43', 'x']]
row_sums = [105, 120, 120]
col_sums = [120, 105, 120]
diag_sum = 99
print(magic_square(grid, row_sums, col_sums, diag_sum))

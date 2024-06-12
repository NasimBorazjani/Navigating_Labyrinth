
import numpy as np
import random

def generate(n, lower_range, upper_range, col_range, row_range, num_more_to_mask, seed):
    np.random.seed(seed)
    random.seed(seed)
    
    # Generate a list of random numbers from lower_range to upper_range
    numbers = np.random.choice(np.arange(lower_range, upper_range), size=n*n, replace=False)    
    
    # Reshape the numbers into an n by m grid
    grid = numbers.reshape(n, n)
    
    # Calculate the sum of each column in the specified range
    sum_cols = np.sum(grid[:,col_range[0]:col_range[1]], axis=0)
    
    # Calculate the sum of each row in the specified range
    sum_rows = np.sum(grid[row_range[0]:row_range[1],:], axis=1)
    
    # Calculate the sum of the top right to bottom left diagonal
    sum_diag = np.trace(np.fliplr(grid))
    
    # Randomly mask numbers in the grid
    # the number of masked numbers must be at least 3 more than the number of equations
    # make sure at least 2 numebrs are in the grid
    num_contraints = n + 1
    num_to_mask = num_contraints + num_more_to_mask
    mask = np.full(n*n, False)
    mask[:num_to_mask] = True
    np.random.shuffle(mask)
    grid = np.where(mask.reshape(n, n), 'x', grid)
    
    return grid, sum_cols.tolist(), sum_rows.tolist(), sum_diag


"""# Test the function
grid, sum_cols, sum_rows, sum_diag = generate(4, 10, 50, (4//4, 3*4//4), (4//4, 3*4//4), 1)
print("Grid:")
print(grid)
print("Sum of columns:", sum_cols)
print("Sum of rows:", sum_rows)
print("Sum of main diagonal:", sum_diag)"""
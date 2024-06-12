
from itertools import permutations

# The initial grid with 'x's
grid = [['x', 'x', 'x'], ['30', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for each row, each column, and the two diagonals
sums = {'row1': 87, 'col1': 82, 'diag1': 94, 'diag2': 94}

# The range of numbers to fill in the grid
num_range = range(20, 40)

# Initialize the minimum sum and the solution
min_sum = float('inf')
solution = None

# Generate all possible permutations of numbers within the range
for perm in permutations(num_range, 3):
    # Create a copy of the grid to fill in the numbers
    new_grid = [row.copy() for row in grid]
    
    # Fill in the numbers
    for i, num in enumerate(perm):
        new_grid[i//3][i%3] = str(num)
    
    # Check if the sums of each row, each column, and the diagonals equal the given amounts
    if (sum(map(int, new_grid[0])) != sums['row1'] or
        sum(map(int, [new_grid[0][0], new_grid[1][1], new_grid[2][2]])) != sums['col1'] or
        sum(map(int, [new_grid[0][2], new_grid[1][1], new_grid[2][0]])) != sums['diag1'] or
        sum(map(int, [new_grid[0][0], new_grid[1][1], new_grid[2][2]])) != sums['diag2']):
        continue
    
    # If all the conditions are met, check if this configuration gives us a lower sum than we have seen so far
    cur_sum = sum(map(int, [num for sublist in new_grid for num in sublist]))
    if cur_sum < min_sum:
        min_sum = cur_sum
        # Store this configuration as a list of tuples
        solution = [(i//3, i%3, num) for i, num in enumerate(perm)]

# Return the configuration with the lowest sum
print(solution)


import numpy as np
from itertools import permutations

# Initial state of the grid
grid = np.array([['x', '37', 'x', 'x'],
                 ['x', '35', '40', 'x'],
                 ['15', 'x', 'x', '44'],
                 ['11', '20', '36', 'x']])

# Range of numbers to fill in the grid
numbers = list(range(9, 54))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 10)

min_sum = float('inf')
solution = []

# Iterate through each permutation
for perm in perms:
    temp_grid = grid.copy()
    idx = 0
    temp_sum = 0
    
    # Replace 'x' with numbers from the permutation
    for i in range(4):
        for j in range(4):
            if temp_grid[i][j] == 'x':
                temp_grid[i][j] = str(perm[idx])
                idx += 1
    
    # Calculate the sum of the top row, rightmost column, and diagonal
    temp_sum = sum([int(temp_grid[0][j]) for j in range(4)]) + sum([int(temp_grid[i][3]) for i in range(4)]) + sum([int(temp_grid[k][k]) for k in range(4)])
    
    # Update the minimum sum and solution if a better one is found
    if temp_sum < min_sum:
        min_sum = temp_sum
        solution = [(i, j, int(temp_grid[i][j])) for i in range(4) for j in range(4) if temp_grid[i][j] != grid[i][j]]

print(solution)

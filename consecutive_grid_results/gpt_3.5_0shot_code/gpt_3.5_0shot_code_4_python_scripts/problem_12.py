
import numpy as np
from itertools import permutations

# Define the initial grid
grid = np.array([[57, 'x', 'x'],
                 ['x', 50, 63],
                 ['x', 69, 71]])

# Define the range of numbers
numbers = list(range(35, 73))

# Generate all possible permutations of the numbers
perms = permutations(numbers, 6)

# Function to check if a row or column is strictly increasing or decreasing
def check_order(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or all(arr[i] > arr[i+1] for i in range(len(arr)-1))

# Function to calculate the sum of the specified elements
def calculate_sum(grid):
    return grid[0, :].sum() + grid[:, -1].sum() + np.diag(grid).sum()

# Function to solve the problem
def solve(grid, perms):
    min_sum = float('inf')
    solution = None
    
    for perm in perms:
        new_grid = grid.copy()
        idx = 0
        
        for i in range(3):
            for j in range(3):
                if new_grid[i, j] == 'x':
                    new_grid[i, j] = perm[idx]
                    idx += 1
        
        if all(check_order(new_grid[i, :]) for i in range(3)) and all(check_order(new_grid[:, j]) for j in range(3)):
            current_sum = calculate_sum(new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                solution = new_grid
    
    return solution

# Solve the problem
solution_grid = solve(grid, perms)

# Find the x positions and corresponding numbers
solution = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x':
            solution.append((i, j, solution_grid[i, j]))

print(solution)

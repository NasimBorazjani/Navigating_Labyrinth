
import numpy as np

# Define the grid
grid = np.array([['x', 16, 'x'],
                 ['x', 'x', 'x'],
                 [45, 'x', 'x']])

# Define the unique integers
unique_integers = list(range(9, 49))

# Remove the known numbers from the unique integers
for i in range(3):
    for j in range(3):
        if grid[i, j] != 'x':
            unique_integers.remove(grid[i, j])

# Define the sums
sum_column_1 = 67
sum_row_1 = 60
sum_diagonal = 89

# Solve the problem
solution = []
for i in range(3):
    for j in range(3):
        if grid[i, j] == 'x':
            # Find the smallest unique integer that satisfies the conditions
            for integer in unique_integers:
                grid[i, j] = integer
                if np.sum(grid[:, 1]) == sum_column_1 and np.sum(grid[1, :]) == sum_row_1 and np.sum(grid.diagonal()[::-1]) == sum_diagonal:
                    solution.append((i, j, integer))
                    unique_integers.remove(integer)
                    break
                else:
                    grid[i, j] = 'x'

print(solution)

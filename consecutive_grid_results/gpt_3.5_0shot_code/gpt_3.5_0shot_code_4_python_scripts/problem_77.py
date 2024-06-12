
import numpy as np
from itertools import permutations

# Given grid
grid = np.array([[25, 'x', 'x', 57],
                 [39, 45, 56, 'x'],
                 [43, 'x', 58, 'x'],
                 [46, 'x', 65, 69]])

# Generate all permutations of numbers in the range [21, 71)
numbers = list(range(21, 71))
perms = permutations(numbers, 10)

# Function to check if a permutation satisfies the grid constraints
def check_permutation(perm):
    perm = iter(perm)
    for i in range(4):
        row = grid[i]
        row = [next(perm) if x == 'x' else x for x in row]
        if any(row[j] >= row[j+1] for j in range(3)):
            return False
    for j in range(4):
        col = grid[:, j]
        col = [next(perm) if x == 'x' else x for x in col]
        if any(col[i] >= col[i+1] for i in range(3)):
            return False
    diag = [grid[i, i] for i in range(4)]
    diag = [next(perm) if x == 'x' else x for x in diag]
    if any(diag[i] >= diag[i+1] for i in range(3)):
        return False
    return True

# Find the permutation that minimizes the sum of the specified elements
for perm in perms:
    if check_permutation(perm):
        result = [(i, j, x) for i in range(4) for j in range(4) if grid[i, j] == 'x']
        print(result)
        break


from itertools import permutations

def magic_square(grid, total):
    # Generate all possible permutations of the numbers in the given range
    perms = permutations(range(20, 40))
    solutions = []
    for perm in perms:
        temp_grid = grid.copy()  # Create a copy of the grid to avoid modification
        # Place the numbers in the grid
        for i in range(3):
            for j in range(3):
                if temp_grid[i][j] == 'x':
                    temp_grid[i][j] = perm[i * 3 + j]
        # Calculate the sum of each row, each column, and the two diagonals
        row_sums = [sum(temp_grid[i]) for i in range(3)]
        col_sums = [sum(temp_grid[i][j] for i in range(3)) for j in range(3)]
        diag_sums = [temp_grid[i][i] for i in range(3)]
        diag_sums.append(temp_grid[0][2])
        # Check if all the sums equal the total
        if all(sum == total for sum in row_sums + col_sums + diag_sums):
            # Add this permutation to the solutions
            solutions.append((perm[0], perm[1], perm[2]))
    # Return the solution with the minimum sum
    return min(solutions, key=lambda x: sum(x))

grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['22', 'x', 'x']]
print(magic_square(grid, 82))

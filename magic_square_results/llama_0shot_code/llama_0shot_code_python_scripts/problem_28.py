
from itertools import permutations

def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    # Generate all possible permutations of the numbers in the given range
    perms = permutations(range(26, 66))
    solutions = []

    for perm in perms:
        # Create a copy of the grid to fill in the permutation
        grid_copy = [row.copy() for row in grid]

        # Fill in the permutation into the grid
        for i, value in enumerate(perm):
            row, col = divmod(i, 3)
            grid_copy[row][col] = value

        # Check if the sums of the rows, columns, and diagonal match the given amounts
        if (sum(grid_copy[0]) == row_sums[0] and
            sum(grid_copy[1]) == row_sums[1] and
            sum(grid_copy[2]) == row_sums[2] and
            sum(grid_copy[i][i] for i in range(3)) == diag_sum):

            # If the sums match, store the solution as a list of tuples
            solutions.append([(row, col, value) for row in range(3) for col in range(3) if grid_copy[row][col] != 'x' for value in perm if grid_copy[row][col] == value])

    # Return the solution with the minimum sum of all the numbers in the grid
    return min(solutions, key=lambda solution: sum(value for _, _, value in solution))

# The initial grid with 'x's
grid = [['51', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The given sums for the rows and the diagonal
row_sums = [124, 107, 107]
diag_sum = 108

# Call the function to solve the magic square
solution = solve_magic_square(grid, row_sums, col_sums, diag_sum)

print(solution)

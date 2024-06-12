
from itertools import permutations

def solve_magic_square():
    # Define the grid
    grid = [['x', 'x', 'x', 'x'],
            ['53', '43', 'x', 'x'],
            ['72', 'x', 'x', 'x'],
            ['63', 'x', 'x', '50']]

    # Define the sums
    col_sums = [None, 209, 265, None]
    row_sums = [None, 227, 250, None]
    diag_sum = 260

    # Define the range of numbers
    numbers = list(map(str, range(43, 85)))

    # Remove the numbers already in the grid
    for row in grid:
        for num in row:
            if num in numbers:
                numbers.remove(num)

    # Generate all permutations of the remaining numbers
    perms = permutations(numbers)

    # Try each permutation
    for perm in perms:
        # Fill the grid with the permutation
        filled_grid = [[num if num != 'x' else perm.pop(0) for num in row] for row in grid]

        # Check if the sums match
        if all(sum(int(num) for num in row) == row_sum if row_sum is not None else True for row, row_sum in zip(filled_grid, row_sums)) and \
           all(sum(int(filled_grid[i][j]) for i in range(4)) == col_sum if col_sum is not None else True for j, col_sum in enumerate(col_sums)) and \
           sum(int(filled_grid[i][3-i]) for i in range(4)) == diag_sum:
            # If the sums match, return the solution
            return [(i, j, int(num)) for i, row in enumerate(filled_grid) for j, num in enumerate(row) if grid[i][j] == 'x']

# Print the solution
print(solve_magic_square())

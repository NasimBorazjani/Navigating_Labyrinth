
from itertools import permutations

def solve_magic_square():
    # Define the grid
    grid = [['26', '38', '27', 'x'],
            ['x', 'x', 'x', '19'],
            ['x', '43', 'x', 'x'],
            ['42', 'x', '34', '20']]

    # Define the constraints
    row_sums = [None, 94, 109, None]
    col_sums = [None, 128, 80, None]
    diag_sum = 99

    # Find the 'x' positions and the numbers already in the grid
    x_positions = []
    numbers_in_grid = set()
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                x_positions.append((i, j))
            else:
                numbers_in_grid.add(int(grid[i][j]))

    # Generate the possible numbers to fill in the 'x' positions
    possible_numbers = set(range(6, 48)) - numbers_in_grid
    possible_numbers = list(permutations(possible_numbers, len(x_positions)))

    # Try each combination of possible numbers
    for numbers in possible_numbers:
        # Fill in the 'x' positions with the current combination of numbers
        for (i, j), number in zip(x_positions, numbers):
            grid[i][j] = str(number)

        # Check if the current combination of numbers satisfies the constraints
        if all(sum(int(grid[i][j]) for j in range(4)) == row_sums[i] or row_sums[i] is None for i in range(4)) and \
           all(sum(int(grid[i][j]) for i in range(4)) == col_sums[j] or col_sums[j] is None for j in range(4)) and \
           sum(int(grid[i][3 - i]) for i in range(4)) == diag_sum:
            # If the constraints are satisfied, return the solution
            return [(i, j, int(grid[i][j])) for (i, j) in x_positions]

    # If no solution is found, return None
    return None

print(solve_magic_square())

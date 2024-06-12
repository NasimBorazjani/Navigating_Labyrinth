
import itertools

def magic_square(grid, row_sums, col_sums, diag_sum):
    # Define the range of numbers and the empty places in the grid
    range_nums = range(19, 44)
    empty_places = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 'x']

    # Generate all possible combinations of numbers within the range for the empty places
    combinations = itertools.permutations(range_nums, len(empty_places))

    # Initialize the solution list
    solutions = []

    # For each combination
    for combination in combinations:
        new_grid = [row[:] for row in grid]  # Create a copy of the grid
        for (i, j), num in zip(empty_places, combination):
            new_grid[i][j] = num

        # Check if the new grid satisfies the conditions of the problem
        if (sum(new_grid[0]) == row_sums[0] and
            sum(new_grid[1]) == row_sums[1] and
            sum(new_grid[2]) == row_sums[2] and
            sum(new_grid[i][i] for i in range(3)) == diag_sum):

            # If it does, add it to the solution list
            solutions.append(((i, j), num) for (i, j), num in zip(empty_places, combination))

    return solutions

grid = [['37', 'x', '26'], ['x', 'x', 'x'], ['x', 'x', 'x']]
row_sums = [94, 111, 111]
col_sums = [111, 111, 111]
diag_sum = 82

print(magic_square(grid, row_sums, col_sums, diag_sum))

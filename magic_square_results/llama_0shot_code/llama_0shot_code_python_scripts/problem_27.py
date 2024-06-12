
import itertools

def magic_square(grid, row_sums, col_sums, diag_sum):
    # Get the list of numbers from 26 to 65
    nums = list(range(26, 66))

    # Get all possible combinations of the numbers
    combs = list(itertools.permutations(nums))

    # Initialize the solution
    solution = None

    # Iterate over each combination
    for comb in combs:
        # Fill in the 'x' values in the grid with the numbers in the combination
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    grid[i][j] = comb[i * 3 + j]

        # Check if the sums of each row, column, and diagonal match the given amounts
        if (sum(grid[0]) == row_sums[0] and
            sum(grid[1]) == row_sums[1] and
            sum(grid[2]) == row_sums[2] and
            sum(grid[i][i] for i in range(3)) == diag_sum and
            sum(grid[i][2 - i] for i in range(3)) == diag_sum):

            # If the sums match, we have found a solution
            solution = [(i, j, grid[i][j]) for i in range(3) for j in range(3) if grid[i][j] != 'x']
            break

    # Return the solution
    return solution

# The initial grid
grid = [['47', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

# The row sums
row_sums = [135, 93, 93]

# The column sums
col_sums = [93, 93, 135]

# The diagonal sums
diag_sum = 106

# Call the function
solution = magic_square(grid, row_sums, col_sums, diag_sum)

# Print the solution
print(solution)

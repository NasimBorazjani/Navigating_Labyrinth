
import itertools

# The initial grid with 'x's
grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['37', 'x', 'x']]

# Function to replace 'x's with numbers and check the sums
def check_grid(grid, numbers):
    # Replace 'x's with numbers
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = numbers.pop(0)

    # Check row sums
    row_sums = [sum(row) for row in grid]
    if row_sums != [157, 125, 125]:
        return False

    # Check column sums
    col_sums = [sum(col) for col in zip(*grid)]
    if col_sums != [125, 157, 125]:
        return False

    # Check diagonal sums
    if grid[0][0] + grid[1][1] + grid[2][2] != 138:
        return False
    if grid[0][2] + grid[1][1] + grid[2][0] != 138:
        return False

    # If all conditions are satisfied, return the total sum
    return sum(sum(row) for row in grid)

# Generate all permutations
perms = list(itertools.permutations(list(range(35, 60))))

# Check each permutation
solutions = [(perm, check_grid(list(map(list, grid)), list(perm))) for perm in perms]

# Filter out invalid solutions (where check_grid returned False)
solutions = [sol for sol in solutions if sol[1] is not False]

# Find the solution with the minimum total sum
min_sum_solution = min(solutions, key=lambda x: x[1])

# Print the solution as a list of tuples
print(list(map(lambda x: (x[0]//10, x[0]%10, x[1]), enumerate(min_sum_solution[0]))))

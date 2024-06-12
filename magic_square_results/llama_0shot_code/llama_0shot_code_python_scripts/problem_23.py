
import itertools

# Define the range of numbers
num_range = range(12, 47)

# Define the grid with 'x's as placeholders
grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 19]]

# Define the target sums
row_sums = [82, 71, 70]
col_sums = [71, 82, 70]
diag_sum = 70

# Function to check if a particular combination fills in the grid correctly
def check_combination(combination):
    new_grid = [[num if num != 'x' else comb for num, comb in zip(row, combination)] for row in grid]
    sums = [sum(row) for row in new_grid] + [sum(new_grid[i][i] for i in range(len(new_grid)))] + [sum(new_grid[i][len(new_grid)-1-i] for i in range(len(new_grid)))]
    return sums == row_sums + col_sums + [diag_sum]

# Function to try every combination and return the one with the smallest sum
def find_best_combination():
    for combination in itertools.permutations(num_range, len(grid)):
        if check_combination(combination):
            return combination

# Find the best combination and create the solution
best_combination = find_best_combination()
solution = [(i, j, val) for i, row in enumerate(grid) for j, num in enumerate(row) if num == 'x' for val in best_combination]

print(solution)

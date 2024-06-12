
from itertools import combinations

# The given range
low = 28
high = 57

# The required sums
col1_sum = 143
row1_sum = 134
diag_sum = 131

# The grid
grid = [['x', 32, 'x'], [38, 'x', 'x'], ['x', 'x', 'x']]

# Function to check if a combination meets the conditions
def check_conditions(combination):
    row1, col1, diag = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                val = combination[i*3 + j]
                row1 += val
                col1 += val
                if i == j:
                    diag += val
    return row1 == row1_sum and col1 == col1_sum and diag == diag_sum

# Function to solve the problem
def solve_problem():
    numbers = list(range(low, high+1))
    combinations = list(combinations(numbers, 5))
    for combination in combinations:
        if check_conditions(combination):
            result = [(i//3, i%3, val) for i, val in enumerate(combination) if grid[i//3][i%3] == 'x']
            return result
    return None

# Call the function and print the result
result = solve_problem()
print(result)

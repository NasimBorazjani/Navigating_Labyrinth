
import itertools

# The initial grid
grid = [['79', '63', '43'],
        ['x', '68', 'x'],
        ['x', 'x', 'x']]

# Function to check if a row is in ascending or descending order
def is_arrange(row):
    return row == sorted(row) or row == sorted(row, reverse=True)

# Function to calculate the sum of the top row, rightmost column, and diagonal
def calculate_sum(grid):
    top_row_sum = sum(int(x) for x in grid[0] if x != 'x')
    rightmost_column_sum = sum(int(grid[i][2]) for i in range(3))
    diagonal_sum = int(grid[0][0]) + int(grid[1][1]) + int(grid[2][2])
    return top_row_sum + rightmost_column_sum + diagonal_sum

# Function to replace the 'x's with unique integers from the given range
def replace_x(grid):
    replacements = []
    for i, j in itertools.product(range(3), repeat=2):
        if grid[i][j] == 'x':
            for k in range(41, 89):
                grid[i][j] = str(k)
                if all(is_arrange(row) for row in grid) and all(is_arrange(column) for column in zip(*grid)):
                    replacements.append((i, j, k))
                    break
                grid[i][j] = 'x'
    return replacements, calculate_sum(grid)

# Call the function to replace the 'x's and print the result
replacements, min_sum = replace_x(grid)
print(replacements)
print("Minimum sum:", min_sum)


import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x', 60],
                 [72, 'x', 'x', 'x'],
                 [63, 70, 'x', 'x'],
                 [61, 75, 'x', 'x']])

# Initialize the constraints
row_sums = [None, 231, 259, None]
col_sums = [None, 247, 236, None]
diag_sum = 234

# Initialize the set of available numbers
available_numbers = set(range(35, 77)) - {60, 72, 63, 70, 61, 75}

# Initialize the solution
solution = []

def solve(grid, row, col):
    # If we have reached the end of the grid, check the constraints
    if row == 4:
        if (all(sum(grid[:,i]) == col_sums[i] or col_sums[i] is None for i in range(4)) and
            sum(grid[i, 3-i] for i in range(4)) == diag_sum):
            return True
        else:
            return False

    # If the current cell is not 'x', move to the next cell
    if grid[row, col] != 'x':
        if solve(grid, row + (col+1)//4, (col+1)%4):
            return True
    else:
        # Try all available numbers
        for num in list(available_numbers):
            grid[row, col] = num
            available_numbers.remove(num)

            # If the current number satisfies the row constraint, move to the next cell
            if row_sums[row] is None or sum(grid[row,:]) <= row_sums[row]:
                if solve(grid, row + (col+1)//4, (col+1)%4):
                    solution.append((row, col, num))
                    return True

            # If the current number does not satisfy the constraint, remove it and try the next number
            grid[row, col] = 'x'
            available_numbers.add(num)

    return False

solve(grid, 0, 0)
solution.reverse()
print(solution)

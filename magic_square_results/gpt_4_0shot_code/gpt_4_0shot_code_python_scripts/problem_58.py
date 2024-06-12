
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x', 40],
                 [34, 37, 'x', 'x'],
                 ['x', 43, 'x', 22],
                 ['x', 'x', 'x', 47]])

# Initialize the sums
col_sums = [None, 137, 162, None]
row_sums = [None, 141, 135, None]
diag_sum = 151

# Initialize the set of available numbers
available_numbers = set(range(22, 54)) - {34, 37, 40, 43, 22, 47}

# Initialize the solution
solution = []

def solve(grid, row=0, col=0):
    # If we have filled the entire grid, check the sums
    if row == 4:
        if (all(sum(grid[:,i]) == s for i, s in enumerate(col_sums) if s is not None) and
            all(sum(grid[i,:]) == s for i, s in enumerate(row_sums) if s is not None) and
            sum(grid[i,3-i] for i in range(4)) == diag_sum):
            return True
        else:
            return False

    # If the current cell is not 'x', move to the next cell
    if grid[row, col] != 'x':
        if solve(grid, row + (col+1)//4, (col+1)%4):
            return True
    else:
        # Try all available numbers for the current cell
        for num in list(available_numbers):
            grid[row, col] = num
            available_numbers.remove(num)
            if solve(grid, row + (col+1)//4, (col+1)%4):
                solution.append((row, col, num))
                return True
            grid[row, col] = 'x'
            available_numbers.add(num)

    return False

solve(grid)
print(solution)

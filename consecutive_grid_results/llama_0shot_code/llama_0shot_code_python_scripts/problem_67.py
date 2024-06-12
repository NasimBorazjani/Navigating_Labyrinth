
# Function to check if a number can be placed in a cell
def is_valid(grid, row, col, num):
    # Check the number is not in the row or column
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

# Function to solve the grid
def solve(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in range(9, 54):
                    if is_valid(grid, i, j, num):
                        # Place the number in the cell and recurse
                        grid[i][j] = num
                        if solve(grid):
                            return True
                        # If the placement leads to a solution, return True
                        # If not, backtrack by replacing the cell with 'x'
                        grid[i][j] = 'x'
                # If no number can be placed in the cell, return False to backtrack
                return False
    # If the grid is filled, return True
    return True

# Function to get the solution
def get_solution(grid):
    if not solve(grid):
        return "No solution"
    # If a solution is found, return it as a list of tuples
    return [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x']

# Initial state of the grid
grid = [['x', '37', 'x', 'x'],
        ['x', '35', '40', 'x'],
        ['15', 'x', 'x', '44'],
        ['11', '20', '36', 'x']]

print(get_solution(grid))

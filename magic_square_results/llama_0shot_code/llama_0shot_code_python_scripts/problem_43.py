
# Function to check if a number is valid at a position
def is_valid(grid, row, col, num):
    # Check the number in the row
    for i in range(4):
        if grid[row][i] == num:
            return False

    # Check the number in the column
    for i in range(4):
        if grid[i][col] == num:
            return False

    # Check the number in the main diagonal
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False

    # Check the number in the counter diagonal
    if row + col == 3:
        for i in range(4):
            if grid[i][3 - i] == num:
                return False

    return True

# Function to solve the magic square
def solve_magic_square(grid):
    # List of all numbers in the grid
    numbers = [i for i in range(35, 62) if i not in grid]

    # Start from the first cell
    row, col = 0, 0

    # List to store the solution
    solution = []

    # Backtracking function
    def backtrack(grid, row, col, numbers):
        # Base case: if all cells are filled
        if len(numbers) == 0:
            return True

        # Try each number
        for num in numbers:
            # If the number is valid at the current position
            if is_valid(grid, row, col, num):
                # Place the number in the grid
                grid[row][col] = num

                # Move to the next cell
                new_row, new_col = row, col + 1
                if new_col == 4:
                    new_row, new_col = row + 1, 0

                # Recurse
                if backtrack(grid, new_row, new_col, numbers[1:]):
                    # If the recursion succeeded, add the solution to the list
                    solution.append((row, col, num))
                    return True

                # If the recursion failed, remove the number from the grid
                grid[row][col] = 'x'

        return False

    # Start the backtracking
    backtrack(grid, row, col, numbers)

    return solution

# Test the function
grid = [['x', '51', '39', 'x'],
        ['x', 'x', '48', '37'],
        ['54', 'x', 'x', 'x'],
        ['x', 'x', 'x', '53']]

print(solve_magic_square(grid))

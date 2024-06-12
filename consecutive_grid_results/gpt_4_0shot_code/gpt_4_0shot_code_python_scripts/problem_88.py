
import numpy as np

# Define the initial grid
grid = np.array([[51, 'x', 68, 'x'],
                 [50, 54, 69, 'x'],
                 ['x', 'x', 70, 'x'],
                 ['x', 'x', 76, 77]])

# Define the range of possible numbers
numbers = set(range(27, 83))

# Find the initial 'x' positions and the initial used numbers
x_positions = []
used_numbers = set()
for i in range(4):
    for j in range(4):
        if grid[i, j] == 'x':
            x_positions.append((i, j))
        else:
            used_numbers.add(grid[i, j])

# Define the available numbers
available_numbers = list(numbers - used_numbers)
available_numbers.sort()

# Define a function to check if a number can be placed at a certain position
def can_place(x, y, num):
    # Check the row
    for j in range(4):
        if grid[x, j] == num:
            return False
    # Check the column
    for i in range(4):
        if grid[i, y] == num:
            return False
    # Check the diagonal
    if x == y:
        for i in range(4):
            if grid[i, i] == num:
                return False
    return True

# Define a function to solve the grid
def solve():
    # If there are no more 'x' positions, the grid is solved
    if not x_positions:
        return True
    # Try to place each available number at the first 'x' position
    x, y = x_positions[0]
    for num in available_numbers:
        if can_place(x, y, num):
            # Place the number
            grid[x, y] = num
            available_numbers.remove(num)
            x_positions.pop(0)
            # Try to solve the rest of the grid
            if solve():
                return True
            # If the rest of the grid can't be solved, undo the placement
            grid[x, y] = 'x'
            available_numbers.append(num)
            x_positions.insert(0, (x, y))
    # If no number can be placed at the first 'x' position, the grid can't be solved
    return False

# Solve the grid
solve()

# Print the solution
solution = []
for i in range(4):
    for j in range(4):
        if (i, j) in x_positions:
            solution.append((i, j, grid[i, j]))
print(solution)

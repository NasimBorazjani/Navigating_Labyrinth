
import numpy as np

def solve_grid():
    # Define the initial grid
    grid = np.array([[22, 'x', 48], [27, 'x', 'x'], ['x', 42, 52]])

    # Define the range of possible numbers
    numbers = set(range(20, 54))

    # Remove the numbers already in the grid from the set of possible numbers
    for row in grid:
        for cell in row:
            if cell != 'x':
                numbers.remove(cell)

    # Convert the set to a list and sort it
    numbers = sorted(list(numbers))

    # Define the positions of the 'x's
    positions = [(0, 1), (1, 1), (1, 2), (2, 0)]

    # Replace the 'x's with the smallest possible numbers
    for pos in positions:
        grid[pos] = numbers.pop(0)

    # Convert the grid to integers
    grid = grid.astype(int)

    # Return the replacements as a list of tuples
    replacements = [(pos[0], pos[1], grid[pos]) for pos in positions]
    return replacements

print(solve_grid())

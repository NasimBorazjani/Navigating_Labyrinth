
import numpy as np

def solve_grid():
    grid = np.array([[22, 35, 40, 47], [0, 0, 37, 45], [18, 24, 0, 0], [0, 17, 0, 0]])
    replacements = []

    # Find the positions of the 'x's
    x_positions = np.where(grid == 0)

    # Create a list of possible numbers that can replace 'x'
    possible_numbers = list(range(9, 50))
    for row in grid:
        for num in row:
            if num in possible_numbers:
                possible_numbers.remove(num)

    # Sort the 'x' positions by the sum of their indices
    # This ensures that we fill the 'x's in the top-left corner first
    sorted_positions = sorted(list(zip(x_positions[0], x_positions[1])), key=sum)

    for pos in sorted_positions:
        for num in possible_numbers:
            # Check if the number can be placed at the current position
            if check_validity(grid, pos, num):
                # If it can, place it and remove it from the list of possible numbers
                grid[pos] = num
                possible_numbers.remove(num)
                replacements.append((pos[0], pos[1], num))
                break

    return replacements

def check_validity(grid, pos, num):
    # Check the row
    row = grid[pos[0]]
    if any(n > num for n in row if n != 0):
        return False

    # Check the column
    col = grid[:, pos[1]]
    if any(n > num for n in col if n != 0):
        return False

    # Check the diagonal
    if pos[0] == pos[1]:
        diag = grid.diagonal()
        if any(n > num for n in diag if n != 0):
            return False

    return True

print(solve_grid())

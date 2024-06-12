
import numpy as np

# Initialize the grid
grid = np.array([[38, 'x', 50, 'x'],
                 ['x', 'x', 64, 67],
                 [54, 'x', 71, 79],
                 ['x', 59, 89, 90]])

# Find all 'x' in the grid
x_positions = np.where(grid == 'x')

# Create a list of tuples for 'x' positions
x_positions = list(zip(x_positions[0], x_positions[1]))

# Create a list of possible numbers
possible_numbers = list(range(36, 92))

# Remove already used numbers from the list
for row in grid:
    for number in row:
        if number in possible_numbers:
            possible_numbers.remove(number)

# Sort the list in ascending order
possible_numbers.sort()

# Create a list to store the replacements
replacements = []

# Iterate over each 'x' position
for position in x_positions:
    # Find the smallest possible number that maintains the order
    for number in possible_numbers:
        row = grid[position[0]]
        column = grid[:, position[1]]
        if ((all(row[i] < number for i in range(position[1])) and all(number < row[i] for i in range(position[1] + 1, len(row)))) or
            (all(row[i] > number for i in range(position[1])) and all(number > row[i] for i in range(position[1] + 1, len(row)))) and
            (all(column[i] < number for i in range(position[0])) and all(number < column[i] for i in range(position[0] + 1, len(column))) or
             (all(column[i] > number for i in range(position[0])) and all(number > column[i] for i in range(position[0] + 1, len(column))))):
            # If the number maintains the order, add it to the replacements and remove it from the possible numbers
            replacements.append((position[0], position[1], number))
            possible_numbers.remove(number)
            break

print(replacements)


import numpy as np

# Initialize the grid
grid = np.array([[12, 'x', 'x'], [18, 'x', 52], [22, 'x', 31]])

# Find the positions of the 'x's
x_positions = np.where(grid == 'x')

# Initialize the list of tuples
tuples = []

# Initialize the list of used numbers
used_numbers = [12, 18, 22, 52, 31]

# Initialize the sum
sum = 12 + 52 + 31

# Loop over the 'x' positions
for i in range(len(x_positions[0])):
    # Find the smallest possible number that can be placed in the current position
    for number in range(13, 61):
        if number not in used_numbers:
            # Check if the number maintains the consecutive order in the row and column
            row = x_positions[0][i]
            col = x_positions[1][i]
            if (grid[row-1, col] < number < grid[row+1, col]) or (grid[row, col-1] < number < grid[row, col+1]):
                # Add the number to the grid and the list of used numbers
                grid[row, col] = number
                used_numbers.append(number)
                # Add the number to the sum if it is in the topmost row, the rightmost column, or the diagonal
                if row == 0 or col == 2 or row == col:
                    sum += number
                # Add the tuple to the list
                tuples.append((row, col, number))
                break

# Print the list of tuples
print(tuples)

# Print the minimized sum
print(sum)

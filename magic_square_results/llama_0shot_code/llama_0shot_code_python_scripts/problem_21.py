
def solve_magic_square(grid):
    # List of all numbers from 50 to 84
    numbers = list(range(50, 85))

    # List to store the tuples
    solution = []

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    # Update the grid with the current number
                    grid[i][j] = num

                    # Check if the current grid configuration satisfies the conditions
                    if (sum(grid[0]) == 193) and (sum(zip(*grid)[0]) == 212) and (sum(diagonal(grid)) == 217):
                        solution.append((i, j, num))
                        numbers.remove(num) # Remove the number from the list to avoid duplicates
                    grid[i][j] = 'x' # Reset the grid
    return solution

def diagonal(grid):
    return [grid[i][i] for i in range(len(grid))]

# Test the function
grid = [['x', 'x', '62'], ['x', 'x', 'x'], ['x', 'x', '56']]
print(solve_magic_square(grid))

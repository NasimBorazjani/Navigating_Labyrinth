
from itertools import permutations

def magic_square(grid):
    # List of all possible numbers
    numbers = list(range(28, 58))
    
    # List to store all possible solutions
    solutions = []
    
    # Go through all possible combinations of numbers
    for nums in permutations(numbers, 9-len(grid[0])):
        new_grid = []
        j = 0
        for i in range(3):
            new_row = []
            for k in range(3):
                if grid[i][k] == 'x':
                    new_row.append(nums[j])
                    j += 1
                else:
                    new_row.append(int(grid[i][k]))
            new_grid.append(new_row)
        
        # Check if the sums of rows, columns, and diagonals are correct
        if (sum(new_grid[0]) == 133 and
            sum(new_grid[1]) == 133 and
            sum(new_grid[2]) == 129 and
            sum(new_grid[i][i] for i in range(3)) == 136 and
            sum(new_grid[i][2-i] for i in range(3)) == 136):
            # If they are, add this combination to the list of solutions
            solutions.append((new_grid[0][1], new_grid[0][2], new_grid[1][1], new_grid[1][2], new_grid[2][1], new_grid[2][2], sum(sum(row) for row in new_grid)))
    
    # Return the combination with the smallest sum of all the numbers in the grid
    return min(solutions, key=lambda x: x[6])

grid = [['41', 'x', 'x'], ['34', 'x', 'x'], ['x', 'x', 'x']]
print(magic_square(grid))


import itertools

def is_magic_square(grid):
    # Check rows
    for row in grid:
        if sum(row) != 213 and sum(row) != 197:
            return False
    
    # Check columns
    for col in range(4):
        if (col == 0 or col == 3) and sum([grid[row][col] for row in range(4)]) != 214:
            return False
        if (col == 1 or col == 2) and sum([grid[row][col] for row in range(4)]) != 240:
            return False
    
    # Check diagonal
    if sum([grid[i][i] for i in range(4)]) != 215:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', '48', '64', '67'],
            ['x', '50', '61', 'x'],
            ['42', 'x', 'x', '74'],
            ['x', 'x', '72', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [num for num in range(37, 84) if num not in [int(cell) for row in grid for cell in row]]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(permutation[i])
        
        if is_magic_square(grid):
            current_sum = sum([int(cell) for row in grid for cell in row])
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)

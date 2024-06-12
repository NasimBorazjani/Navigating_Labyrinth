
import itertools

def is_magic_square(grid):
    # Check rows
    for row in grid:
        if sum(row) != 211 and sum(row) != 161:
            return False
    
    # Check columns
    for col in range(4):
        if (col == 0 or col == 3) and sum([grid[row][col] for row in range(4)]) != 143:
            return False
        if col == 1 or col == 2:
            if sum([grid[row][col] for row in range(4)]) != 170:
                return False
    
    # Check diagonal
    if grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] != 146:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', '32', 'x'],
            ['37', '61', 'x', '54'],
            ['x', 'x', 'x', '62'],
            ['x', '30', 'x', '44']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(22, 69) if val not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            current_sum = sum(itertools.chain(*grid))
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, permutation)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

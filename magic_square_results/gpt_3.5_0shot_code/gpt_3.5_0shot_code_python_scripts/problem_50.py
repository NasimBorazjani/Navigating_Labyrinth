
import itertools

def is_magic_square(grid):
    # Check rows
    for row in grid:
        if sum(row) != 114 and sum(row) != 84:
            return False
    
    # Check columns
    for col in range(4):
        column_sum = sum(grid[row][col] for row in range(4))
        if col == 0 and column_sum != 77:
            return False
        if col == 1 and column_sum != 110:
            return False
    
    # Check diagonal
    diagonal_sum = sum(grid[i][i] for i in range(4))
    if diagonal_sum != 98:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', 'x', '39'],
            ['28', 'x', 'x', 'x'],
            ['x', '11', '33', 'x'],
            ['18', '20', '38', '35']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [i for i in range(9, 41) if i not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            current_sum = sum(itertools.chain(*grid))
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, value) for (row, col), value in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

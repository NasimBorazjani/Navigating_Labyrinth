
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 67 for x in col_sums) and all(x == 60 for x in row_sums) and diag_sum1 == 89 and diag_sum2 == 89

def find_minimal_magic_square():
    grid = [['x', '16', 'x'],
            ['x', 'x', 'x'],
            ['45', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [x for x in range(9, 49) if x not in [int(cell) for row in grid for cell in row if cell != 'x']]
    
    minimal_sum = float('inf')
    minimal_magic_square = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(values[i])
        
        if is_magic_square(grid):
            current_sum = sum(int(cell) for row in grid for cell in row)
            if current_sum < minimal_sum:
                minimal_sum = current_sum
                minimal_magic_square = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return minimal_magic_square

solution = find_minimal_magic_square()
print(solution)

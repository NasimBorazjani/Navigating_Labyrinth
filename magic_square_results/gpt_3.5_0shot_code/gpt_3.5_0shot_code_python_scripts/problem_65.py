
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 192, 173, None] and col_sums == [None, 191, 190, None] and diag_sum1 == 180 and diag_sum2 == 180

def solve_magic_square():
    grid = [['x', '65', '49', '35'],
            ['40', 'x', '52', 'x'],
            ['x', 'x', '34', 'x'],
            ['x', 'x', '55', '61']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(30, 67) if x not in [int(cell) for row in grid for cell in row]]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            return [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
        
        for row, col in unknown_positions:
            grid[row][col] = 'x'

    return None

solution = solve_magic_square()
print(solution)


from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 125, 164, None] and col_sums == [None, 135, 160, None] and diag_sum == 146 and anti_diag_sum == 146

def solve_magic_square():
    grid = [['x', 'x', '40', 'x'],
            ['x', '31', 'x', '43'],
            ['37', 'x', 'x', '32'],
            ['34', '29', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(24, 51) if val not in [int(cell) for row in grid for cell in row if cell != 'x']]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            return [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]

solution = solve_magic_square()
print(solution)

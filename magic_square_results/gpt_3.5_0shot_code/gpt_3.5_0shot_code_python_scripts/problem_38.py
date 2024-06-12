
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 207, 218, None] and col_sums == [None, 227, 215, None] and diag_sum == 195 and anti_diag_sum == 195

def solve_magic_square():
    grid = [['x', '56', 'x', '40'],
            ['x', 'x', '44', '60'],
            ['x', '52', 'x', '45'],
            ['x', 'x', '62', '47']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(40, 67) if x not in [int(cell) for row in grid for cell in row]]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            return [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
        
        for row, col in unknown_positions:
            grid[row][col] = 'x'

solution = solve_magic_square()
print(solution)

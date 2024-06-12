
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 118, 120, None] and col_sums == [None, 146, 168, None] and diag_sum1 == 91 and diag_sum2 == 91

def solve_magic_square():
    grid = [['x', '46', 'x', '22'],
            ['x', 'x', '36', '15'],
            ['47', 'x', 'x', '25'],
            ['x', 'x', '53', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(13, 55) if x not in [int(cell) for row in grid for cell in row]]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(perm[i])
        
        if check_sums(grid):
            return [(row, col, int(val)) for (row, col), val in zip(unknown_positions, perm)]

solution = solve_magic_square()
print(solution)

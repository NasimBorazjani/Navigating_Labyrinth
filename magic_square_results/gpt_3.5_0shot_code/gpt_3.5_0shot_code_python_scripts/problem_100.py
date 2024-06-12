
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 220, 184, None] and col_sums == [None, 239, 192, None] and diag_sum == 199 and anti_diag_sum == 199

def solve_magic_square():
    grid = [['x', 'x', 'x', '67'],
            ['62', 'x', '32', '77'],
            ['66', 'x', '34', 'x'],
            ['x', 'x', '73', '35']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(30, 87) if val not in sum(grid, [])]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, perm):
            grid[pos[0]][pos[1]] = val
        
        if check_sums(grid):
            solution = [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, perm)]
            return solution
    
    return None

solution = solve_magic_square()
print(solution)

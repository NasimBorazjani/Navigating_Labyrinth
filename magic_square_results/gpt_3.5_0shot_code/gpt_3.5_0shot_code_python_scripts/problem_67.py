
from itertools import permutations

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][j] for i, j in zip(range(4), range(3, -1, -1)))
    
    return row_sums == [None, 187, 203, None] and col_sums == [None, 204, 206, None] and diag_sum == 199

def solve_magic_square():
    grid = [['x', '59', '52', '54'],
            ['x', 'x', 'x', '62'],
            ['x', '58', 'x', 'x'],
            ['x', 'x', '63', '42']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(31, 68) if x not in [int(cell) for row in grid for cell in row]]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, perm):
            grid[pos[0]][pos[1]] = str(val)
        
        if check_sums(grid):
            return [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, perm)]

solution = solve_magic_square()
print(solution)


from itertools import permutations

def check_sums(grid):
    row_sums = [sum([int(num) for num in row if num != 'x']) for row in grid]
    col_sums = [sum([int(grid[i][j]) for i in range(4) if grid[i][j] != 'x']) for j in range(4)]
    diag_sum1 = sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])
    diag_sum2 = sum([int(grid[i][3-i]) for i in range(4) if grid[i][3-i] != 'x'])
    
    return row_sums[0] == 105 and row_sums[2] == 115 and col_sums[1] == 148 and col_sums[3] == 109 and diag_sum1 == 134

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['x', '52', '20', 'x'],
            ['41', '13', 'x', 'x'],
            ['54', 'x', '16', '11']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(num) for num in range(11, 63) if str(num) not in sum(grid, [])]
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            return [(row, col, int(val)) for (row, col), val in zip(unknown_positions, perm)]

solution = solve_magic_square()
print(solution)

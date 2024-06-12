
from itertools import permutations

def check_sums(grid):
    row_sums = [180, 176]
    col_sums = [151, 189]
    diag_sum = 184
    
    for i in range(2):
        if sum(grid[i]) != row_sums[i]:
            return False
        if sum([grid[j][i] for j in range(4)]) != col_sums[i]:
            return False
    
    if grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] != diag_sum:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['x', '37', 'x', '41'],
            ['48', 'x', 'x', 'x'],
            ['49', 'x', '46', '38']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(35, 62) if x not in [37, 41, 48, 49, 46, 38]]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if check_sums(grid):
            current_sum = sum([x for row in grid for x in row if x != 'x'])
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, grid[row][col]) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)


from itertools import permutations

def check_sums(grid):
    row_sums = [None, 177, 160, None]
    col_sums = [None, 188, 188, None]
    diagonal_sum = 173
    
    for i in range(4):
        row_sum = sum([int(x) if x != 'x' else 0 for x in grid[i]])
        if row_sums[i] is not None and row_sums[i] != row_sum:
            return False
        
        col_sum = sum([int(grid[j][i]) if grid[j][i] != 'x' else 0 for j in range(4)])
        if col_sums[i] is not None and col_sums[i] != col_sum:
            return False
    
    diagonal_sum_check = int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])
    if diagonal_sum_check != diagonal_sum:
        return False
    
    return True

def solve_magic_square():
    grid = [['x', 'x', '39', 'x'],
            ['x', 'x', 'x', '43'],
            ['x', 'x', 'x', '47'],
            ['46', '49', 'x', '53']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(35, 62)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(perm[i])
        
        if check_sums(grid):
            total_sum = sum([int(x) for row in grid for x in row if x != 'x'])
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)

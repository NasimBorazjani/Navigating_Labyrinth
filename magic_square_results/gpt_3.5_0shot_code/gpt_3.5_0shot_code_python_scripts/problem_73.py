
from itertools import permutations

def check_sums(grid):
    row_sums = [sum([int(x) if x != 'x' else 0 for x in row]) for row in grid]
    col_sums = [sum([int(grid[i][j]) if grid[i][j] != 'x' else 0 for i in range(4)]) for j in range(4)]
    diag_sum = sum([int(grid[i][3-i]) if grid[i][3-i] != 'x' else 0 for i in range(4)])
    
    return row_sums[1] == 116 and row_sums[2] == 124 and col_sums[1] == 144 and col_sums[2] == 76 and diag_sum == 75

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['x', '41', '17', 'x'],
            ['x', 'x', '13', '43'],
            ['9', '24', '27', '11']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(6, 48) if x not in [int(grid[i][j]) for i, j in unknown_positions]]
    
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

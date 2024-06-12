
import itertools

def is_magic_square(grid):
    row_sums = [None, 217, 193, None]
    col_sums = [None, 177, 192, None]
    diagonal_sum = 149
    
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(row[i] for row in grid) != col_sums[i]:
            return False
    
    if sum(grid[i][i] for i in range(4)) != diagonal_sum:
        return False
    if sum(grid[i][3-i] for i in range(4)) != diagonal_sum:
        return False
    
    return True

def solve_magic_square():
    grid = [['62', 'x', 'x', 'x'],
            ['x', '35', '60', 'x'],
            ['x', '39', 'x', '54'],
            ['x', '55', '34', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(22, 69) if val not in [int(cell) for row in grid for cell in row]]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = str(permutation[i])
        
        if is_magic_square(grid):
            current_sum = sum(int(cell) for row in grid for cell in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(grid[row][col])) for row, col in unknown_positions]
    
    return min_solution

solution = solve_magic_square()
print(solution)

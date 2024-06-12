
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum = sum(grid[i][i] for i in range(4))
    anti_diag_sum = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 221, 257, None] and col_sums == [None, 252, 238, None] and diag_sum == 221 and anti_diag_sum == 221

def solve_magic_square():
    grid = [['x', 'x', '80', '72'],
            ['44', 'x', '39', 'x'],
            ['x', '70', '64', 'x'],
            ['x', '67', 'x', '42']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [num for num in range(37, 84)]
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, permutation)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

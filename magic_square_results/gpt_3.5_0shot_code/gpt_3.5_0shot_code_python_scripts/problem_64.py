
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 173, 194, None] and col_sums == [None, 154, 157, None] and diag_sum1 == 208 and diag_sum2 == 208

def solve_magic_square():
    grid = [['46', '30', 'x', '49'],
            ['43', 'x', 'x', '53'],
            ['x', 'x', '37', 'x'],
            ['x', '34', '33', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [str(i) for i in range(30, 67)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            current_sum = sum(int(val) for row in grid for val in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, int(val)) for (row, col), val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

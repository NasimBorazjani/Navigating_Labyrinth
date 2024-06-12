
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 139, 178, None] and col_sums == [None, 187, 186, None] and diag_sum1 == 160 and diag_sum2 == 160

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['24', 'x', '27', '41'],
            ['22', '37', 'x', 'x'],
            ['29', 'x', 'x', '46']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [val for val in range(22, 69) if val not in itertools.chain.from_iterable(grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = perm[i]
        
        if is_magic_square(grid):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, perm)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

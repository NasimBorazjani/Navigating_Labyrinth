
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 101, 108, None] and col_sums == [None, 125, 51, None] and diag_sum1 == 90 and diag_sum2 == 90

def solve_magic_square():
    grid = [['x', 'x', 'x', 'x'],
            ['28', '33', 'x', 'x'],
            ['16', 'x', 'x', '37'],
            ['36', '18', '7', '23']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [i for i in range(6, 48) if i not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = val
        
        if is_magic_square(grid):
            total_sum = sum(itertools.chain(*grid))
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, values)]
        
        for pos in unknown_positions:
            grid[pos[0]][pos[1]] = 'x'
    
    return min_solution

solution = solve_magic_square()
print(solution)

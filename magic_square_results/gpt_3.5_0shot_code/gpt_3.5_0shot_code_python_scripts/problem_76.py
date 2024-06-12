
import itertools

def check_sums(grid):
    row_sums = [sum(row) if None not in row else None for row in grid]
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(4))
    diag_sum2 = sum(grid[i][3-i] for i in range(4))
    
    return row_sums == [None, 94, 109, None] and col_sums == [None, 128, 80, None] and diag_sum1 == 99 and diag_sum2 == 99

def solve_magic_square():
    grid = [['26', '38', '27', 'x'],
            ['x', 'x', 'x', '19'],
            ['x', '43', 'x', 'x'],
            ['42', 'x', '34', '20']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [i for i in range(6, 48) if i not in [int(num) for row in grid for num in row if num != 'x']]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = str(val)
        
        if check_sums(grid):
            total_sum = sum(int(num) for row in grid for num in row if num != 'x')
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)


import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 82 for sum in row_sums) and all(sum == 82 for sum in col_sums) and diag_sum1 == 96 and diag_sum2 == 96

def find_minimal_magic_square():
    grid = [['x', '20', 'x'],
            ['x', 'x', 'x'],
            ['x', 'x', '33']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [num for num in range(19, 44)]
    
    min_sum = float('inf')
    min_square = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, value in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = str(value)
        
        if is_magic_square(grid):
            current_sum = sum(int(num) for row in grid for num in row)
            if current_sum < min_sum:
                min_sum = current_sum
                min_square = [(pos[0], pos[1], value) for pos, value in zip(unknown_positions, values)]
    
    return min_square

solution = find_minimal_magic_square()
print(solution)

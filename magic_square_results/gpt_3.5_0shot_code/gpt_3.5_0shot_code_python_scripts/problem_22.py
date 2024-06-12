
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 120 for sum in col_sums) and all(sum == 105 for sum in row_sums) and diag_sum1 == 99 and diag_sum2 == 99

def find_minimal_magic_square():
    grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '43', 'x']]
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [val for val in range(12, 47) if val != 43]
    
    min_sum = float('inf')
    min_square = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for pos, val in zip(unknown_positions, values):
            grid[pos[0]][pos[1]] = val
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_square = [(pos[0], pos[1], val) for pos, val in zip(unknown_positions, values)]
    
    return min_square

solution = find_minimal_magic_square()
print(solution)


import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diagonal_sum1 = sum(grid[i][i] for i in range(3))
    diagonal_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 177 for sum in col_sums) and all(sum == 180 for sum in row_sums) and diagonal_sum1 == 183 and diagonal_sum2 == 183

def find_minimal_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', '73', '47'],
            ['x', 'x', 'x']]
    
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_values = [val for val in range(34, 79) if val not in [73, 47]]
    
    minimal_sum = float('inf')
    minimal_magic_square = None
    
    for permutation in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < minimal_sum:
                minimal_sum = current_sum
                minimal_magic_square = [(row, col, val) for (row, col), val in zip(unknown_positions, permutation)]
    
    return minimal_magic_square

solution = find_minimal_magic_square()
print(solution)

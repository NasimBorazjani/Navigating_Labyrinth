
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diagonal_sum1 = sum(grid[i][i] for i in range(3))
    diagonal_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 115 for sum in col_sums) and all(sum == 95 for sum in row_sums) and diagonal_sum1 == 133 and diagonal_sum2 == 133

def find_minimal_sum(grid):
    min_sum = float('inf')
    min_grid = None
    
    for permutation in itertools.permutations(range(9, 49), 6):
        new_grid = [row.copy() for row in grid]
        idx = 0
        for i in range(3):
            for j in range(3):
                if new_grid[i][j] == 'x':
                    new_grid[i][j] = permutation[idx]
                    idx += 1
        
        if is_magic_square(new_grid):
            current_sum = sum(sum(row) for row in new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = new_grid
    
    return min_grid

grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['42', '45', 'x']]

solution = find_minimal_sum(grid)
print(solution)

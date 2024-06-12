
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 212 for x in col_sums) and all(x == 193 for x in row_sums) and diag_sum1 == 217 and diag_sum2 == 217

def find_min_sum_magic_square():
    possible_values = [x for x in range(50, 85)]
    unknown_positions = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
    min_sum = float('inf')
    min_square = None
    
    for perm in itertools.permutations(possible_values, len(unknown_positions)):
        grid = [['x', 'x', 62], ['x', 'x', 'x'], ['x', 'x', 56]]
        for i, pos in enumerate(unknown_positions):
            grid[pos[0]][pos[1]] = perm[i]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_square = grid
    
    return [(i, j, min_square[i][j]) for i in range(3) for j in range(3) if min_square[i][j] != 'x']

solution = find_min_sum_magic_square()
print(solution)

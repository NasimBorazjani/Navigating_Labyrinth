
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 135 for x in col_sums) and all(x == 134 for x in row_sums) and diag_sum1 == 122 and diag_sum2 == 122

def find_min_sum_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['41', 'x', 'x']]
    
    possible_values = [i for i in range(31, 76) if i != 41]
    min_sum = float('inf')
    min_square = None
    
    for perm in itertools.permutations(possible_values, 6):
        grid[0][0] = perm[0]
        grid[0][1] = perm[1]
        grid[0][2] = perm[2]
        grid[1][0] = perm[3]
        grid[1][1] = perm[4]
        grid[2][1] = perm[5]
        
        if is_magic_square(grid):
            current_sum = sum(perm)
            if current_sum < min_sum:
                min_sum = current_sum
                min_square = grid.copy()
    
    return [(i, j, int(min_square[i][j])) for i in range(3) for j in range(3) if min_square[i][j] == 'x']

solution = find_min_sum_magic_square()
print(solution)

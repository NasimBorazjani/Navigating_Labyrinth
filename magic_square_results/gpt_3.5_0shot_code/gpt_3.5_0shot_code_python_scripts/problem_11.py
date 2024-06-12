
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diagonal_sum1 = sum(grid[i][i] for i in range(3))
    diagonal_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 127 for sum in col_sums) and all(sum == 144 for sum in row_sums) and diagonal_sum1 == 141 and diagonal_sum2 == 141

def find_min_sum_magic_square():
    possible_values = [i for i in range(35, 60)]
    grid = [['x', 'x', 48], ['x', 'x', 'x'], ['x', 'x', 'x']]
    min_sum = float('inf')
    min_grid = None
    
    for permutation in itertools.permutations(possible_values, 6):
        grid[0][0] = permutation[0]
        grid[0][1] = permutation[1]
        grid[1][0] = permutation[2]
        grid[1][1] = permutation[3]
        grid[1][2] = permutation[4]
        grid[2][0] = permutation[5]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = [tuple([i, j, grid[i][j]]) for i in range(3) for j in range(3) if grid[i][j] != 'x']
    
    return min_grid

solution = find_min_sum_magic_square()
print(solution)

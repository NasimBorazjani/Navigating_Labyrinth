
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 125 for x in col_sums) and all(x == 157 for x in row_sums) and diag_sum1 == 138 and diag_sum2 == 138

def solve_magic_square():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['37', 'x', 'x']]
    
    possible_values = [x for x in range(35, 60) if x != 37]
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_values, 6):
        temp_grid = [row.copy() for row in grid]
        temp_grid[2][0] = 37
        temp_grid[0][0] = permutation[0]
        temp_grid[0][1] = permutation[1]
        temp_grid[0][2] = permutation[2]
        temp_grid[1][1] = permutation[3]
        temp_grid[1][2] = permutation[4]
        temp_grid[2][2] = permutation[5]
        
        if is_magic_square(temp_grid):
            temp_sum = sum(sum(row) for row in temp_grid)
            if temp_sum < min_sum:
                min_sum = temp_sum
                min_solution = [(i, j, temp_grid[i][j]) for i in range(3) for j in range(3) if temp_grid[i][j] != 'x']
    
    return min_solution

solution = solve_magic_square()
print(solution)

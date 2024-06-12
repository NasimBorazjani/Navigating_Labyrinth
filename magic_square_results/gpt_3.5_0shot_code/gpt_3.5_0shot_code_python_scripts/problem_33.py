
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(sum == 138 for sum in col_sums) and all(sum == 171 for sum in row_sums) and diag_sum1 == 145 and diag_sum2 == 145

def find_unique_integers(grid):
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    possible_integers = [num for num in range(31, 76)]
    
    min_sum = float('inf')
    min_combination = None
    
    for combination in itertools.permutations(possible_integers, len(unknown_positions)):
        new_grid = [row.copy() for row in grid]
        for pos, num in zip(unknown_positions, combination):
            new_grid[pos[0]][pos[1]] = num
        
        if is_magic_square(new_grid):
            current_sum = sum(sum(row) for row in new_grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_combination = [(pos[0], pos[1], num) for pos, num in zip(unknown_positions, combination)]
    
    return min_combination

grid = [['x', 'x', 'x'],
        ['x', 'x', 'x'],
        ['x', 'x', 55]]

solution = find_unique_integers(grid)
print(solution)


import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 151 for x in row_sums) and all(x == 154 for x in col_sums) and diag_sum1 == 133 and diag_sum2 == 133

def find_unique_integers():
    grid = [['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['x', 'x', 57]]
    
    possible_integers = [x for x in range(35, 60)]
    unknown_positions = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 'x']
    
    min_sum = float('inf')
    min_solution = None
    
    for permutation in itertools.permutations(possible_integers, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = permutation[i]
        
        if is_magic_square(grid):
            current_sum = sum(sum(row) for row in grid)
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, permutation)]
    
    return min_solution

solution = find_unique_integers()
print(solution)


import itertools

def is_magic_square(grid):
    # Check column sums
    col_sums = [sum(col) if None not in col else None for col in zip(*grid)]
    if col_sums != [None, 267, 236, None]:
        return False
    
    # Check row sums
    row_sums = [sum(row) if None not in row else None for row in grid]
    if row_sums != [None, 270, 234, None]:
        return False
    
    # Check diagonal sum
    diagonal_sum = sum(grid[i][3-i] for i in range(4))
    if diagonal_sum != 301:
        return False
    
    return True

def solve_magic_square():
    grid = [['48', 'x', 'x', 'x'],
            ['54', 'x', 'x', 'x'],
            ['x', '64', '44', '83'],
            ['82', '68', '51', 'x']]
    
    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [num for num in range(41, 93) if num not in itertools.chain(*grid)]
    
    min_sum = float('inf')
    min_solution = None
    
    for values in itertools.permutations(possible_values, len(unknown_positions)):
        for i, (row, col) in enumerate(unknown_positions):
            grid[row][col] = values[i]
        
        if is_magic_square(grid):
            current_sum = sum(itertools.chain(*grid))
            if current_sum < min_sum:
                min_sum = current_sum
                min_solution = [(row, col, val) for (row, col), val in zip(unknown_positions, values)]
    
    return min_solution

solution = solve_magic_square()
print(solution)

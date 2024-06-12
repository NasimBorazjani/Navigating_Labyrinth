import numpy as np

def is_feasible(grid, edge_length, lower_range, upper_range, solution):
    grid = eval(grid)
    count_masked = sum(i == "" or i == None for sublist in grid for i in sublist)
    
    if count_masked != len(solution):
        return False
    
    seen_numbers = set([int(i) for sublist in grid for i in sublist if i != ""])   
    for sol in solution:
        if not (type(sol[0]) == int and type(sol[1]) == int and type(sol[2]) == int):
            return False
        # Check if the coordinates are valid
        if not (0 <= sol[0] < edge_length  and 0 <= sol[1] < edge_length):
            return False
        # Check if the value is in the given range and is unique
        if not (lower_range <= sol[2] < upper_range) or sol[2] in seen_numbers:
            return False
        else:
            seen_numbers.add(sol[2])
        if grid[sol[0]][sol[1]]:
            return False
    return True

import copy   
def is_correct(grid_str, lower_range, upper_range, col_range, row_range,
               sum_cols, sum_rows, sum_diag, solution):
    try:
        grid = eval(grid_str)
        if not is_feasible(grid_str, len(grid), lower_range, upper_range, solution):
            return False, None
        
        # Fill the 'x' positions in the grid with the numbers in the solution
        for sol in solution:
            grid[sol[0]][sol[1]] = sol[2]
            
        grid = np.array([[int(j) for j in i] for i in grid])
        
        # Calculate the sums
        new_sum_cols = np.sum(grid[:,col_range[0]:col_range[1]], axis=0)
        new_sum_rows = np.sum(grid[row_range[0]:row_range[1],:], axis=1)
        new_sum_diag = np.trace(np.fliplr(grid))
        
        # Check if the sums match
        if not (np.array_equal(sum_cols, new_sum_cols) and
                np.array_equal(sum_rows, new_sum_rows) and 
                sum_diag == new_sum_diag):
            return False, None
        
        return True, int(np.sum(grid))
    except Exception as e:
        print(e)
        print(solution)
        print(grid, lower_range, upper_range, col_range, row_range,
               sum_cols, sum_rows, sum_diag, solution)
    

print(is_correct("[['', '32', ''], ['38', '', ''], ['', '', '']]",
            28,
            57,
            [
                1,
                2
            ],
            [
                1,
                2
            ],
            [
                143
            ],
            [
                134
            ],
            131, [(0, 0, 28), (0, 2, 29), (1, 1, 57), (1, 2, 39), (2, 0, 45), (2, 1, 54), (2, 2, 30)]))
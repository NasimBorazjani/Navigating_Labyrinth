import numpy as np

def is_feasible(grid, lower_range, upper_range, solution):
    grid = eval(grid)
    edge_length = len(grid[0])
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
        
    # Fill the 'x' positions in the grid with the numbers in the solution
    for sol in solution:
        if type(grid[sol[0]][sol[1]]) != str:
            return False
        grid[sol[0]][sol[1]] = sol[2]
        
    grid = np.array([[int(j) for j in i] for i in grid])
    
   
    return True


import copy   
def is_correct(grid, lower_range, upper_range, solution):
    try:
        if not is_feasible(grid, lower_range, upper_range, solution):
            return False, None
        
        grid = eval(grid)
        
        # Fill the 'x' positions in the grid with the numbers in the solution
        for sol in solution:
            if type(grid[sol[0]][sol[1]]) != str:
                return False, None
            grid[sol[0]][sol[1]] = sol[2]
            
        grid = np.array([[int(j) for j in i] for i in grid])
        
        for row in grid:
            if not (all(row[i] < row[i+1] for i in range(len(row)-1)) or
                    all(row[i] > row[i+1] for i in range(len(row)-1))):
                return False, None

        # Check columns
        for col in zip(*grid):
            if not (all(col[i] < col[i+1] for i in range(len(col)-1)) or
                    all(col[i] > col[i+1] for i in range(len(col)-1))):
                return False, None
        
        return True, int(sum(grid[0]) + sum(row[-1] for row in grid) + sum(grid[i][i] for i in range(len(grid))))
    
    except Exception as e:
        print(e)
        print(solution)
        print(grid, lower_range, upper_range, solution)
        
        
print(is_correct( "[['', '', '85'], ['58', '', '84'], ['', '74', '59']]", 48,91, [(0, 0, 48), (0, 1, 49), (1, 1, 59), (2, 0, 75)]))
   
   

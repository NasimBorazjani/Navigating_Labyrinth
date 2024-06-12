
import heapq
import numpy as np

def a_star():
    # Define the initial state of the grid
    grid = np.array([['x', '51', 'x'],
                     ['48', '50', 'x'],
                     ['x', 'x', 'x']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(22, 76))
    
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    
    # The information we must encode for each state includes the grid and the set of available numbers
    initial_state = (grid, numbers)
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heappop(queue)
        
        # Unpack the information encoded in each state
        state_grid, state_numbers = state
        
        # If there is at least 1 remaining unknown number in the grid
        if 'x' in state_grid:
            # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
            for i in range(num_rows):
                for j in range(num_cols):
                    if state_grid[i][j] == 'x':
                        for num in state_numbers:
                            new_grid = state_grid.copy()
                            new_grid[i][j] = num
                            new_numbers = state_numbers.copy()
                            new_numbers.remove(num)
                            new_state = (new_grid, new_numbers)
                            new_cost = g + heuristic(new_grid)
                            
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_state))
        else:
            return actions

def heuristic(grid):
    # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that each number must only appear once in the grid
    # It presumes that the sum of the numbers in the topmost row, rightmost column, and diagonal should be minimized, thus providing a lower estimate on the cost to reach the goal state
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum possible decrease in the sum of the topmost row, rightmost column, and diagonal is 1
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])
    right_col_sum = sum([int(num) for num in grid[:, -1] if num != 'x'])
    diagonal_sum = sum([int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x'])
    
    return top_row_sum + right_col_sum + diagonal_sum

print(a_star())

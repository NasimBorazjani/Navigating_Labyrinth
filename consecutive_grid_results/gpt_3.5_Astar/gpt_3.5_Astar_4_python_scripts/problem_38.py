
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([['x', '89', '95'],
                     ['x', 'x', '96'],
                     ['74', '93', 'x']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(45, 99))
    
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    
    # The information we must encode for each state includes the grid and the set of available numbers to replace 'x'
    initial_state = (grid, numbers)
    
    # Initialize the priority queue with the initial state
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        state_grid, state_numbers = state
        
        # If there is at least 1 remaining unknown number in the grid
        if 'x' in state_grid:
            # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
            for row in range(num_rows):
                for col in range(num_cols):
                    if state_grid[row][col] == 'x':
                        for num in state_numbers:
                            new_grid = state_grid.copy()
                            new_grid[row][col] = str(num)
                            new_numbers = state_numbers.copy()
                            new_numbers.remove(num)
                            new_state = (new_grid, new_numbers)
                            new_cost = g + heuristic(new_grid)
                            
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(row, col, num)], new_state))
        else:
            return actions
    
    return None


def heuristic(grid):
    # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and the diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, as it presumes we can replace the 'x's with any number in the range
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is the difference between the largest and smallest number in the range
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])
    right_col_sum = sum([int(num) for num in grid[:, -1] if num != 'x'])
    diagonal_sum = sum([int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x'])
    
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

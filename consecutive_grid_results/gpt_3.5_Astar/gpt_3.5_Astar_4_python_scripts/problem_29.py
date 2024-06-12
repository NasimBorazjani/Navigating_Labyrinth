
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', 65],
                      ['x', 47, 56],
                      [48, 44, 'x']])
    
    # Define the range of numbers that can be used to replace 'x's
    numbers = set(range(40, 89))
    
    # Define the initial state as a tuple of the grid and the set of available numbers
    initial_state = (grid, numbers)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heappop(queue)
        
        # Unpack the grid and available numbers from the state
        grid, numbers = state
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in grid:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for num in numbers:
                        # Create a copy of the grid and available numbers
                        new_grid = grid.copy()
                        new_numbers = numbers.copy()
                        # Replace the 'x' with the new number
                        new_grid[i][j] = num
                        # Remove the new number from the available numbers
                        new_numbers.remove(num)
                        # Generate the new state
                        new_state = (new_grid, new_numbers)
                        # Calculate the cost of the new state
                        new_cost = g + heuristic(new_grid)
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Add the action to the list of actions
                            heappush(queue, (new_cost, new_cost, actions + [(i, j, num)], new_state))
    
    return None


def heuristic(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(grid[0][grid[0] != 'x'])
    right_col_sum = np.sum(grid[:, 2][grid[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(grid))
    
    # Return the sum of the three sums as the heuristic value
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

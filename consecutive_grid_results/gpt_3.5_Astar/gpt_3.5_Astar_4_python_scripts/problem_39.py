
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', '60', 'x'],
                     ['x', 'x', '53'],
                     ['52', '39', '20']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(18, 72))
    
    # Define the initial state as a tuple of the grid and the set of available numbers
    initial_state = (grid, numbers)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the state into the grid and the set of available numbers
        grid, numbers = state
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in grid:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for num in numbers:
                        # Create a copy of the grid and the set of available numbers
                        new_grid = grid.copy()
                        new_numbers = numbers.copy()
                        
                        # Replace 'x' with the new number in the copy of the grid
                        new_grid[i][j] = str(num)
                        # Update the set of available numbers by removing the new number
                        new_numbers.remove(num)
                        
                        # Generate the new state
                        new_state = (new_grid, new_numbers)
                        # Calculate the cost of the new state as the sum of the numbers in the top row, rightmost column, and diagonal
                        new_cost = g + num
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_state))
    
    return None

def heuristic(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])
    right_col_sum = sum([int(num) for num in grid[:, 2] if num != 'x'])
    diagonal_sum = sum([int(grid[i][i]) for i in range(3) if grid[i][i] != 'x'])
    
    return top_row_sum + right_col_sum + diagonal_sum

print(a_star())

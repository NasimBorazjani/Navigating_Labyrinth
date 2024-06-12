
import heapq
import numpy as np

def a_star():
    # Define the initial state of the grid
    grid = np.array([[46, 80, 90],
                     [51, 'x', 'x'],
                     ['x', 'x', 'x']])
    
    # Define the range of numbers that can be used to replace 'x's
    numbers = list(range(45, 99))
    
    # Define the dimensions of the grid
    num_rows, num_cols = grid.shape
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    
    # Define the initial state as a tuple
    initial_state = (grid, set(numbers))
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the state
        current_grid, available_numbers = state
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in current_grid:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if current_grid[i][j] == 'x':
                    for num in available_numbers:
                        # Create a copy of the current grid to modify
                        new_grid = current_grid.copy()
                        new_grid[i][j] = num
                        
                        # Filter out the 'x's to avoid errors when comparing elements
                        row = [elem for elem in new_grid[i] if elem != 'x']
                        col = [new_grid[row][j] for row in range(num_rows) if new_grid[row][j] != 'x']
                        
                        # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
                        diagonal_sum = sum([new_grid[i][i] for i in range(num_rows) if new_grid[i][i] != 'x'])
                        new_cost = g + sum(row) + sum(col) + diagonal_sum
                        
                        # Update the set of available numbers after adding a number to the grid
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        
                        new_state = (new_grid, new_available_numbers)
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_grid, new_available_numbers), new_cost, actions + [(i, j, num)], new_state))
    
    return None

def heuristic(grid, available_numbers):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = sum([grid[0][j] for j in range(grid.shape[1]) if grid[0][j] != 'x'])
    right_col_sum = sum([grid[i][-1] for i in range(grid.shape[0]) if grid[i][-1] != 'x'])
    diagonal_sum = sum([grid[i][i] for i in range(grid.shape[0]) if grid[i][i] != 'x'])
    
    # Calculate the heuristic value as the sum of the topmost row, rightmost column, and diagonal
    h = top_row_sum + right_col_sum + diagonal_sum
    
    return h

print(a_star())

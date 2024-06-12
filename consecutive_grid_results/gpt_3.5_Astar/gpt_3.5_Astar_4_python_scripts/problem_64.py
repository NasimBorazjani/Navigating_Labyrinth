
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', '68', '71', 'x'],
                     ['x', 'x', '62', 'x'],
                     ['43', 'x', '55', 'x'],
                     ['44', '45', '52', '58']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(31, 77))
    
    # Define the initial state as a tuple of the grid and the set of available numbers
    initial_state = (grid, set(numbers))
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heappop(queue)
        
        # Unpack the grid and available numbers from the state
        grid, available_numbers = state
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in grid:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 'x':
                    for num in available_numbers:
                        # Create a copy of the grid and available numbers
                        new_grid = grid.copy()
                        new_available_numbers = available_numbers.copy()
                        
                        # Replace 'x' with the new number in the grid
                        new_grid[i][j] = str(num)
                        # Remove the new number from the available numbers
                        new_available_numbers.remove(num)
                        
                        # Generate the new state
                        new_state = (new_grid, new_available_numbers)
                        # Calculate the cost of the new state based on the sum of the top row, rightmost column, and diagonal
                        new_cost = g + sum([int(new_grid[0][k]) for k in range(4)]) + sum([int(new_grid[l][3]) for l in range(4)]) + sum([int(new_grid[m][m]) for m in range(4)])
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Add the action to the list of actions
                            actions.append((i, j, num))
                            heappush(queue, (new_cost, g + 1, actions.copy(), new_state))
                            # Remove the action to backtrack and try other possibilities
                            actions.pop()
    
    return None

print(a_star())

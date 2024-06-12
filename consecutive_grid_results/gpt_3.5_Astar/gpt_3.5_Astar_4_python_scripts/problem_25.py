
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', 'x'],
                     ['39', 'x', '52'],
                     ['60', 'x', 'x']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(29, 73))
    
    # Define the initial state as a tuple of the grid and the set of available numbers
    initial_state = (grid, numbers)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
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
                        
                        # Replace 'x' with the new number
                        new_grid[i][j] = str(num)
                        # Update the set of available numbers
                        new_numbers.remove(num)
                        
                        # Generate the new state
                        new_state = (new_grid, new_numbers)
                        # Calculate the cost of the new state based on the sum of the numbers in the top row, rightmost column, and diagonal
                        new_cost = g + num + sum(int(new_grid[0][k]) for k in range(3)) + sum(int(new_grid[l][2]) for l in range(3)) + int(new_grid[0][0]) + int(new_grid[1][1]) + int(new_grid[2][2])
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_state))
    
    return None

def heuristic(grid):
    # Calculate the heuristic as the sum of the numbers in the top row, rightmost column, and diagonal
    return sum(int(grid[0][k]) for k in range(3)) + sum(int(grid[l][2]) for l in range(3)) + int(grid[0][0]) + int(grid[1][1]) + int(grid[2][2])

print(a_star())

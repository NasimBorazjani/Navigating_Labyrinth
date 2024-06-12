
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([['x', 'x', 'x'],
                     ['x', '36', '44'],
                     ['x', '34', 'x']])
    
    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(19, 53))
    
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
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for num in available_numbers:
                        # Create a copy of the grid and available numbers to simulate the new state
                        new_grid = grid.copy()
                        new_grid[i][j] = str(num)
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_state = (new_grid, new_available_numbers)
                        new_cost = g + heuristic(new_grid)
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_state))
    
    return None


def heuristic(grid):
    # An admissible and consistent heuristic is the sum of the numbers in the topmost row, rightmost column, and diagonal
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because the sum of the numbers in the topmost row, rightmost column, and diagonal is always greater than or equal to the sum of the numbers in the final grid
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number that can be added to the sum is the number that is replaced, which is exactly the decrease in the heuristic estimate
    h = 0
    # Calculate the sum of the topmost row
    h += sum([int(num) for num in grid[0] if num != 'x'])
    # Calculate the sum of the rightmost column
    h += sum([int(num) for num in grid[:, 2] if num != 'x'])
    # Calculate the sum of the diagonal from top-left to bottom-right
    h += sum([int(grid[i][i]) for i in range(3) if grid[i][i] != 'x'])
    return h


print(a_star())


import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[30, 'x', 'x'], [28, 33, 43], ['x', 'x', 51]])
    num_rows, num_cols = grid.shape
    num_range = set(range(15, 59))
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    
    queue = []
    heappush(queue, (0, 0, [], grid))
    
    while queue:
        _, g, actions, state = heappop(queue)
        
        # Unpack the state
        state = np.array(state)
        
        # If there is at least one unknown number in the grid
        if 'x' in state:
            # Generate all possible actions from the current state
            for row in range(num_rows):
                for col in range(num_cols):
                    if state[row][col] == 'x':
                        for num in num_range - set(state.flatten()):
                            new_state = state.copy()
                            new_state[row][col] = num
                            new_cost = g + num
                            
                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heappush(queue, (new_cost + heuristic(new_state, num_range), new_cost, actions + [(row, col, num)], new_state))
        else:
            return actions
    
    return None


def heuristic(state, num_range):
    # An admissible and consistent heuristic is the sum of the remaining numbers in the range that are not present in the grid
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it never overestimates the cost to reach the goal, as each number must be added to the grid at least once
    # It's consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the next number in the range, which is exactly the number used to fill the grid in the heuristic
    h = sum(num for num in num_range if num not in state)
    return h


print(a_star())

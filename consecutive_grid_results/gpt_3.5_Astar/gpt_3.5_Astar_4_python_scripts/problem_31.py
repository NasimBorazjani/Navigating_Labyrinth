
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([[10, 25, 'x'],
                     ['x', 'x', 45],
                     ['x', 7, 'x']])
    
    # Define the range of numbers that can replace 'x'
    numbers = set(range(5, 54))
    
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid, numbers))
    
    while queue:
        _, g, actions, state, available_numbers = heappop(queue)
        
        # Unpack the state
        state = np.array(state)
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i][j] = num
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + heuristic(new_state)
                        
                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost, new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
    
    return None


def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that each number must be unique
    # It presumes that the sum of the numbers in the topmost row, rightmost column, and diagonal should be minimized, and thus provides a lower estimate on the cost to reach the goal state
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the sum of the numbers in the topmost row, rightmost column, and diagonal will only increase by the value of the number added
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, 2][state[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])
    
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

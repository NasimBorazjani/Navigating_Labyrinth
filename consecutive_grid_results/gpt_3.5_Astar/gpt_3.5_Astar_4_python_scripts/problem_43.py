
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid, encoding the numbers as integers and the unknown numbers as 'x'
    initial_state = np.array([[13, 'x', 'x'], ['x', 'x', 27], ['x', 26, 'x']])
    num_rows = 3
    num_cols = 3
    num_range = range(7, 61)
    
    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the state to a numpy array
        state = np.array(state)
        
        # If there are no unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions
        
        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        available_numbers = set(num_range) - set(state.flatten())
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i][j] = num
                        new_cost = g + num
                        
                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, num_range), new_cost, actions + [(i, j, num)], new_state))
    
    return None


def heuristic(state, num_range):
    # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and the diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that each number must be unique
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum possible decrease in the heuristic is 1, which is the cost of adding the number to the grid
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, -1][state[:, -1] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])
    
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

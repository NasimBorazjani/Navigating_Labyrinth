
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', '58', 'x'],
                     ['44', '54', '59', 'x'],
                     ['43', 'x', '63', '75'],
                     ['x', 'x', 'x', '84']])
    
    # Define the range of numbers that can replace 'x'
    numbers = list(range(36, 87))
    
    # Define the initial state as a tuple
    initial_state = tuple(map(tuple, grid))
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, set(numbers))]
    
    while queue:
        _, g, actions, state, available_numbers = heapq.heappop(queue)
        
        # Unpack the state
        state = np.array(state)
        
        # If there are no more 'x's in the grid, return the actions taken
        if 'x' not in state:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        # Check if replacing 'x' with num maintains the strictly increasing or decreasing order in each row and column
                        if (all(state[i, k] == 'x' or (state[i, k] < state[i, k+1]) for k in range(num_cols-1)) or
                            all(state[i, k] == 'x' or (state[i, k] > state[i, k+1]) for k in range(num_cols-1)) and
                            all(state[k, j] == 'x' or (state[k, j] < state[k+1, j]) for k in range(num_rows-1)) or
                            all(state[k, j] == 'x' or (state[k, j] > state[k+1, j]) for k in range(num_rows-1))):
                            
                            # Generate the new state
                            new_state = state.copy()
                            new_state[i][j] = num
                            new_state = tuple(map(tuple, new_state))
                            
                            # Update the set of available numbers
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)
                            
                            # The cost so far is the number of actions taken
                            new_cost = g + num
                            
                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
    return None

def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = sum([state[0][j] for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([state[i][3] for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([state[i][i] for i in range(4) if state[i][i] != 'x'])
    
    # Calculate the heuristic value as the sum of the three sums
    h = top_row_sum + right_col_sum + diagonal_sum
    
    return h

print(a_star())

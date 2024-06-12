
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([[47, 51, 'x', 64],
                      [50, 53, 'x', 'x'],
                      ['x', 55, 68, 74],
                      ['x', 'x', 72, 'x']])
    
    # Define the range of numbers that can replace 'x'
    numbers = list(range(37, 88))
    
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
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions
        
        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        # Check if replacing 'x' with the number maintains the consecutive order in each row and column
                        if (check_row(state[i]) and check_col(state[:, j]) and
                            check_row(state[:, j]) and check_col(state[i]) and
                            num not in state):
                            
                            # Generate the new state
                            new_state = state.copy()
                            new_state[i][j] = num
                            
                            # Update the set of available numbers
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)
                            
                            # The cost so far is the number being replaced
                            new_cost = g + num
                            
                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
    
    return None

def heuristic(state, numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
    # The heuristic is admissible because it is the minimum possible value that can replace the remaining 'x's in the grid, ensuring it never overestimates the cost to reach the goal
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced, or equal or less by at most the value of the number replaced, which is exactly the cost of reaching the successor node
    h = 0
    for row in state:
        for item in row:
            if item == 'x':
                h += min(numbers)
    return h

def check_row(row):
    # Helper function to check if a row is in consecutive order
    if 'x' in row:
        return True
    return all(row[i] < row[i+1] for i in range(len(row)-1)) or all(row[i] > row[i+1] for i in range(len(row)-1)

def check_col(col):
    # Helper function to check if a column is in consecutive order
    if 'x' in col:
        return True
    return all(col[i] < col[i+1] for i in range(len(col)-1)) or all(col[i] > col[i+1] for i in range(len(col)-1)

print(a_star())

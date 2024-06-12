
import heapq
import numpy as np

def initialize():
    # Define the initial state of the grid, as a 3x3 numpy array
    initial_state = np.array([['x', 42, 38], ['x', 'x', 'x'], ['x', 63, 'x']])
    
    # Define the range of numbers that can be used to replace 'x's
    num_range = set(range(38, 76))
    
    # Define the dimensions of the grid
    num_rows = 3
    num_cols = 3
    
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, num_range)]
    
    return initial_state, num_range, num_rows, num_cols, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of numbers, and the dimensions of the grid)
    initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()
    
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, available_nums = heapq.heappop(queue)
        
        # If the current state has no 'x's, ie all numbers have been filled in, return the actions taken to reach this state
        if 'x' not in state:
            return actions
        
        # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_nums:
                        new_state = state.copy()
                        new_state[i][j] = num
                        # Check if the new state is valid, ie if the numbers in each row and column are strictly increasing or decreasing
                        if all(np.all(np.diff(row) > 0) or np.all(np.diff(row) < 0) for row in new_state) and all(np.all(np.diff(col) > 0) or np.all(np.diff(col) < 0) for col in new_state.T):
                            # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal of the grid
                            new_cost = g + sum(int(x) for x in new_state[0] if x != 'x') + sum(int(x) for x in new_state[:, -1] if x != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                # The action taken to reach the new state is replacing the 'x' at coordinate (i, j) with the number num
                                heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, available_nums - {num}))
                    # Once we have generated all possible states from replacing the current 'x', we can break the loop as we only replace one 'x' at a time
                    break
            else:
                continue
            break
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
    # It's consistent because replacing an 'x' reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    return np.sum(state == 'x')

print(a_star())


import numpy as np
import heapq

def a_star():
    # Define the initial state of the grid
    initial_state = np.array([['49', 'x', 'x', 'x'],
                              ['x', '51', 'x', '84'],
                              ['47', 'x', 'x', '79'],
                              ['x', 'x', 'x', '77']])
    
    # Define the range of numbers that can be used to replace 'x'
    num_range = set(map(str, range(44, 90)))
    
    # Define the size of the grid
    grid_size = 4
    
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
    queue = [(0, 0, [], initial_state)]
    
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, replacements, state = heapq.heappop(queue)
        
        # If the current state has no 'x', return the replacements
        if 'x' not in state:
            return replacements
        
        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
        for i in range(grid_size):
            for j in range(grid_size):
                if state[i][j] == 'x':
                    for num in num_range - set(state.flatten()):
                        new_state = state.copy()
                        new_state[i][j] = num
                        # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                        if all(np.all(np.diff(list(map(int, row))) > 0) or np.all(np.diff(list(map(int, row))) < 0) for row in new_state) and all(np.all(np.diff(list(map(int, col))) > 0) or np.all(np.diff(list(map(int, col))) < 0) for col in new_state.T):
                            # The cost so far is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal from the top-left corner to the bottom-right corner
                            new_cost = g + sum(map(int, filter(lambda x: x != 'x', new_state[0]))) + sum(map(int, filter(lambda x: x != 'x', new_state[:, -1]))) + sum(map(int, filter(lambda x: x != 'x', np.diag(new_state))))
                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(i, j, int(num))], new_state))
                    break
            else:
                continue
            break
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the count of 'x' in the state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced at least once
    # It's consistent because replacing an 'x' reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    return np.count_nonzero(state == 'x')

print(a_star())

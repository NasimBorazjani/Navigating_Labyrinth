
import numpy as np
import heapq

def a_star():
    # Define the initial state of the grid
    initial_state = np.array([['x', 40, 'x', 65],
                              [34, 'x', 53, 'x'],
                              ['x', 'x', 'x', 63],
                              ['x', 56, 'x', 62]])

    # Define the range of numbers that can be used to replace 'x'
    num_range = set(range(25, 71))

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

        # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        else:
            # Find the next 'x' in the grid
            x_row, x_col = np.where(state == 'x')
            x_row, x_col = x_row[0], x_col[0]

            # Generate the set of available numbers by subtracting the set of numbers already in the grid from the set of all possible numbers
            available_nums = num_range - set(map(int, filter(lambda x: x != 'x', state.flatten())))

            # For each available number, check if replacing the 'x' with this number results in a valid state, ie the numbers in the row and column of the replaced 'x' are in strictly increasing or decreasing order
            for num in available_nums:
                new_state = state.copy()
                new_state[x_row, x_col] = num

                # Check if the numbers in the row and column of the replaced 'x' are in strictly increasing or decreasing order
                if all(new_state[x_row, i] < new_state[x_row, i + 1] or new_state[x_row, i] > new_state[x_row, i + 1] for i in range(grid_size - 1)) and all(new_state[i, x_col] < new_state[i + 1, x_col] or new_state[i, x_col] > new_state[i + 1, x_col] for i in range(grid_size - 1)):
                    # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal of the grid
                    new_cost = g + sum(map(int, filter(lambda x: x != 'x', new_state[0, :]))) + sum(map(int, filter(lambda x: x != 'x', new_state[:, -1]))) + sum(map(int, filter(lambda x: x != 'x', np.diag(new_state))))

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                        visited_costs[tuple(map(tuple, new_state))] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(x_row, x_col, num)], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the number of 'x's in the grid
    # The heuristic relaxes the constraints that the numbers in each row and column must be in strictly increasing or decreasing order and that each number can only appear once in the grid; ie It presumes we can replace any 'x' with any number
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal of the grid, which is always greater than or equal to 1, the decrease in the number of 'x's
    return np.count_nonzero(state == 'x')

print(a_star())

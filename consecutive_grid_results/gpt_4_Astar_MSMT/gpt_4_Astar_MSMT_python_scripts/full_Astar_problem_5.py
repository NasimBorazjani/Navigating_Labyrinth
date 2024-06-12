
import heapq
import numpy as np

def initialize():
    # Define the initial state of the grid, as a 2d tuple
    initial_state = (('66', 'x', '74'), ('x', '60', '62'), ('x', 'x', 'x'))
    # Define the range of numbers that can be used to replace 'x'
    numbers = set(range(44, 77))
    # Remove the numbers already present in the initial state from the set of available numbers
    for row in initial_state:
        for number in row:
            if number != 'x':
                numbers.remove(int(number))
    # Define the dimensions of the grid
    num_rows = 3
    num_cols = 3
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
    queue = [(0, 0, [], initial_state, numbers)]
    return initial_state, num_rows, num_cols, visited_costs, queue, numbers

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the set of available numbers)
    initial_state, num_rows, num_cols, visited_costs, queue, numbers = initialize()
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, replacements, state, available_numbers = heapq.heappop(queue)
        # Convert the state to a numpy array for easier manipulation
        state = np.array(state)
        # If the current state has no 'x's, it is a goal state
        if 'x' not in state:
            return replacements
        # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        for number in available_numbers:
            # Find the first 'x' in the grid
            x_row, x_col = np.where(state == 'x')
            x_row, x_col = x_row[0], x_col[0]
            # Generate the new state
            new_state = state.copy()
            new_state[x_row, x_col] = str(number)
            # Check if the new state is valid, ie the numbers in each row and column are consecutive
            if all(np.diff(sorted(row)) in [1, -1] for row in new_state) and all(np.diff(sorted(col)) in [1, -1] for col in new_state.T):
                # Convert the new state back to a tuple for hashing
                new_state = tuple(map(tuple, new_state))
                # The cost so far is the sum of the numbers in the top row, right column, and main diagonal
                new_cost = g + sum(int(number) for number in new_state[0]) + sum(int(number) for number in new_state[:, -1]) + sum(int(new_state[i][i]) for i in range(num_rows))
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The replacement made to get to the new state must be added to the list of replacements
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(x_row, x_col, number)], new_state, available_numbers - {number}))
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum available number is always less than or equal to the actual number used to replace 'x'
    # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
    return sum(min(numbers) for _ in np.where(state == 'x')[0])

print(a_star())

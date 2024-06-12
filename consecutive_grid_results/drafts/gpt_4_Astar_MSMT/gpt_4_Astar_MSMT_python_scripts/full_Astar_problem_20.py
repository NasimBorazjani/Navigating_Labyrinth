
import heapq
import numpy as np

def initialize():
    # Define the initial state of the grid, as a 2d tuple
    initial_state = (('80', 'x', 'x'), ('56', 'x', '64'), ('51', 'x', '76'))
    # Define the range of numbers
    num_range = list(range(48, 91))
    # Define the size of the grid
    num_rows = 3
    num_cols = 3
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]
    return initial_state, num_range, num_rows, num_cols, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of numbers, and the size of the grid)
    initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # We can check if the current state is the goal state by checking if there are no 'x's left in the state
        if 'x' not in np.array(state).flatten():
            return actions
        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    # Get the set of numbers already in the grid
                    current_nums = set(np.array(state).flatten())
                    # Get the set of available numbers
                    available_nums = set(num_range) - current_nums
                    for num in available_nums:
                        # Generate the new state
                        new_state = [list(row[:]) for row in state]
                        new_state[i][j] = str(num)
                        new_state = tuple(tuple(row) for row in new_state)
                        # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                        if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                            # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal
                            new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                    break
            else:
                continue
            break
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum available number is always less than or equal to the actual number that will replace the 'x'
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
    return sum(min(set(num_range) - set(np.array(state).flatten())) for _ in np.array(state).flatten() if _ == 'x')

print(a_star())

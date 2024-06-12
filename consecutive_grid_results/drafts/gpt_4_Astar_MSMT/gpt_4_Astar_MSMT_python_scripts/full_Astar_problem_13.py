
import heapq
import numpy as np

def initialize():
    # Define the initial state of the grid, as a 2d tuple
    initial_state = (('29', '45', 'x'), ('x', 'x', 'x'), ('x', '43', '34'))
    # Define the range of numbers that can be used to replace 'x's
    num_range = set(range(21, 59))
    # Define the dimensions of the grid
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
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of numbers that can be used to replace 'x's, and the dimensions of the grid)
    initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state has no 'x's, ie all the 'x's have been replaced with numbers, return the actions taken to reach this state
        if 'x' not in np.array(state).flatten():
            return actions
        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers in the range
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in num_range:
                        new_state = [list(row[:]) for row in state]
                        new_state[i][j] = str(num)
                        new_state = tuple(tuple(row) for row in new_state)
                        # Check if the new state is valid, ie the numbers in each row and column are in strictly increasing or decreasing order
                        if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                            # The cost so far is the sum of the numbers in the top row, right column, and main diagonal of the grid, as our objective is to minimize this sum
                            new_cost = sum(int(num) for num in new_state[0]) + sum(int(num) for num in zip(*new_state)[-1]) + sum(int(new_state[i][i]) for i in range(num_rows))
                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                            break
                    break
            else:
                continue
            break
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that can be used to replace the 'x's
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum remaining numbers are always less than or equal to the actual numbers that will replace the 'x's
    # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum remaining number
    return sum(sorted(set(range(21, 59)) - set(int(num) for num in np.array(state).flatten() if num != 'x'))[:np.array(state).flatten().tolist().count('x')])

print(a_star())

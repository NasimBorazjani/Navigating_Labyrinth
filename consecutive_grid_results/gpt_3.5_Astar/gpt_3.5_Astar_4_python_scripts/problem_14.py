
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    initial_state = np.array([[41, 'x', 21], ['x', 'x', 'x'], [12, 'x', 42]])
    num_rows = 3
    num_cols = 3
    num_range = set(range(11, 50))

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state, num_range))

    while queue:
        _, g, actions, state, num_range = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in num_range:
                        # Check if replacing the 'x' with the number maintains the consecutive order in each row and column
                        if (check_row(state, row, num) and check_col(state, col, num)):
                            new_state = state.copy()
                            new_state[row][col] = num
                            new_num_range = num_range.copy()
                            new_num_range.remove(num)
                            new_cost = g + num

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heappush(queue, (new_cost + heuristic(new_state, new_num_range), new_cost, actions + [(row, col, num)], new_state, new_num_range))
    return None


def check_row(state, row, num):
    # Check if the number can be placed in the row while maintaining the consecutive order
    for i in range(len(state[row])):
        if state[row][i] != 'x' and not (state[row][i] < num < state[row][i] + 2) and not (state[row][i] > num > state[row][i] - 2):
            return False
    return True


def check_col(state, col, num):
    # Check if the number can be placed in the column while maintaining the consecutive order
    for i in range(len(state)):
        if state[i][col] != 'x' and not (state[i][col] < num < state[i][col] + 2) and not (state[i][col] > num > state[i][col] - 2):
            return False
    return True


def heuristic(state, num_range):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the 'x's in the grid
    # The heuristic relaxes the constraint that the numbers in the grid must be consecutive, as it presumes we can replace the 'x's with the minimum possible values
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a higher value, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can replace the 'x' is the next available number in the range
    h = 0
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 'x':
                h += min(num_range)
    return h


print(a_star())

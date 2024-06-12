
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid, encoding the numbers as integers and the 'x's as None
    initial_state = np.array([[38, None, 50, None],
                              [None, None, 64, 67],
                              [54, None, 71, 79],
                              [None, 59, 89, 90]])

    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    num_range = range(36, 92)

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to a numpy array
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if None not in state:
            return actions

        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] is None:
                    for num in num_range:
                        # Check if the new state would be valid, ie if the consecutive order in each row and column is maintained
                        if (check_row(state, row, num) and check_col(state, col, num)):
                            new_state = state.copy()
                            new_state[row][col] = num
                            new_cost = g + num

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, num_range), new_cost, actions + [(row, col, num)], new_state))

    return None


def check_row(state, row, num):
    # Check if the consecutive order is maintained in the row after adding the new number
    row_values = [val for val in state[row] if val is not None]
    row_values.append(num)
    return all(row_values[i] < row_values[i+1] for i in range(len(row_values)-1) if row_values[i] is not None and row_values[i+1] is not None) or all(row_values[i] > row_values[i+1] for i in range(len(row_values)-1) if row_values[i] is not None and row_values[i+1] is not None)


def check_col(state, col, num):
    # Check if the consecutive order is maintained in the column after adding the new number
    col_values = [val for val in state[:, col] if val is not None]
    col_values = np.append(col_values, num)
    return all(col_values[i] < col_values[i+1] for i in range(len(col_values)-1) if col_values[i] is not None and col_values[i+1] is not None) or all(col_values[i] > col_values[i+1] for i in range(len(col_values)-1) if col_values[i] is not None and col_values[i+1] is not None)


def heuristic(state, num_range):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can be added to the grid to minimize the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
    # The heuristic relaxes the constraint that the numbers in the grid must be unique, as it presumes we can add the minimum possible values to minimize the sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can be added to the grid is 36, which is exactly the decrease in the heuristic estimate
    h = 0
    for row in range(state.shape[0]):
        for col in range(state.shape[1]):
            if state[row][col] is None:
                h += min(num_range)
    return h


print(a_star())

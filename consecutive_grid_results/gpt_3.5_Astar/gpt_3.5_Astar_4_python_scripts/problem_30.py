
import heapq
import numpy as np


def a_star():
    # Define the initial grid state and the range of numbers that can replace 'x'
    initial_grid = np.array([['x', '57', 'x'], ['42', 'x', '72'], ['39', 'x', '73']])
    numbers_range = list(range(39, 88))

    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_grid))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid, set(numbers_range)))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state to a numpy array
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in available_numbers:
                        # Check if replacing 'x' with the number maintains the strictly increasing or decreasing order in each row and column
                        if (row == 0 or (state[row - 1][col] == 'x' or int(state[row - 1][col]) < num)) and \
                                (row == num_rows - 1 or (state[row + 1][col] == 'x' or int(state[row + 1][col]) > num)) and \
                                (col == 0 or (state[row][col - 1] == 'x' or int(state[row][col - 1]) < num)) and \
                                (col == num_cols - 1 or (state[row][col + 1] == 'x' or int(state[row][col + 1]) > num)):
                            # Generate the new state
                            new_state = state.copy()
                            new_state[row][col] = str(num)
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)
                            # The cost so far is the number of actions taken, as the task is to minimize the sum of the numbers in the topmost row, rightmost column, and diagonal
                            new_cost = g + num

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state, new_available_numbers))
    return None


def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, as it presumes the minimum possible values will be used to replace the 'x's
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a larger number is used to replace an 'x', or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can replace an 'x' is used in the heuristic
    h = 0
    for row in range(state.shape[0]):
        for col in range(state.shape[1]):
            if state[row][col] == 'x':
                h += min(numbers_range)
    return h


print(a_star())


import heapq
import numpy as np


def a_star():
    # Define the initial grid state and the goal state
    initial_grid = np.array([[80, 'x', 'x'], [56, 'x', 64], [51, 'x', 76]])
    goal_grid = np.array([[80, 89, 91], [56, 84, 64], [51, 48, 76]])

    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    num_range = range(48, 92)

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_grid))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_grid)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state into a numpy array
        state = np.array(state)

        # If the current state is the goal state, return the actions taken
        if np.array_equal(state, goal_grid):
            return actions

        # Generate all possible actions from the current state
        if 'x' in state:
            # Find the indices of the 'x' elements in the grid
            x_indices = np.argwhere(state == 'x')

            for x_index in x_indices:
                row, col = x_index

                # Generate the new states by replacing 'x' with each available number
                for num in num_range:
                    if num not in state:
                        new_state = state.copy()
                        new_state[row, col] = num
                        new_state_tuple = tuple(map(tuple, new_state))

                        # Calculate the cost of the new state
                        new_cost = g + num

                        if new_state_tuple not in visited_costs or new_cost < visited_costs[new_state_tuple]:
                            visited_costs[new_state_tuple] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_grid, num_range), new_cost, actions + [(row, col, num)], new_state))

    return None


def heuristic(state, goal, num_range):
    # An admissible and consistent heuristic is the sum of the remaining numbers in the range that are not present in the grid
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it never overestimates the cost to reach the goal, as each remaining number must be placed in the grid
    # It's consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the next available number in the range
    h = 0
    for num in num_range:
        if num not in state:
            h += num
    return h


print(a_star())


import heapq
import numpy as np


def a_star():
    # Define the initial grid state and the goal state
    initial_grid = np.array([[49, 'x', 'x'], [47, 'x', 54], ['x', 35, 'x']])
    goal_grid = np.array([[49, 51, 53], [47, 50, 54], [45, 35, 57]])

    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3
    num_range = range(9, 58)

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_grid))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_grid, set(num_range))]

    while queue:
        _, g, actions, state, available_nums = heapq.heappop(queue)

        # Unpack the state into a numpy array
        state = np.array(state)

        # If the current state matches the goal state, return the actions taken
        if np.array_equal(state, goal_grid):
            return actions

        # Generate all possible actions from the current state
        if 'x' in state:
            for row in range(num_rows):
                for col in range(num_cols):
                    if state[row][col] == 'x':
                        for num in available_nums:
                            new_state = state.copy()
                            new_state[row][col] = num
                            new_available_nums = available_nums.copy()
                            new_available_nums.remove(num)
                            new_cost = g + calculate_cost(new_state)

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_grid), new_cost, actions + [(row, col, num)], new_state, new_available_nums))

    return None


def heuristic(state, goal):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0])
    right_col_sum = np.sum(state[:, 2])
    diagonal_sum = np.trace(state)

    # An admissible and consistent heuristic is the sum of the differences between the corresponding elements of the current state and the goal state
    h = np.sum(np.abs(state - goal))

    return h + top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(state):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0])
    right_col_sum = np.sum(state[:, 2])
    diagonal_sum = np.trace(state)

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

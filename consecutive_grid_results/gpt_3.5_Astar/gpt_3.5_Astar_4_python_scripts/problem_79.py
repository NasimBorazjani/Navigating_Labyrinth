
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', '35', 'x', 'x'],
                     ['34', '36', '38', 'x'],
                     ['29', 'x', '43', 'x'],
                     ['x', 'x', '49', '53']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(23, 74))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, set(numbers)))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Find the indices of the next 'x' in the grid
        x_indices = np.argwhere(state == 'x')
        x_row, x_col = x_indices[0]

        # Generate all possible actions from the current state
        for num in available_numbers:
            # Create a copy of the current state to modify
            new_state = state.copy()
            new_state[x_row, x_col] = str(num)
            new_available_numbers = available_numbers.copy()
            new_available_numbers.remove(num)
            new_cost = g + calculate_cost(new_state)

            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                visited_costs[tuple(map(tuple, new_state))] = new_cost
                heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(x_row, x_col, num)], new_state, new_available_numbers))

    return None


def heuristic(state, available_numbers):
    # Calculate the heuristic value based on the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum([int(num) for num in state[0] if num != 'x'])
    right_col_sum = np.sum([int(num) for num in state[:, -1] if num != 'x'])
    diagonal_sum = np.sum([int(state[i, i]) for i in range(state.shape[0]) if state[i, i] != 'x'])

    # The heuristic value is the sum of the three sums calculated above
    return top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(state):
    # Calculate the cost based on the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum([int(num) for num in state[0] if num != 'x'])
    right_col_sum = np.sum([int(num) for num in state[:, -1] if num != 'x'])
    diagonal_sum = np.sum([int(state[i, i]) for i in range(state.shape[0]) if state[i, i] != 'x'])

    # The cost is the sum of the three sums calculated above
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

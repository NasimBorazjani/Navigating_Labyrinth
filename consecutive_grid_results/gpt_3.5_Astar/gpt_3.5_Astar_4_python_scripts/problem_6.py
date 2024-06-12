
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[41, 48, 'x'],
                      ['x', 'x', 63],
                      ['x', 'x', 67]])

    # Define the range of numbers that can replace 'x'
    available_numbers = set(range(41, 75))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, available_numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more 'x's in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(3):
            for j in range(3):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i][j] = num
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + calculate_cost(new_state)

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))

    return None


def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, 2][state[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])

    # Calculate the sum of the top row, rightmost column, and diagonal
    return top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(state):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, 2][state[:, 2] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])

    # Calculate the sum of the top row, rightmost column, and diagonal
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

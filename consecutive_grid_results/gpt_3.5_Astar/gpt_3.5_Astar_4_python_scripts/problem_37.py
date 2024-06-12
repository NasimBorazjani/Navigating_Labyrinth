
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[57, 'x', 86],
                     ['x', 75, 'x'],
                     ['x', 76, 90]])

    # Define the range of numbers that can replace 'x'
    numbers = set(range(48, 102))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

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
                        new_cost = g + calculate_cost(new_state)

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)
                            heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))

    return None


def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(state[0])
    right_col_sum = sum(state[:, 2])
    diagonal_sum = state[0][0] + state[1][1] + state[2][2]

    # Calculate the sum of the top row, rightmost column, and diagonal
    return top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(state):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(state[0])
    right_col_sum = sum(state[:, 2])
    diagonal_sum = state[0][0] + state[1][1] + state[2][2]

    # Calculate the total cost as the sum of the top row, rightmost column, and diagonal
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

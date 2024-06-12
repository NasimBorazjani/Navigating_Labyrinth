
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[20, 21, 33, 60],
                     ['x', 'x', 'x', 49],
                     ['x', 38, 'x', 'x'],
                     [36, 'x', 46, 'x']])

    # Define the range of numbers that can replace 'x'
    numbers = list(range(14, 65))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, set(numbers)))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more 'x's in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(4):
            for j in range(4):
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
    right_col_sum = sum(state[:, 3])
    diagonal_sum = sum([state[i][i] for i in range(4)])

    # Find the minimum sum possible by replacing the remaining 'x's with the smallest available numbers
    min_sum = top_row_sum + right_col_sum + diagonal_sum + len(available_numbers) * min(available_numbers)

    return min_sum


def calculate_cost(state):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(state[0])
    right_col_sum = sum(state[:, 3])
    diagonal_sum = sum([state[i][i] for i in range(4)])

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

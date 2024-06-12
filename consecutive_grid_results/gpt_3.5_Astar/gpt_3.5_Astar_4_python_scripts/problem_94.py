
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', '36', '71', '79'],
                     ['x', 'x', '69', 'x'],
                     ['x', '50', '63', '70'],
                     ['21', '53', 'x', '62']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(20, 81))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there is at least one 'x' in the grid, generate all possible actions
        if 'x' in state:
            for i in range(4):
                for j in range(4):
                    if state[i][j] == 'x':
                        for num in available_numbers:
                            new_state = state.copy()
                            new_state[i][j] = str(num)
                            new_numbers = available_numbers.copy()
                            new_numbers.remove(num)
                            new_cost = g + calculate_cost(new_state)

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heappush(queue, (new_cost + heuristic(new_state, new_numbers), new_cost, actions + [(i, j, num)], new_state, new_numbers))
        else:
            return actions

    return None


def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(state[0][j]) for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([int(state[i][3]) for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([int(state[i][i]) for i in range(4) if state[i][i] != 'x'])

    # Calculate the heuristic value as the sum of the three sums
    h = top_row_sum + right_col_sum + diagonal_sum

    return h


def calculate_cost(state):
    # Calculate the cost as the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(state[0][j]) for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([int(state[i][3]) for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([int(state[i][i]) for i in range(4) if state[i][i] != 'x'])

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

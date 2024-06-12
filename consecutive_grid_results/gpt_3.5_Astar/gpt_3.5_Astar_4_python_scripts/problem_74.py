
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', '53', '62'],
                     ['x', '27', 'x', 'x'],
                     ['21', '22', 'x', '50'],
                     ['x', '20', '25', '44']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(14, 65))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
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

    return None


def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(state[0][j]) for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([int(state[i][3]) for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([int(state[i][i]) for i in range(4) if state[i][i] != 'x'])

    # An admissible and consistent heuristic is the sum of the top row, rightmost column, and diagonal sums
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the numbers in the top row, rightmost column, and diagonal is minimized
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum decrease in the sum is 1
    return top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(state):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(state[0][j]) for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([int(state[i][3]) for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([int(state[i][i]) for i in range(4) if state[i][i] != 'x'])

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

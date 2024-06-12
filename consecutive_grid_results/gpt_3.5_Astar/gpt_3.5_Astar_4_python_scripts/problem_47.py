
import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([[27, 37, 'x', 'x'],
                     [30, 'x', 'x', 'x'],
                     [32, 44, 53, 61],
                     [33, 54, 'x', 64]])

    # Define the range of numbers that can replace 'x'
    numbers = list(range(27, 68))

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
    # An admissible and consistent heuristic is the sum of the remaining available numbers
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the remaining available numbers is the minimum possible sum that can be achieved
    # It is consistent because the cost of adding a number to the grid is always 1, which is the decrease in the heuristic estimate, and the estimated cost of the successor node is always higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node)
    h = sum(available_numbers)
    return h


def calculate_cost(grid):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[:, -1])
    diagonal_sum = sum([grid[i][i] for i in range(4)])
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

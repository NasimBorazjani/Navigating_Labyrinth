
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', 'x', '60'],
                      ['47', 'x', '62', '65'],
                      ['x', '58', '67', '68'],
                      ['54', 'x', '74', 'x']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(36, 77))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, set(numbers)))

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
    # This heuristic relaxes the constraint that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the remaining available numbers is always less than the actual sum of the numbers in the grid
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the smallest available number, which is exactly the decrease in the heuristic estimate
    h = sum(available_numbers)
    return h


def calculate_cost(grid):
    # Calculate the sum of the numbers in the topmost row
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])

    # Calculate the sum of the numbers in the rightmost column
    right_col_sum = sum([int(num) for num in grid[:, -1] if num != 'x'])

    # Calculate the sum of the numbers in the diagonal connecting the top-left corner to the bottom-right corner
    diagonal_sum = sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

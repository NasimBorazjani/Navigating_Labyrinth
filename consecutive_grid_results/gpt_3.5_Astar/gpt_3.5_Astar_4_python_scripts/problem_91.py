
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', '38', 'x'],
                     ['x', 'x', '33', 'x'],
                     ['16', 'x', '28', '47'],
                     ['14', 'x', 'x', '52']])

    # Define the range of numbers that can replace 'x'
    numbers = set(range(14, 70))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_grid = state.copy()
                        new_grid[i][j] = str(num)
                        new_state = tuple(map(tuple, new_grid))
                        new_numbers = available_numbers.copy()
                        new_numbers.remove(num)
                        new_cost = g + calculate_cost(new_grid)

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, new_numbers), new_cost, actions + [(i, j, num)], new_grid, new_numbers))

    return None


def heuristic(grid, available_numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the 'x's in the grid
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it underestimates the cost to reach the goal state, as the actual cost will be at least as high as the heuristic value
    # It is consistent because the cost of replacing an 'x' with a number is at least 1, which is the decrease in the heuristic value
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += min(available_numbers)
    return h


def calculate_cost(grid):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal from top-left to bottom-right
    top_row_sum = sum([int(grid[0][j]) for j in range(4) if grid[0][j] != 'x'])
    right_col_sum = sum([int(grid[i][3]) for i in range(4) if grid[i][3] != 'x'])
    diagonal_sum = sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

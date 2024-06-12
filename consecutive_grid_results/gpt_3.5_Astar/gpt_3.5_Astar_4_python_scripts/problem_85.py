
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[71, 'x', 57, 'x'],
                     [67, 68, 'x', 73],
                     [51, 'x', 72, 'x'],
                     [50, 'x', 75, 'x']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(39, 95))

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
                        new_grid[i][j] = num
                        new_numbers = available_numbers.copy()
                        new_numbers.remove(num)
                        new_state = tuple(map(tuple, new_grid))
                        new_cost = g + calculate_cost(new_grid)

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, new_numbers), new_cost, actions + [(i, j, num)], new_grid, new_numbers))

    return None


def heuristic(grid, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(4))
    diagonal_sum = sum(grid[i][i] for i in range(4))

    # An admissible and consistent heuristic is the sum of the top row, rightmost column, and diagonal
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the numbers in the top row, rightmost column, and diagonal will always be minimized
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum possible decrease in the sum is 1
    return top_row_sum + right_col_sum + diagonal_sum


def calculate_cost(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(4))
    diagonal_sum = sum(grid[i][i] for i in range(4))

    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

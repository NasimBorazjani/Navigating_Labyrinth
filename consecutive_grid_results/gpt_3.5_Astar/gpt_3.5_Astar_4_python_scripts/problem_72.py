
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[25, 'x', 'x', 57],
                     [39, 45, 56, 'x'],
                     [43, 'x', 58, 'x'],
                     [46, 'x', 65, 69]])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(21, 72))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
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
    # An admissible and consistent heuristic for this problem is the sum of the remaining available numbers
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because the sum of the remaining available numbers is the minimum possible sum that can be achieved by replacing the remaining 'x's
    # It is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the minimum possible sum that can be achieved by replacing the remaining 'x's is the sum of the remaining available numbers
    return sum(available_numbers)


def calculate_cost(grid):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal connecting the top-left corner to the bottom-right corner
    top_row_sum = sum(grid[0])
    right_col_sum = sum(row[-1] for row in grid)
    diagonal_sum = sum(grid[i][i] for i in range(4))
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

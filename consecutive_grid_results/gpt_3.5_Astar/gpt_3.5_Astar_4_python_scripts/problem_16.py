
import heapq
import numpy as np


def a_star():
    # Define the initial grid state and the range of numbers that can replace 'x'
    initial_grid = np.array([[37, 'x', 'x'], ['x', 'x', 'x'], [44, 'x', 61]])
    numbers_range = list(range(28, 67))

    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_grid))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_grid, set(numbers_range))]

    while queue:
        _, g, actions, state, available_numbers = heapq.heappop(queue)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_grid = np.copy(state)
                        new_grid[i][j] = num
                        new_state = tuple(map(tuple, new_grid))
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_grid, new_available_numbers))

    return None


def heuristic(grid):
    # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that each number only appears once in the grid
    # It presumes that the sum of the numbers in the topmost row, rightmost column, and diagonal should be minimized, thus providing a lower estimate on the cost to reach the goal state
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the sum of the numbers in the topmost row, rightmost column, and diagonal can only decrease by at most 1 when a number is added to the grid
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(num_rows))
    diagonal_sum = sum(grid[i][i] for i in range(num_rows))
    return top_row_sum + right_col_sum + diagonal_sum


print(a_star())

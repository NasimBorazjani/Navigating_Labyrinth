
import heapq
import numpy as np


def a_star():
    # Define the initial grid state as a numpy array
    initial_grid = np.array([[85, 73, 59, 'x'],
                              ['x', 'x', 66, 70],
                              ['x', 59, 'x', 'x'],
                              [40, 41, 79, 82]])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(31, 87))

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_grid))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid, numbers))

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
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_grid, numbers), new_cost, actions + [(i, j, num)], new_grid, new_numbers))

    return None


def heuristic(grid, numbers):
    # An admissible and consistent heuristic for this problem is the sum of the minimum possible values that can replace the 'x's in the grid
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, as well as the constraint on the sum of the topmost row, rightmost column, and diagonal
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can replace the 'x' is the next available number in the range
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += min(numbers)
    return h


print(a_star())


import heapq
import numpy as np


def a_star():
    # Define the initial state of the grid
    grid = np.array([[69, 70, 'x', 'x'],
                     [64, 66, 'x', 75],
                     [62, 64, 'x', 'x'],
                     [60, 'x', 48, 46]])

    # Define the range of numbers that can replace 'x' in the grid
    available_numbers = set(range(41, 87))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid, available_numbers))

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
                        # Check if the new grid maintains the strictly increasing or decreasing order in each row and column
                        if all(new_grid[row][col] < new_grid[row+1][col] for row in range(3) if new_grid[row] != 'x') or all(new_grid[row][col] > new_grid[row+1][col] for row in range(3) if new_grid[row] != 'x') and all(new_grid[row][col] < new_grid[row][col+1] for col in range(3) if new_grid[:, col] != 'x') or all(new_grid[row][col] > new_grid[row][col+1] for col in range(3) if new_grid[:, col] != 'x'):
                            # Calculate the new cost based on the sum of the numbers in the topmost row, rightmost column, and diagonal
                            new_cost = g + sum(new_grid[0]) + sum(new_grid[:, 3]) + sum([new_grid[i][i] for i in range(4)])
                            new_state = tuple(map(tuple, new_grid))
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)

                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heappush(queue, (new_cost + heuristic(new_grid, new_available_numbers), new_cost, actions + [(i, j, num)], new_grid, new_available_numbers))
    return None


def heuristic(grid, available_numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the numbers in the grid must be strictly increasing or decreasing, and that each number must be unique
    # It is admissible because it underestimates the cost to reach the goal state, as the minimum possible values are used
    # It is consistent because the estimated cost of the next node is always less than or equal to the cost of reaching the successor node plus the estimated cost to reach the goal
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += min(available_numbers)
    return h


print(a_star())

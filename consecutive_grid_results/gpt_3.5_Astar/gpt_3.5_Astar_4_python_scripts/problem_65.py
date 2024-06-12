
import heapq
import numpy as np

def a_star():
    # Define the initial state of the grid
    grid = np.array([[10, 26, 30, 46],
                      ['x', 33, 43, 'x'],
                      [21, 40, 'x', 'x'],
                      ['x', 'x', 'x', 52]])

    # Define the range of numbers that can replace 'x'
    numbers = set(range(9, 55))

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
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_grid, new_numbers))

    return None

def heuristic(grid):
    # Calculate the sum of the numbers in the topmost row
    top_row_sum = sum(grid[0])

    # Calculate the sum of the numbers in the rightmost column
    right_col_sum = sum(grid[i][3] for i in range(4))

    # Calculate the sum of the numbers in the diagonal connecting the top-left corner to the bottom-right corner
    diagonal_sum = sum(grid[i][i] for i in range(4))

    # The heuristic is the sum of the three sums calculated above
    return top_row_sum + right_col_sum + diagonal_sum

print(a_star())


import heapq
import numpy as np

def a_star():
    # Define the initial state of the grid
    grid = np.array([[62, 58, 'x', 'x'],
                      [56, 57, 'x', 'x'],
                      [50, 'x', 'x', 74],
                      [48, 'x', 'x', 78]])

    # Define the range of numbers that can replace 'x'
    numbers = list(range(30, 86))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, set(numbers)))

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
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_state = tuple(map(tuple, new_grid))
                        new_cost = g + calculate_cost(new_grid)

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, new_available_numbers), new_cost, actions + [(i, j, num)], new_grid, new_available_numbers))

    return None

def calculate_cost(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(row[-1] for row in grid)
    diagonal_sum = sum(grid[i][i] for i in range(4))
    return top_row_sum + right_col_sum + diagonal_sum

def heuristic(grid, available_numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it underestimates the cost to reach the goal state, as the actual cost will be at least as high as the heuristic estimate
    # It is consistent because the cost of moving from one state to another is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                h += min(available_numbers)
    return h

print(a_star())

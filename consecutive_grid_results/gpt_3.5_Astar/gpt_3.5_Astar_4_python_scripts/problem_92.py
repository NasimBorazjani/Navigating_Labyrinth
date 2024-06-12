
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', '28', '11', 'x'],
                      ['x', '27', 'x', 'x'],
                      ['15', 'x', 'x', '46'],
                      ['x', 'x', 'x', '50']])

    # Define the range of numbers that can be used to replace 'x'
    numbers = set(range(6, 62))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # If there are no more 'x's in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_grid = state.copy()
                        new_grid[i][j] = str(num)
                        new_numbers = available_numbers.copy()
                        new_numbers.remove(num)
                        new_state = tuple(map(tuple, new_grid))
                        new_cost = g + calculate_cost(new_grid)

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid), new_cost, actions + [(i, j, num)], new_grid, new_numbers))

    return None

def calculate_cost(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(grid[0][j]) for j in range(4)])
    right_col_sum = sum([int(grid[i][3]) for i in range(4)])
    diagonal_sum = sum([int(grid[i][i]) for i in range(4)])
    return top_row_sum + right_col_sum + diagonal_sum

def heuristic(grid):
    # An admissible and consistent heuristic is the sum of the differences between the numbers and the next number in the sequence in each row and column
    h = 0
    for i in range(4):
        row = [int(num) for num in grid[i] if num != 'x']
        col = [int(grid[j][i]) for j in range(4) if grid[j][i] != 'x']
        for j in range(3):
            if row[j] < row[j+1]:
                h += row[j+1] - row[j]
            if col[j] < col[j+1]:
                h += col[j+1] - col[j]
    return h

print(a_star())

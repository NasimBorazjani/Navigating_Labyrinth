
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', '73', '74', 'x'],
                     ['46', 'x', '63', '72'],
                     ['x', '47', 'x', 'x'],
                     ['41', '45', 'x', '54']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(35, 81))

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
        for i in range(state.shape[0]):
            for j in range(state.shape[1]):
                if state[i, j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i, j] = str(num)
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + calculate_cost(new_state)

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))

    return None

def calculate_cost(grid):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(num) for num in grid[0] if num != 'x'])
    right_col_sum = sum([int(num) for num in grid[:, -1] if num != 'x'])
    diagonal_sum = sum([int(grid[i, i]) for i in range(grid.shape[0]) if grid[i, i] != 'x'])
    return top_row_sum + right_col_sum + diagonal_sum

def heuristic(grid, available_numbers):
    # Calculate the sum of the remaining available numbers to be placed in the grid
    remaining_sum = sum(available_numbers)
    return remaining_sum

print(a_star())

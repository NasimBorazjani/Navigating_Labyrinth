
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', '63', 'x'],
                     ['x', '53', '57', '73'],
                     ['x', 'x', '56', 'x'],
                     ['42', 'x', 'x', '68']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = list(range(40, 81))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, set(numbers)))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Find the indices of the next 'x' in the grid
        x_indices = np.argwhere(state == 'x')
        x_row, x_col = x_indices[0]

        # Generate all possible actions from the current state
        for num in available_numbers:
            # Create a copy of the current state to modify
            new_state = np.copy(state)
            new_state[x_row, x_col] = str(num)

            # Check if the new state maintains the strictly increasing or decreasing order in each row and column
            valid = True
            for i in range(4):
                row = new_state[i]
                col = new_state[:, i]
                if not (is_strictly_increasing(row) or is_strictly_decreasing(row)) or not (is_strictly_increasing(col) or is_strictly_decreasing(col)):
                    valid = False
                    break

            if valid:
                # Update the set of available numbers after adding the new number to the grid
                new_available_numbers = available_numbers.copy()
                new_available_numbers.remove(num)

                # Generate the new state as a tuple for hashing
                new_state_tuple = tuple(map(tuple, new_state))

                # Calculate the cost of the new state based on the sum of the numbers in the topmost row, rightmost column, and diagonal
                new_cost = g + sum_top_row(new_state) + sum_right_column(new_state) + sum_diagonal(new_state)

                if new_state_tuple not in visited_costs or new_cost < visited_costs[new_state_tuple]:
                    visited_costs[new_state_tuple] = new_cost
                    heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(x_row, x_col, num)], new_state, new_available_numbers))

    return None

def is_strictly_increasing(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

def is_strictly_decreasing(arr):
    return all(arr[i] > arr[i+1] for i in range(len(arr)-1))

def sum_top_row(grid):
    return sum([int(num) for num in grid[0] if num != 'x'])

def sum_right_column(grid):
    return sum([int(num) for num in grid[:, -1] if num != 'x'])

def sum_diagonal(grid):
    return sum([int(grid[i][i]) for i in range(4) if grid[i][i] != 'x'])

def heuristic(state, available_numbers):
    # An admissible heuristic is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the numbers in the grid must be unique, as it assumes the minimum values will be used
    # The heuristic is consistent because the estimated cost of the next node is always less than or equal to the cost of reaching the successor node plus the estimated cost to reach the goal
    return sum(sorted(available_numbers)[:state[state == 'x'].size])

print(a_star())

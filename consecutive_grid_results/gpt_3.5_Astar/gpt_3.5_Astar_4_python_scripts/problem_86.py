
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([[81, 52, 'x', 'x'],
                      ['x', 50, 53, 'x'],
                      [42, 'x', 54, 74],
                      ['x', 'x', 56, 77]])

    # Define the range of numbers that can replace 'x'
    numbers = set(range(28, 84))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, numbers))

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
            new_state[x_row, x_col] = num

            # Check if the new state maintains the strictly increasing or decreasing order in each row and column
            valid = True
            for i in range(4):
                row = new_state[i]
                col = new_state[:, i]
                if 'x' not in row and not (all(row[j] < row[j+1] for j in range(3)) or all(row[j] > row[j+1] for j in range(3)):
                    valid = False
                    break
                if 'x' not in col and not (all(col[j] < col[j+1] for j in range(3)) or all(col[j] > col[j+1] for j in range(3)):
                    valid = False
                    break

            if valid:
                # Update the set of available numbers after adding the new number to the grid
                new_available_numbers = available_numbers - {num}
                new_cost = g + num

                if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                    visited_costs[tuple(map(tuple, new_state))] = new_cost
                    heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(x_row, x_col, num)], new_state, new_available_numbers))

    return None

def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0])
    right_col_sum = np.sum(state[:, 3])
    diagonal_sum = np.sum([state[i][i] for i in range(4)])

    # Find the minimum sum among the three sums
    min_sum = min(top_row_sum, right_col_sum, diagonal_sum)

    # The heuristic is the difference between the minimum sum and the sum of the top row, rightmost column, and diagonal
    h = top_row_sum + right_col_sum + diagonal_sum - min_sum

    return h

print(a_star())

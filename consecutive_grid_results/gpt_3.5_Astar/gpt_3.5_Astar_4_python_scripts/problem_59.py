
import heapq
import numpy as np

def a_star():
    # Define the initial grid state
    grid = np.array([['x', 'x', 'x', 'x'],
                     ['37', 'x', '49', 'x'],
                     ['x', '44', 'x', 'x'],
                     ['42', 'x', '51', '61']])

    # Define the range of numbers that can replace 'x'
    numbers = list(range(24, 65))

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
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i][j] = str(num)
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + num

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))

    return None

def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum([int(state[0][j]) for j in range(4) if state[0][j] != 'x'])
    right_col_sum = sum([int(state[i][3]) for i in range(4) if state[i][3] != 'x'])
    diagonal_sum = sum([int(state[i][i]) for i in range(4) if state[i][i] != 'x'])

    # An admissible and consistent heuristic is the sum of the sums calculated above
    h = top_row_sum + right_col_sum + diagonal_sum

    return h

print(a_star())

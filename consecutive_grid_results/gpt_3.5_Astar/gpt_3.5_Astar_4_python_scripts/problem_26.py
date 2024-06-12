
import heapq
import numpy as np

def a_star():
    # Define the initial state of the grid
    grid = np.array([[29, 'x', 'x'], ['x', 'x', 'x'], [36, 55, 'x']])
    num_rows, num_cols = grid.shape
    available_numbers = set(range(17, 61))

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    queue = []
    heappush(queue, (0, 0, [], grid, available_numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        new_state = state.copy()
                        new_state[i][j] = num
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        new_cost = g + calculate_cost(new_state)

                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))

    return None

def heuristic(state, available_numbers):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, -1][state[:, -1] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])

    # Calculate the sum of the numbers in the diagonal connecting the top-left corner to the bottom-right corner
    diag_sum = np.trace(state)
    
    # The heuristic is the sum of the top row, right column, and diagonal sums
    h = top_row_sum + right_col_sum + diag_sum

    return h

def calculate_cost(state):
    # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
    top_row_sum = np.sum(state[0][state[0] != 'x'])
    right_col_sum = np.sum(state[:, -1][state[:, -1] != 'x'])
    diagonal_sum = np.sum(np.diag(state)[np.diag(state) != 'x'])

    # Calculate the sum of the numbers in the diagonal connecting the top-left corner to the bottom-right corner
    diag_sum = np.trace(state)
    
    # The cost is the sum of the top row, right column, and diagonal sums
    cost = top_row_sum + right_col_sum + diag_sum

    return cost

print(a_star())

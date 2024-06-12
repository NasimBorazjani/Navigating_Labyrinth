
import heapq
import numpy as np


def a_star():
    # Define the initial grid state as a numpy array
    initial_state = np.array([[33, 37, 'x', 58],
                               [44, 51, 'x', 63],
                               ['x', 52, 62, 64],
                               ['x', 'x', 65, 'x']])

    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(33, 79))

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state, numbers))

    while queue:
        _, g, actions, state, available_numbers = heappop(queue)

        # Unpack the state to a numpy array
        state = np.array(state)

        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in state:
            return actions

        # Generate all possible actions from the current state
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in available_numbers:
                        # Create a copy of the current state to modify
                        new_state = state.copy()
                        new_state[i][j] = num
                        # Filter out the 'x's to avoid errors when comparing elements
                        row = new_state[i][new_state[i] != 'x']
                        col = new_state[:, j][new_state[:, j] != 'x']
                        # Calculate the sum of the numbers in the topmost row, rightmost column, and diagonal
                        new_cost = g + sum(new_state[0]) + sum(new_state[:, 3]) + sum(np.diag(new_state))

                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            # Update the set of available numbers after adding a new number to the grid
                            new_available_numbers = available_numbers.copy()
                            new_available_numbers.remove(num)
                            heappush(queue, (new_cost + heuristic(new_state, numbers), g + 1, actions + [(i, j, num)], new_state, new_available_numbers))
    return None


def heuristic(state, numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the 'x's in the grid
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, as well as the constraint on the sum of the numbers in the topmost row, rightmost column, and diagonal
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can replace the 'x' is added to the heuristic
    h = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] == 'x':
                h += min(numbers)
    return h


print(a_star())

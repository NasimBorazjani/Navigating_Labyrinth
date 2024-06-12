
import heapq
import numpy as np


def a_star():
    # Define the initial grid state as a numpy array
    initial_state = np.array([[29, 45, 'x'], ['x', 'x', 'x'], ['x', 43, 34]])
    # Define the range of numbers that can replace 'x' in the grid
    numbers = set(range(21, 60))
    
    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3

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

        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in available_numbers:
                        # Create a copy of the current state to modify
                        new_state = state.copy()
                        new_state[row][col] = num
                        # Update the set of available numbers after replacing the 'x' with a number
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        # The cost so far is the number of actions taken, as the task is to minimize the sum of the numbers in the topmost row, rightmost column, and diagonal
                        new_cost = g + num

                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                        if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, numbers), new_cost, actions + [(row, col, num)], new_state, new_available_numbers))
    return None


def heuristic(state, numbers):
    # An admissible and consistent heuristic for this problem is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the minimum possible values that can replace the remaining 'x's is always less than or equal to the actual sum of the numbers in the topmost row, rightmost column, and diagonal
    # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger value, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the minimum possible value that can replace the remaining 'x's is always less than or equal to the actual value that can replace the 'x'
    h = 0
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 'x':
                h += min(numbers)
    return h


print(a_star())

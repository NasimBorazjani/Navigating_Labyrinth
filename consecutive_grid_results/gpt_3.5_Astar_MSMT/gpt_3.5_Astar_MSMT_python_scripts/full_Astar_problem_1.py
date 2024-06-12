
import heapq
import numpy as np


def initialize():
    # Define the initial state of the grid as a numpy array
    grid = np.array([[16, 'x', 41], ['x', 30, 'x'], ['x', 29, 30]])
    # Define the range of numbers that can replace 'x' in the grid
    numbers_range = set(range(13, 46))

    # Encoding other variables given in the problem statement
    num_rows = 3
    num_cols = 3

    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], grid, numbers_range)]

    return grid, num_rows, num_cols, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem
    grid, num_rows, num_cols, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state, numbers_range = heapq.heappop(queue)

        # Unpack the state from the numpy array
        state = np.array(state)

        # If the state has at least 1 remaining unknown number, ie 'x'
        if 'x' in state:
            # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of available unique integers
            for row in range(num_rows):
                for col in range(num_cols):
                    if state[row][col] == 'x':
                        for num in numbers_range:
                            new_state = state.copy()
                            new_state[row][col] = num
                            new_numbers_range = numbers_range.copy()
                            new_numbers_range.remove(num)
                            new_cost = g + num

                            if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                                visited_costs[tuple(map(tuple, new_state))] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, new_numbers_range), new_cost, actions + [(row, col, num)], new_state, new_numbers_range))
        else:
            return actions

    return None


def heuristic(state, numbers_range):
    # An admissible and consistent heuristic is the sum of the numbers in the topmost row, rightmost column, and diagonal connecting the top-left corner to the bottom-right corner
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, as well as the constraint that each number must be unique
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the numbers in the topmost row, rightmost column, and diagonal is minimized
    # It is consistent because the estimated cost of the next node is higher if a number is replaced, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the sum of the numbers in the topmost row, rightmost column, and diagonal is minimized
    h = 0
    # Calculate the sum of the topmost row
    h += sum(state[0])
    # Calculate the sum of the rightmost column
    h += sum(state[:, -1])
    # Calculate the sum of the diagonal connecting the top-left corner to the bottom-right corner
    h += sum([state[i][i] for i in range(len(state))])
    return h


print(a_star())

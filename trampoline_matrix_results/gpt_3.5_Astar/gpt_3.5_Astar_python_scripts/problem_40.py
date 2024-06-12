
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((9, 9))
    destination = (2, 0)
    num_rows = 11
    num_cols = 11
    grid = [[1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == destination:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0] + i
                new_col = state[1] + j
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the cost of moving to the new position
                    new_cost = g + math.sqrt(i**2 + j**2)
                    new_state = (new_row, new_col)
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Add the new action to the queue
                        heapq.heappush(queue, (new_cost + heuristic(new_state, destination), new_cost, actions + [new_state], new_state))

    return None


def heuristic(state, destination):
    # A heuristic function that calculates the Euclidean distance between the current state and the destination
    # This heuristic is admissible as it never overestimates the cost to reach the destination
    # It is consistent because the cost of moving from one state to a neighboring state is always 1, which is less than or equal to the Euclidean distance between the states
    return math.sqrt((state[0] - destination[0])**2 + (state[1] - destination[1])**2)


print(a_star())

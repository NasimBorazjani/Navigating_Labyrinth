
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((9, 9),)
    destination = (4, 1)
    num_rows = 10
    num_cols = 10
    grid = [[1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state[0] == destination:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = state[0][0] + i
                new_col = state[0][1] + j
                # Check if the new position is within the bounds of the grid and the trampoline is functional
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 0:
                    # Calculate the number of diagonal jumps made so far
                    diagonal_jumps = sum(1 for action in actions if abs(action[0] - state[0][0]) == 1 and abs(action[1] - state[0][1]) == 1)
                    # Ensure that exactly 3 diagonal jumps are made
                    if abs(new_row - state[0][0]) == 1 and abs(new_col - state[0][1]) == 1 and diagonal_jumps < 3:
                        new_state = ((new_row, new_col),)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state, destination)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
    return None


def heuristic(state, destination):
    # A consistent and admissible heuristic is the Manhattan distance between the current position and the destination
    # The heuristic is admissible because the shortest path between two points in a grid is the Manhattan distance, which is always less than or equal to the actual cost
    # The heuristic is consistent because the cost of moving from one position to another is always 1, which is equal to the decrease in the heuristic estimate
    h = abs(state[0][0] - destination[0]) + abs(state[0][1] - destination[1])
    return h


print(a_star())


import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 1, 0, 1, 0, 1, 1, 1, 1),
                     (0, 0, 1, 1, 0, 0, 0, 0, 1),
                     (0, 0, 0, 1, 1, 1, 0, 0, 1),
                     (0, 0, 0, 0, 0, 0, 0, 1, 0),
                     (0, 0, 0, 0, 0, 1, 1, 1, 1),
                     (0, 0, 1, 1, 1, 1, 0, 1, 1),
                     (0, 0, 0, 1, 1, 1, 1, 1, 0),
                     (1, 0, 1, 1, 1, 1, 1, 0, 1),
                     (0, 1, 1, 1, 1, 1, 0, 1, 0))
    num_rows = 9
    num_cols = 9
    start = (8, 0)
    goal = (2, 7)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 3

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, position = heapq.heappop(queue)

        # If Alex reaches the goal position with exactly 3 diagonal jumps, return the actions taken
        if position == goal and len([action for action in actions if action in moves]) == num_diagonal_jumps:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_position = (position[0] + move[0], position[1] + move[1])
            # Check if the new position is within the bounds of the grid and is not a broken trampoline
            if 0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and initial_state[new_position[0]][new_position[1]] == 0:
                # Generate the new state
                new_cost = g + 1
                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_position, goal), new_cost, actions + [new_position], new_position))

    return None


def heuristic(position, goal):
    # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
    # The Manhattan distance is the sum of the absolute differences of the x and y coordinates
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


print(a_star())

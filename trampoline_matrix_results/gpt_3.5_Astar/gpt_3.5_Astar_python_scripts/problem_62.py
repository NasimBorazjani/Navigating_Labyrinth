
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0),
                      (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1),
                      (1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                      (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1),
                      (1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1),
                      (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1),
                      (1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0),
                      (1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1),
                      (0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1),
                      (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0),
                      (1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0),
                      (1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1),
                      (0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0))
    num_rows = 13
    num_cols = 13
    start = (11, 8)
    goal = (1, 0)
    # Define the possible moves Alex can make
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 4

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        # If Alex reaches the goal position, return the path
        if current == goal and len(path) == num_diagonal_jumps + 1:
            return path

        # Generate all possible actions from the current position, which includes moving to any of the adjacent trampolines
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            # Check if the new position is within the grid and not broken
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                new_path = path + [new_pos]
                new_cost = g + 1

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, goal)
                    heapq.heappush(queue, (new_cost + h, new_cost, new_path, new_pos))

    return None


def heuristic(current, goal):
    # A heuristic function that calculates the Manhattan distance between the current position and the goal position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the heuristic estimate
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


print(a_star())

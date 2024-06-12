
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                     (0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0),
                     (0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                     (0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1),
                     (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1),
                     (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
                     (0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1),
                     (1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0),
                     (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1),
                     (0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1),
                     (0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
                     (1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0),
                     (1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1),
                     (1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0))
    num_rows = 15
    num_cols = 15
    start = (11, 1)
    goal = (2, 12)
    # Define the possible moves Alex can make
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        # If Alex reaches the goal position, return the path
        if current == goal:
            return path

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            # Check if the new position is within the bounds of the grid and the trampoline is functional
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                new_cost = g + 1
                # Calculate the heuristic cost using the Euclidean distance to the goal position
                h = math.sqrt((new_pos[0] - goal[0]) ** 2 + (new_pos[1] - goal[1]) ** 2)
                # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [new_pos], new_pos))

    return None


print(a_star())

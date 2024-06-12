
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 1, 1, 1, 0, 0, 0, 1, 0),
                     (0, 1, 1, 0, 1, 0, 1, 0, 0),
                     (1, 0, 1, 1, 1, 1, 0, 0, 1),
                     (0, 0, 1, 0, 1, 1, 1, 0, 1),
                     (1, 0, 1, 1, 0, 1, 1, 0, 1),
                     (1, 1, 1, 1, 1, 0, 0, 0, 0),
                     (0, 0, 1, 1, 1, 0, 0, 0, 1),
                     (1, 1, 1, 0, 0, 0, 0, 1, 1),
                     (1, 1, 1, 0, 0, 0, 0, 1, 1))
    num_rows = 9
    num_cols = 9
    start = (0, 8)
    goal = (8, 3)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 3

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
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            # Check if the new position is within the bounds of the grid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                new_pos = (new_row, new_col)
                # Check if the new position is not a broken trampoline and is not already visited
                if initial_state[new_row][new_col] == 0 and new_pos not in path:
                    new_path = path + [new_pos]
                    new_cost = g + 1

                    # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of unvisited positions
                    if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                        visited_costs[new_pos] = new_cost
                        # Calculate the heuristic cost based on the Euclidean distance to the goal position
                        h = math.sqrt((new_row - goal[0]) ** 2 + (new_col - goal[1]) ** 2)
                        heapq.heappush(queue, (new_cost + h, new_cost, new_path, new_pos))

    return None


print(a_star())

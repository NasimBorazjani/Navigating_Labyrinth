
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 1, 1, 0, 0, 0, 0, 1, 1),
                     (0, 1, 1, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 1, 0, 1, 0, 0, 1),
                     (0, 0, 0, 1, 0, 0, 0, 0, 0),
                     (0, 0, 1, 1, 0, 1, 1, 0, 1),
                     (1, 1, 1, 1, 1, 0, 0, 0, 0),
                     (0, 1, 1, 1, 0, 1, 1, 0, 0),
                     (1, 1, 1, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 0, 0, 0, 1, 0, 0))
    num_rows = 9
    num_cols = 9
    start = (8, 7)
    goal = (0, 3)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 3

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        # If Alex reaches the goal position and has made exactly 3 diagonal jumps, return the path
        if current == goal and len([pos for pos in path if pos[0] != pos[1]]) == num_diagonal_jumps:
            return path

        # Generate all possible moves from the current position
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            # Check if the new position is within the grid and not a broken trampoline
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                new_path = path + [new_pos]
                new_cost = g + 1

                # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    # Calculate the heuristic cost based on the Euclidean distance to the goal
                    h = math.sqrt((new_pos[0] - goal[0]) ** 2 + (new_pos[1] - goal[1]) ** 2)
                    heapq.heappush(queue, (new_cost + h, new_cost, new_path, new_pos))

    return None


print(a_star())

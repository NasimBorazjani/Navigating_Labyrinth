
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((5, 15, 15, 5, 6, 19, math.inf, 9, 2, math.inf, 16, math.inf, 15),
                     (16, math.inf, math.inf, 7, 5, math.inf, math.inf, math.inf, 5, 2, 19, math.inf, 3),
                     (math.inf, 11, 2, 19, 17, 5, 11, 6, 3, 18, 15, 16, math.inf),
                     (2, math.inf, 12, math.inf, 20, 11, 7, 19, 2, math.inf, 4, 14, math.inf),
                     (3, math.inf, 19, math.inf, 11, 19, math.inf, 14, math.inf, 12, math.inf, 18, 7),
                     (6, math.inf, 5, 8, 3, 12, 12, 11, 5, 14, math.inf, 6, math.inf),
                     (math.inf, math.inf, 13, 2, math.inf, 20, math.inf, math.inf, math.inf, 18, 18, math.inf, 3),
                     (math.inf, math.inf, 13, 1, 10, 18, math.inf, math.inf, math.inf, math.inf, 10, math.inf, 15),
                     (10, math.inf, 9, 2, 17, 19, 16, 8, math.inf, 18, 10, math.inf, 13),
                     (math.inf, math.inf, 2, 8, 2, 7, math.inf, 17, math.inf, 1, math.inf, 9, math.inf),
                     (math.inf, 13, math.inf, 19, 15, 3, 15, 13, 1, 12, 4, 7, math.inf),
                     (14, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 16, math.inf, 15, math.inf, math.inf, math.inf),
                     (3, 15, math.inf, 6, math.inf, 9, math.inf, math.inf, 9, 1, 6, math.inf, 5))

    num_rows = 13
    num_cols = 13
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 12)}
    start = (8, 2)
    end = (2, 9)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(path[districts[d][0]:districts[d][1] + 1])) > 1 for d in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != math.inf:
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_row, new_col, end), new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())


import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((math.inf, math.inf, math.inf, 3, math.inf, math.inf, 16, math.inf, 2, 16, 3),
                     (8, math.inf, 8, 5, math.inf, math.inf, 10, math.inf, 19, 4, math.inf),
                     (math.inf, math.inf, 18, 1, 16, math.inf, 9, 15, math.inf, math.inf, 11),
                     (math.inf, math.inf, 17, 16, 4, 19, 2, math.inf, 1, 11, math.inf),
                     (9, math.inf, 5, 16, 18, math.inf, math.inf, 7, math.inf, 18, 6),
                     (math.inf, 15, 7, math.inf, math.inf, math.inf, 19, 8, 9, 17, math.inf),
                     (math.inf, 15, 19, math.inf, math.inf, math.inf, 6, 2, 6, math.inf, 5),
                     (math.inf, 12, 11, 3, 11, 4, math.inf, math.inf, math.inf, 3, math.inf),
                     (18, 12, 4, math.inf, 3, 10, math.inf, 3, math.inf, 7, 14),
                     (15, 11, 12, math.inf, 13, 2, math.inf, math.inf, 5, 14, math.inf),
                     (math.inf, math.inf, 15, math.inf, 16, 4, 10, 13, math.inf, math.inf, 4))

    num_rows = 11
    num_cols = 11
    districts = {1: (0, 3), 2: (4, 7), 3: (8, 10)}
    start = (3, 6)
    end = (8, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)] for workshop in path):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != math.inf:
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_row, new_col, end), new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(row, col, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(row - end[0]) + abs(col - end[1])


print(a_star())

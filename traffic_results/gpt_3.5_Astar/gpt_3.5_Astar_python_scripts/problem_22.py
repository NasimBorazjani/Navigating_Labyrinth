
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((2, 2, 3, math.inf, 2, 10, math.inf, 8, 6, math.inf),
                      (6, 11, math.inf, math.inf, math.inf, math.inf, math.inf, 16, math.inf, 7),
                      (17, 17, 7, 12, 13, 15, 5, 6, 10, 13),
                      (1, 15, 13, 3, math.inf, math.inf, math.inf, 14, math.inf, 9),
                      (14, math.inf, math.inf, 6, 15, 2, 12, 18, math.inf, 18),
                      (11, 19, 1, 19, 10, 8, math.inf, 14, math.inf, math.inf),
                      (11, math.inf, math.inf, math.inf, 3, math.inf, math.inf, 7, math.inf, 2),
                      (16, 12, math.inf, math.inf, math.inf, 5, math.inf, math.inf, 10, math.inf),
                      (math.inf, 11, math.inf, 2, 12, math.inf, 8, math.inf, 8, math.inf),
                      (math.inf, math.inf, 16, math.inf, math.inf, math.inf, 16, math.inf, 16, 12))
    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 1), (1, 0)], 2: [(2, 0), (4, 0)], 3: [(5, 0), (9, 0)]}
    start = (1, 0)
    end = (5, 7)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(any(cell in district for cell in path) for district in districts.values()):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != math.inf:
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                if new_row == end[0] and new_col == end[1] and all(any(cell in district for cell in new_path) for district in districts.values()):
                    return new_path
                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    heapq.heappush(queue, (g + initial_state[new_row][new_col], new_cost, new_path, (new_row, new_col)))
    return None


print(a_star())

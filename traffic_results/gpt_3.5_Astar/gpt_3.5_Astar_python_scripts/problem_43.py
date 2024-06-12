
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[math.inf, 10, 2, math.inf, math.inf, math.inf, 3, math.inf, 4, math.inf, 14],
                [math.inf, math.inf, 17, 16, 8, math.inf, math.inf, math.inf, math.inf, 1, math.inf],
                [18, 18, 16, 16, 15, math.inf, math.inf, 17, 12, 16, 15],
                [math.inf, 4, math.inf, math.inf, 18, 9, math.inf, 15, math.inf, 1, 9],
                [3, 2, 7, math.inf, math.inf, 17, 2, 14, math.inf, 4, 2],
                [16, 17, 6, 4, 9, 2, 5, 7, math.inf, math.inf, 7],
                [math.inf, math.inf, 12, math.inf, math.inf, 16, 1, 11, math.inf, math.inf, 4],
                [math.inf, math.inf, 13, math.inf, math.inf, 19, 16, 9, math.inf, math.inf, math.inf],
                [math.inf, math.inf, math.inf, 9, 7, math.inf, 11, 5, math.inf, math.inf, math.inf],
                [math.inf, 2, math.inf, math.inf, math.inf, 4, 5, math.inf, 10, math.inf, math.inf],
                [math.inf, math.inf, math.inf, 12, 16, math.inf, 6, 16, math.inf, 18, 7]]

    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 3), (0, 4), (0, 5), (0, 6), (1, 5), (1, 6), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 6), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 6), (4, 7), (4, 9), (4, 10)],
                 2: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 3), (8, 4), (8, 6), (8, 7), (9, 1), (9, 3), (9, 5), (9, 7), (10, 3), (10, 4), (10, 5), (10, 7), (10, 9), (10, 10)],
                 3: [(6, 0), (6, 1), (6, 8), (6, 9), (7, 0), (7, 1), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 5), (8, 8), (8, 9), (9, 0), (9, 2), (9, 4), (9, 6), (9, 8), (9, 9), (10, 0), (10, 1), (10, 2), (10, 3), (10, 6), (10, 8), (10, 10)]}

    visited_costs = {}
    visited_costs[(3, 10)] = 0

    queue = [(0, 0, [(3, 10)], (3, 10))]

    while queue:
        _, g, path, current_pos = heapq.heappop(queue)

        if current_pos == (6, 2):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current_pos[0] + d_row, current_pos[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_pos = (new_row, new_col)
                new_cost = g + city_map[new_row][new_col]

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    new_path = path + [new_pos]
                    # Check if Ben has visited at least one workshop in each district
                    if all(any(pos in district for pos in new_path) for district in districts.values()):
                        heapq.heappush(queue, (g + city_map[new_row][new_col], new_cost, new_path, new_pos))

    return None


print(a_star())

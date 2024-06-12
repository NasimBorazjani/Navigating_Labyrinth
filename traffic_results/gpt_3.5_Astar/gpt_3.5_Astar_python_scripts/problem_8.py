
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((None, None, None, None, 13, None, None, 3, 8),
                     (None, 18, 19, 19, 2, 9, None, None, None),
                     (15, None, 6, None, None, None, 13, 13, 4),
                     (7, None, 4, 10, None, 11, 10, 17, None),
                     (2, 7, None, None, 8, 16, 4, 1, 4),
                     (None, None, None, 5, 16, 15, None, 17, 10),
                     (None, None, None, 5, 14, 9, 3, 15, None),
                     (None, 6, 4, None, None, None, 18, None, None),
                     (17, None, 19, None, 1, 4, 8, None, 8))
    num_rows = 9
    num_cols = 9
    districts = {1: [(0, 2), (0, 5)], 2: [(3, 2), (3, 5)], 3: [(6, 2), (6, 5)]}
    start = (2, 8)
    end = (6, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(district) & set(path)) > 0 for district in districts.values()):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] is not None:
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]

                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]

                if new_row in range(3) and current[0] in range(3):
                    new_cost += 1
                elif new_row in range(3, 6) and current[0] in range(3, 6):
                    new_cost += 1
                elif new_row in range(6, 9) and current[0] in range(6, 9):
                    new_cost += 1

                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, new_path, (new_row, new_col)))

    return None


print(a_star())

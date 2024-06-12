
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 8, 18, 3, 19, 'x', 17, 'x', 'x', 'x', 'x'),
                     (19, 16, 'x', 18, 20, 2, 5, 7, 11, 12, 3),
                     (18, 'x', 18, 1, 2, 'x', 'x', 'x', 12, 16, 4),
                     (9, 20, 4, 19, 5, 15, 'x', 'x', 'x', 6, 4),
                     ('x', 18, 8, 1, 'x', 7, 1, 7, 10, 1, 4),
                     ('x', 18, 'x', 18, 19, 9, 18, 5, 15, 1, 7),
                     (3, 'x', 12, 14, 'x', 'x', 'x', 'x', 1, 'x', 'x'),
                     ('x', 12, 6, 'x', 6, 'x', 1, 'x', 1, 7, 'x'),
                     ('x', 5, 10, 14, 2, 'x', 'x', 7, 11, 3, 'x'),
                     (6, 9, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3),
                     (19, 12, 'x', 15, 'x', 14, 'x', 9, 'x', 'x', 19))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 2), 2: (3, 4), 3: (5, 10)}
    start = (3, 1)
    end = (5, 10)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get((i, j)) for i, j in path):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                district_check = {1: False, 2: False, 3: False}
                for i, j in new_path:
                    for district, (start_row, end_row) in districts.items():
                        if start_row <= i <= end_row:
                            district_check[district] = True
                if all(district_check.values()):
                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        h = heuristic((new_row, new_col), end)
                        heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))
    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

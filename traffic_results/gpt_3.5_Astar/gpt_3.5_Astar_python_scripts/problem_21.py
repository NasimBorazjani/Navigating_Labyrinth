
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15),
                     (12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3),
                     (4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6),
                     ('x', 'x', 5, 'x', 'x', 'x', 12, 6, 6, 'x'),
                     ('x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14),
                     (8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6),
                     (18, 'x', 'x', 15, 'x', 15, 4, 'x', 'x', 7),
                     (19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6),
                     (19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'),
                     (12, 1, 'x', 5, 3, 3, 'x', 'x', 'x', 'x'))
    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 1), (6, 1)], 3: [(7, 1), (9, 1)]}
    start = (1, 9)
    end = (6, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(districts[i]) & set(path)) > 0 for i in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]

                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]

                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    h = heuristic(new_path, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(path, end, districts):
    # The heuristic is the sum of the Manhattan distances from the current position to the destination, with an additional cost for visiting workshops in each district
    h = 0
    current = path[-1]
    h += abs(current[0] - end[0]) + abs(current[1] - end[1])

    for i in districts:
        if all(len(set(districts[i]) & set(path)) == 0 for i in districts):
            h += 100

    return h


print(a_star())


import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'),
                     ('x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7),
                     (5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8),
                     ('x', 4, 14, 'x', 'x', 'x', 'x', 'x', 'x', 7, 18),
                     (13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3),
                     ('x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'),
                     ('x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6),
                     ('x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11),
                     (12, 'x', 2, 'x', 'x', 1, 6, 'x', 15, 'x', 1),
                     (3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x', 'x'),
                     ('x', 'x', 6, 'x', 'x', 12, 'x', 'x', 'x', 15, 12))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 1), 2: (2, 4), 3: (5, 10)}
    start = (2, 10)
    end = (5, 2)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end:
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_district = get_district(new_row, districts)
                if new_row == end[0] and new_col == end[1]:
                    new_district = get_district(end[0], districts)
                if new_district not in [get_district(row, districts) for row in actions]:
                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        h = heuristic((new_row, new_col), end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))
    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())

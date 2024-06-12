
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
                     (11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'),
                     ('x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12),
                     (6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'),
                     (4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6),
                     ('x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'),
                     (19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11),
                     ('x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11),
                     ('x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15),
                     (10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17),
                     (19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17),
                     (18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8))
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 11)}
    start = (3, 3)
    end = (8, 11)

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
                new_state = (new_row, new_col)

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state))

    return None


def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the destination
    # If the current position is in a different district than the destination, add a large value to the heuristic to ensure Ben visits at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    current_district = get_district(current, districts)
    end_district = get_district(end, districts)
    if current_district != end_district:
        h += 1000
    return h


def get_district(position, districts):
    for district, (start, end) in districts.items():
        if start <= position[0] <= end:
            return district
    return None


print(a_star())

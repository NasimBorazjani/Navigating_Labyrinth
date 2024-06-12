
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((5, 10, 'x', 'x', 'x', 16, 'x', 'x', 'x', 16, 'x', 10, 8, 'x'),
                     (1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11),
                     (14, 'x', 'x', 'x', 9, 16, 16, 15, 'x', 'x', 15, 'x', 4, 4),
                     (15, 'x', 3, 'x', 'x', 17, 'x', 16, 10, 9, 'x', 6, 16, 17),
                     (12, 8, 'x', 10, 'x', 'x', 13, 10, 'x', 'x', 6, 3, 'x', 1),
                     ('x', 'x', 'x', 5, 8, 9, 6, 14, 1, 'x', 'x', 2, 12, 'x'),
                     (13, 'x', 'x', 'x', 16, 6, 'x', 17, 12, 18, 'x', 17, 8, 'x'),
                     (10, 'x', 14, 15, 'x', 'x', 'x', 20, 'x', 17, 18, 8, 'x', 4),
                     ('x', 11, 3, 'x', 'x', 'x', 'x', 7, 'x', 4, 'x', 'x', 11, 2),
                     (7, 'x', 'x', 10, 'x', 19, 'x', 7, 17, 'x', 'x', 14, 'x', 15),
                     (12, 11, 'x', 'x', 9, 7, 'x', 15, 1, 5, 5, 11, 15, 'x'),
                     ('x', 9, 9, 'x', 'x', 'x', 'x', 8, 'x', 8, 19, 11, 12, 12),
                     ('x', 17, 5, 'x', 'x', 17, 'x', 'x', 12, 'x', 15, 12, 10, 'x'),
                     (18, 'x', 'x', 'x', 3, 'x', 7, 'x', 8, 5, 12, 8, 10, 'x'))
    num_rows = 14
    num_cols = 14
    districts = {1: (0, 4), 2: (5, 9), 3: (10, 13)}
    start = (10, 12)
    end = (4, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end:
            return actions

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]

            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]

                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))

    return None


def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # If the current position is in a different district than the end position, the heuristic is increased by 10 to encourage visiting at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    current_district = get_district(current, districts)
    end_district = get_district(end, districts)
    if current_district != end_district:
        h += 10
    return h


def get_district(position, districts):
    for district, bounds in districts.items():
        if bounds[0] <= position[0] <= bounds[1]:
            return district
    return None


print(a_star())

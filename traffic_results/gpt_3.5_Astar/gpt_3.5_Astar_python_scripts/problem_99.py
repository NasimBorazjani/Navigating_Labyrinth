
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((7, 6, 11, 'x', 'x', 'x', 19, 'x', 9, 15, 12, 8, 10, 15, 5),
                     (9, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 2, 11, 'x', 10),
                     (14, 5, 'x', 'x', 4, 4, 12, 'x', 18, 'x', 17, 11, 3, 18, 19),
                     (18, 17, 'x', 8, 'x', 'x', 9, 'x', 'x', 8, 19, 10, 'x', 'x', 'x'),
                     (7, 'x', 'x', 11, 4, 'x', 'x', 10, 1, 2, 3, 12, 8, 12, 15),
                     ('x', 3, 7, 8, 'x', 'x', 'x', 'x', 4, 16, 13, 19, 14, 10, 13),
                     (18, 1, 2, 'x', 16, 20, 5, 'x', 2, 4, 20, 12, 14, 18, 16),
                     (1, 'x', 1, 'x', 15, 19, 11, 9, 19, 16, 'x', 'x', 'x', 'x', 19),
                     ('x', 8, 'x', 1, 7, 'x', 2, 3, 'x', 'x', 'x', 'x', 1, 3, 'x'),
                     (6, 16, 'x', 3, 'x', 18, 'x', 2, 18, 'x', 'x', 16, 'x', 'x', 8),
                     ('x', 9, 'x', 5, 2, 'x', 'x', 'x', 'x', 17, 'x', 6, 18, 14, 'x'),
                     ('x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 3, 'x', 10, 'x', 'x'),
                     ('x', 2, 15, 'x', 5, 15, 18, 8, 19, 'x', 'x', 'x', 'x', 'x', 10),
                     ('x', 'x', 4, 'x', 7, 2, 2, 'x', 19, 'x', 'x', 'x', 'x', 'x', 'x'),
                     (17, 'x', 'x', 'x', 5, 'x', 'x', 'x', 4, 1, 18, 'x', 9, 2, 8))
    num_rows = 15
    num_cols = 15
    districts = {1: (0, 4), 2: (5, 7), 3: (8, 14)}
    start = (4, 14)
    end = (8, 3)

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
    # The heuristic is the Manhattan distance between the current position and the destination
    # If the current position is in a different district than the destination, add a cost of 100 to the heuristic to encourage visiting at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    current_district = get_district(current, districts)
    end_district = get_district(end, districts)
    if current_district != end_district:
        h += 100
    return h


def get_district(position, districts):
    for district, bounds in districts.items():
        if bounds[0] <= position[0] <= bounds[1]:
            return district
    return None


print(a_star())

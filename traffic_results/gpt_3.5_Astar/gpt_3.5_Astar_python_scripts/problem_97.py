
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((17, 8, 'x', 3, 'x', 13, 'x', 'x', 14, 11, 'x', 'x', 'x', 'x', 'x'),
                     ('x', 'x', 'x', 7, 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 16, 'x', 13),
                     ('x', 'x', 2, 'x', 'x', 12, 10, 'x', 'x', 'x', 2, 'x', 'x', 5, 17),
                     (4, 3, 'x', 14, 'x', 'x', 16, 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x'),
                     (9, 'x', 18, 11, 19, 5, 'x', 'x', 'x', 'x', 'x', 'x', 3, 'x', 'x'),
                     ('x', 14, 'x', 4, 14, 12, 1, 'x', 13, 7, 10, 8, 8, 6, 9),
                     (7, 10, 'x', 18, 15, 8, 13, 14, 15, 'x', 'x', 'x', 13, 'x', 17),
                     (17, 7, 19, 15, 20, 19, 'x', 15, 13, 'x', 9, 'x', 11, 'x', 1),
                     ('x', 9, 6, 17, 14, 'x', 16, 'x', 19, 11, 'x', 14, 11, 'x', 'x'),
                     ('x', 18, 8, 2, 14, 2, 4, 'x', 4, 4, 4, 'x', 'x', 8, 19),
                     ('x', 'x', 5, 'x', 'x', 'x', 1, 5, 'x', 11, 'x', 'x', 1, 14, 'x'),
                     ('x', 'x', 'x', 'x', 5, 'x', 10, 'x', 'x', 'x', 'x', 10, 18, 'x', 19),
                     ('x', 'x', 2, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 6, 16),
                     ('x', 12, 1, 12, 'x', 'x', 15, 7, 18, 15, 13, 19, 'x', 2, 'x'),
                     ('x', 13, 8, 19, 5, 1, 'x', 13, 'x', 'x', 'x', 17, 'x', 3, 'x'))

    num_rows = 15
    num_cols = 15
    districts = {0: (0, 5), 1: (6, 8), 2: (9, 14)}
    start = (9, 1)
    end = (7, 14)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(len(set(actions[i:i+2])) == 2 for i in range(len(actions) - 1)):
            return actions + [end]

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]

            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_pos = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, actions + [current], new_pos))

    return None


def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance between the current position and the end position
    # If the current position is in a different district than the end position, add a cost of 100 to the heuristic
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    current_district = None
    end_district = None

    for district, (start_row, end_row) in districts.items():
        if start_row <= current[0] <= end_row:
            current_district = district
        if start_row <= end[0] <= end_row:
            end_district = district

    if current_district != end_district:
        h += 100

    return h


print(a_star())

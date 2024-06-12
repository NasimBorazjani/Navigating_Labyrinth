
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((10, 'x', 'x', 'x', 16, 9, 'x', 13, 12, 8, 'x', 16, 17),
                     (9, 2, 'x', 'x', 5, 'x', 'x', 'x', 12, 'x', 3, 'x', 'x'),
                     ('x', 'x', 7, 3, 12, 'x', 11, 18, 10, 'x', 'x', 13, 'x'),
                     ('x', 6, 'x', 19, 2, 'x', 'x', 11, 13, 13, 1, 'x', 7),
                     ('x', 'x', 11, 'x', 16, 16, 4, 12, 5, 20, 2, 4, 15),
                     (19, 'x', 18, 5, 11, 'x', 'x', 3, 17, 18, 3, 8, 18),
                     (12, 'x', 9, 'x', 'x', 'x', 'x', 9, 4, 15, 16, 'x', 9),
                     ('x', 15, 'x', 6, 10, 'x', 1, 1, 'x', 9, 4, 7, 1),
                     ('x', 19, 15, 'x', 1, 10, 5, 17, 'x', 8, 'x', 1, 'x'),
                     ('x', 'x', 'x', 'x', 5, 'x', 1, 'x', 'x', 7, 4, 'x', 'x'),
                     (9, 'x', 4, 'x', 5, 13, 'x', 15, 'x', 'x', 18, 9, 15),
                     (17, 2, 'x', 'x', 'x', 18, 8, 'x', 8, 'x', 'x', 8, 7),
                     ('x', 'x', 5, 'x', 'x', 8, 'x', 8, 'x', 15, 19, 'x', 'x'))
    num_rows = 13
    num_cols = 13
    districts = {1: (0, 3), 2: (4, 6), 3: (7, 12)}
    start = (3, 12)
    end = (7, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(districts[d][0] in [action[0] for action in actions] for d in districts):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_actions = actions + [(new_row, new_col)]
                new_state = (new_row, new_col)

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, end, districts)
                    heapq.heappush(queue, (g + h, new_cost, new_actions, new_state))

    return None


def heuristic(current, end, districts):
    # The heuristic is the Manhattan distance from the current position to the destination
    # Additionally, the heuristic ensures that at least one workshop in each district is visited
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])
    for d in districts:
        if districts[d][0] not in [action[0] for action in actions]:
            h += 1
    return h


print(a_star())

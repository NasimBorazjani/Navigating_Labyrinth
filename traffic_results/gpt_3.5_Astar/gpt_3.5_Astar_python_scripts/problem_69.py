
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16),
                     ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6),
                     (9, 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19),
                     (1, 'x', 'x', 'x', 13, 'x', 'x', 'x', 3, 2, 7, 4, 3),
                     ('x', 'x', 'x', 14, 19, 20, 10, 13, 14, 2, 'x', 9, 3),
                     (15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19),
                     (19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5),
                     ('x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'),
                     ('x', 'x', 'x', 'x', 'x', 14, 'x', 10, 14, 13, 'x', 13, 'x'),
                     (15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14),
                     (10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 'x', 13, 2, 'x'),
                     ('x', 'x', 17, 'x', 'x', 'x', 'x', 7, 'x', 'x', 16, 'x', 'x'),
                     (12, 10, 'x', 15, 16, 'x', 'x', 7, 11, 7, 'x', 17, 'x'))
    num_rows = 13
    num_cols = 13
    districts = {1: [(0, 1), (1, 1)], 2: [(2, 1), (5, 1)], 3: [(6, 1), (12, 1)]}
    start = (1, 12)
    end = (6, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(len(set(districts[i]) & set(actions)) > 0 for i in districts):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_pos = (new_row, new_col)

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos))

    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

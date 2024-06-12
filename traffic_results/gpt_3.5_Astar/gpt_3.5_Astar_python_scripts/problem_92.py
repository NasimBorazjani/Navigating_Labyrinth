
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 1, 'x', 3, 'x', 9, 15, 8, 17, 'x', 'x', 6, 'x', 12, 3),
                     ('x', 'x', 'x', 14, 'x', 7, 18, 6, 14, 2, 19, 15, 'x', 'x', 'x'),
                     (4, 3, 'x', 10, 8, 4, 16, 13, 6, 'x', 18, 10, 14, 'x', 'x'),
                     ('x', 'x', 'x', 10, 'x', 14, 10, 7, 'x', 'x', 'x', 4, 2, 19, 3),
                     (5, 'x', 10, 'x', 18, 12, 20, 15, 'x', 'x', 11, 11, 1, 10, 19),
                     (8, 'x', 13, 'x', 'x', 'x', 16, 7, 3, 'x', 'x', 2, 18, 11, 'x'),
                     (12, 'x', 15, 'x', 'x', 6, 'x', 'x', 'x', 'x', 18, 3, 14, 3, 6),
                     ('x', 6, 13, 19, 19, 'x', 7, 12, 18, 5, 'x', 1, 4, 18, 11),
                     (5, 'x', 18, 'x', 12, 4, 3, 7, 'x', 16, 1, 'x', 16, 2, 'x'),
                     ('x', 'x', 'x', 'x', 18, 'x', 'x', 14, 15, 1, 'x', 'x', 9, 'x', 'x'),
                     ('x', 13, 'x', 7, 7, 'x', 'x', 16, 10, 'x', 'x', 'x', 'x', 8, 'x'),
                     ('x', 'x', 19, 18, 8, 18, 'x', 'x', 12, 'x', 13, 'x', 17, 12, 7),
                     ('x', 'x', 'x', 'x', 7, 7, 13, 17, 'x', 'x', 'x', 'x', 'x', 9, 5),
                     (9, 'x', 14, 'x', 9, 'x', 8, 'x', 'x', 'x', 17, 4, 12, 12, 12),
                     (8, 1, 11, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 2, 16, 'x', 15))
    num_rows = 15
    num_cols = 15
    districts = {0: (0, 2), 1: (3, 6), 2: (7, 14)}
    start = (7, 14)
    end = (2, 4)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(len(set(actions[i][0] for i in range(len(actions)) if actions[i][0] in range(districts[j][0], districts[j][1] + 1)) > 0 for j in range(3)):
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

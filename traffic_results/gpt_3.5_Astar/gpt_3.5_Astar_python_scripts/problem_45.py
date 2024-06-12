
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1),
                     ('x', 8, 'x', 9, 'x', 'x', 18, 5, 1, 12, 14),
                     (2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'),
                     (17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13),
                     ('x', 'x', 'x', 9, 17, 'x', 'x', 'x', 'x', 12, 17),
                     ('x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8),
                     (18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3),
                     (4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6),
                     (15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'),
                     ('x', 'x', 'x', 4, 'x', 'x', 'x', 13, 'x', 'x', 'x'),
                     ('x', 3, 'x', 'x', 'x', 'x', 1, 'x', 'x', 5, 13))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 3), 2: (4, 5), 3: (6, 10)}
    start = (3, 10)
    end = (6, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get((i, j)) for i, j in actions):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_actions = actions + [(new_row, new_col)]
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, new_actions, (new_row, new_col)))

    return None


print(a_star())

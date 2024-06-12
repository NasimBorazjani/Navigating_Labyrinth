
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((9, 4, 16, 7, 'x', 2, 'x', 'x', 14, 'x', 'x', 'x'),
                     ('x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18),
                     (12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7),
                     (10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'),
                     (11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7),
                     ('x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20),
                     ('x', 3, 17, 17, 'x', 'x', 18, 4, 'x', 'x', 9, 4),
                     ('x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11),
                     ('x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2),
                     ('x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12),
                     ('x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'),
                     ('x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x'))
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 8), 3: (9, 11)}
    start = (3, 9)
    end = (7, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get((end[0], i)) for i in range(districts[1][0], districts[1][1] + 1)) and all(visited_costs.get((end[0], i)) for i in range(districts[2][0], districts[2][1] + 1)) and all(visited_costs.get((end[0], i)) for i in range(districts[3][0], districts[3][1] + 1)):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_pos = (new_row, new_col)
                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_pos, end), new_cost, actions + [new_pos], new_pos))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

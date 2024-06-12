
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((13, 'x', 'x', 3, 10, 20, 3, 'x', 5),
                     ('x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17),
                     (3, 14, 18, 8, 1, 20, 14, 'x', 7),
                     (13, 3, 6, 10, 7, 4, 6, 6, 1),
                     (10, 12, 2, 'x', 11, 'x', 10, 8, 11),
                     ('x', 'x', 'x', 11, 6, 18, 13, 20, 17),
                     ('x', 'x', 16, 'x', 4, 17, 7, 10, 15),
                     ('x', 7, 16, 6, 19, 4, 7, 'x', 'x'),
                     ('x', 11, 18, 'x', 'x', 'x', 3, 8, 'x'))
    num_rows = 9
    num_cols = 9
    districts = {1: (0, 2), 2: (3, 4), 3: (5, 8)}
    start = (5, 7)
    end = (2, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], [start])]

    while queue:
        _, g, actions, path = heapq.heappop(queue)
        current_position = path[-1]

        if current_position == end:
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current_position[0] + d_row, current_position[1] + d_col

            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_path = path + [new_position]
                new_cost = g + initial_state[new_row][new_col]

                if all(districts[dist][0] <= new_row <= districts[dist][1] for dist in districts for workshop in new_path):
                    if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                        visited_costs[new_position] = new_cost
                        h = heuristic(new_position, end)
                        heapq.heappush(queue, (g + h, g + initial_state[new_row][new_col], actions + [new_position], new_path))

    return None


def heuristic(current_position, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current_position[0] - end[0]) + abs(current_position[1] - end[1])


print(a_star())

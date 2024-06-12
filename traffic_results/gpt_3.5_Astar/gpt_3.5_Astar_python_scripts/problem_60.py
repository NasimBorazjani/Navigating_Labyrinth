
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'),
                     (17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'),
                     (3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'),
                     (13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'),
                     (5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1),
                     (4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4),
                     (7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'),
                     ('x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'),
                     (2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 12),
                     ('x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'),
                     ('x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'),
                     ('x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x'))
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 3), 2: (4, 8), 3: (9, 11)}
    start = (3, 0)
    end = (9, 7)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [1 if districts[i][0] <= workshop[0] <= districts[i][1] else 0 for i in range(1, 4)] for workshop in path):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]

                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]

                if new_path[-1] not in visited_costs or new_cost < visited_costs[new_path[-1]]:
                    visited_costs[new_path[-1]] = new_cost
                    h = heuristic(new_path, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(path, end):
    # A heuristic function that calculates the Manhattan distance from the current position to the end position
    # This heuristic is admissible as it never overestimates the cost to reach the goal
    # It is consistent because the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance
    return abs(path[-1][0] - end[0]) + abs(path[-1][1] - end[1])


print(a_star())

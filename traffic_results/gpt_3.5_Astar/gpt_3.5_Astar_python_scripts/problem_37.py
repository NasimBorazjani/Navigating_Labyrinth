
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 'x', 12, 'x', 9, 19, 'x', 'x', 13, 'x', 16),
                     (14, 6, 3, 18, 'x', 8, 18, 'x', 'x', 'x', 'x'),
                     (16, 10, 9, 4, 9, 5, 15, 4, 'x', 'x', 2),
                     (5, 9, 'x', 8, 1, 15, 7, 15, 'x', 'x', 'x'),
                     (6, 'x', 3, 'x', 4, 6, 6, 19, 'x', 16, 13),
                     (17, 'x', 11, 5, 18, 11, 18, 'x', 'x', 10, 19),
                     (6, 3, 'x', 'x', 10, 18, 2, 'x', 'x', 'x', 'x'),
                     ('x', 'x', 4, 2, 'x', 13, 7, 'x', 3, 19, 16),
                     ('x', 1, 10, 'x', 15, 'x', 2, 'x', 1, 7, 10),
                     ('x', 'x', 'x', 4, 7, 'x', 7, 'x', 'x', 6, 'x'),
                     (16, 'x', 15, 3, 'x', 8, 'x', 'x', 13, 'x', 14))
    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (6, 0)], 3: [(7, 0), (10, 0)]}
    start = (7, 5)
    end = (1, 0)

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

                if new_position in districts[1] and len(set([p for p in new_path if p in districts[1]])) == 1:
                    new_cost += 100
                elif new_position in districts[2] and len(set([p for p in new_path if p in districts[2]])) == 1:
                    new_cost += 100
                elif new_position in districts[3] and len(set([p for p in new_path if p in districts[3]])) == 1:
                    new_cost += 100

                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_path))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

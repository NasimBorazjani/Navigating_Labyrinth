
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((12, 11, 14, 10, 2, 11, 13, 16, 3, 'x', 12),
                     (10, 9, 'x', 8, 'x', 'x', 1, 16, 11, 'x', 15),
                     (1, 18, 1, 'x', 'x', 'x', 'x', 'x', 12, 9, 'x'),
                     (1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6),
                     (18, 11, 'x', 'x', 'x', 15, 'x', 'x', 1, 1, 'x'),
                     (14, 'x', 'x', 'x', 18, 14, 16, 7, 'x', 1, 'x'),
                     (11, 15, 'x', 'x', 15, 3, 11, 13, 'x', 'x', 'x'),
                     (5, 'x', 'x', 'x', 'x', 'x', 15, 'x', 6, 'x', 'x'),
                     (12, 11, 7, 2, 11, 'x', 10, 2, 17, 'x', 'x'),
                     (7, 'x', 'x', 'x', 4, 'x', 4, 'x', 'x', 5, 'x'),
                     ('x', 19, 10, 7, 'x', 2, 3, 9, 2, 6, 'x'))
    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 2), (0, 9)], 2: [(3, 6)], 3: [(7, 10)]}
    start = (7, 0)
    end = (2, 9)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(districts[i]) & set(path)) > 0 for i in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row != current[0] or new_col != current[1]:
                    new_cost += initial_state[current[0]][current[1]]
                if new_row != end[0] or new_col != end[1]:
                    new_cost += initial_state[end[0]][end[1]]
                if new_row not in visited_costs or new_cost < visited_costs[new_row]:
                    visited_costs[new_row] = new_cost
                    h = heuristic(new_row, new_col, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))
    return None


def heuristic(current, end):
    # A consistent and admissible heuristic is the Manhattan distance between the current position and the end position
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the agent can only move in 4 directions
    # The heuristic is consistent because the cost of moving from one cell to a neighboring cell is always 1, which is exactly the decrease in the Manhattan distance, if the agent moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

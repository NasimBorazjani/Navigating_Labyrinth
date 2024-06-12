
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((18, 'x', 'x', 'x', 19, 'x', 'x', 8, 6, 3, 'x', 'x', 'x'),
                     ('x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 4, 6, 4),
                     (1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'),
                     (3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 10, 'x', 'x'),
                     (17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'),
                     ('x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10),
                     (16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'),
                     (5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 8, 'x', 1),
                     (10, 'x', 1, 'x', 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x'),
                     ('x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 'x', 12, 13, 'x'),
                     ('x', 'x', 18, 14, 'x', 'x', 5, 'x', 'x', 13, 1, 'x', 'x'),
                     ('x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'),
                     ('x', 'x', 'x', 16, 1, 'x', 19, 'x', 'x', 'x', 'x', 14, 'x'))
    num_rows = 13
    num_cols = 13
    districts = {1: [(0, 1), (1, 2)], 2: [(2, 5), (5, 12)], 3: [(6, 12), (0, 1)]}
    start = (5, 12)
    end = (1, 2)


    visited_costs = {}
    visited_costs[start] = 0


    queue = [(0, 0, [start], start)]


    while queue:
        _, g, path, current = heapq.heappop(queue)


        if current == end and all(any(cell != 'x' for cell in row) for row in initial_state):
            return path


        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                if new_row in range(districts[1][0][0], districts[1][1][0] + 1) and new_col in range(districts[1][0][1], districts[1][1][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                if new_row in range(districts[2][0][0], districts[2][1][0] + 1) and new_col in range(districts[2][0][1], districts[2][1][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                if new_row in range(districts[3][0][0], districts[3][1][0] + 1) and new_col in range(districts[3][0][1], districts[3][1][1] + 1):
                    new_cost += initial_state[new_row][new_col]
                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    h = heuristic(new, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, new))
    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

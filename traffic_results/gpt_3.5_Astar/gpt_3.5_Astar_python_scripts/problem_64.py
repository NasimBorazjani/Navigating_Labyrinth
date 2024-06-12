
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[8, 'x', 12, 'x', 16, 'x', 'x', 'x', 7, 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 16, 'x', 7, 8, 'x', 17, 'x', 19, 'x'],
                [7, 'x', 13, 'x', 19, 'x', 6, 'x', 14, 'x', 18, 'x', 19],
                [9, 20, 2, 'x', 10, 6, 'x', 18, 'x', 'x', 'x', 18, 'x'],
                ['x', 'x', 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7],
                ['x', 14, 'x', 'x', 'x', 19, 13, 15, 3, 12, 16, 16, 3],
                ['x', 'x', 'x', 13, 'x', 9, 13, 10, 'x', 14, 'x', 4, 18],
                [6, 12, 10, 'x', 'x', 18, 7, 20, 18, 'x', 13, 1, 'x'],
                ['x', 5, 'x', 18, 12, 'x', 'x', 3, 12, 14, 19, 16, 'x'],
                [10, 'x', 19, 'x', 'x', 'x', 'x', 11, 14, 16, 12, 'x', 8],
                [8, 'x', 'x', 'x', 'x', 'x', 'x', 9, 16, 15, 'x', 'x', 8],
                ['x', 'x', 2, 'x', 1, 'x', 'x', 16, 'x', 'x', 3, 'x', 'x'],
                [9, 'x', 5, 'x', 'x', 15, 'x', 'x', 'x', 7, 15, 9, 'x']]

    num_rows = 13
    num_cols = 13
    districts = {1: (0, 3), 2: (4, 5), 3: (6, 12)}
    start = (3, 0)
    end = (6, 12)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end:
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if districts[1][0] <= new_row <= districts[1][1] or districts[2][0] <= new_row <= districts[2][1] or districts[3][0] <= new_row <= districts[3][1]:
                    if new_row == end[0] or new_col == end[1]:
                        new_cost += 100
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic((new_row, new_col), end), new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

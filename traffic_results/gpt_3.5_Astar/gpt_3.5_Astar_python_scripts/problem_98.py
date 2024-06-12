
import heapq
import math


def a_star():
    # Define the city map as a 2D list
    city_map = [
        ['x', 19, 4, 'x', 17, 11, 'x', 'x', 18, 7, 'x', 8, 20, 'x', 1],
        ['x', 16, 'x', 1, 9, 1, 'x', 8, 16, 'x', 15, 7, 1, 'x', 'x'],
        [7, 'x', 9, 9, 9, 'x', 18, 'x', 15, 13, 10, 'x', 19, 16, 9],
        ['x', 'x', 'x', 6, 'x', 'x', 7, 10, 18, 17, 'x', 8, 9, 6, 5],
        [4, 17, 'x', 'x', 19, 5, 20, 1, 15, 18, 'x', 'x', 5, 8, 2],
        ['x', 'x', 'x', 3, 10, 19, 17, 20, 'x', 'x', 'x', 3, 'x', 5, 'x'],
        ['x', 'x', 'x', 3, 8, 2, 'x', 'x', 7, 19, 'x', 'x', 1, 19, 9],
        ['x', 19, 16, 6, 5, 19, 'x', 'x', 'x', 12, 'x', 3, 8, 10, 'x'],
        [13, 2, 'x', 18, 'x', 'x', 5, 'x', 'x', 'x', 13, 1, 'x', 'x', 6],
        [19, 8, 8, 10, 'x', 'x', 'x', 12, 14, 5, 14, 2, 6, 'x', 'x'],
        ['x', 'x', 'x', 12, 18, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 19, 'x'],
        [11, 'x', 12, 'x', 'x', 5, 'x', 15, 8, 'x', 9, 'x', 'x', 'x', 'x'],
        [9, 'x', 4, 'x', 'x', 'x', 'x', 2, 18, 'x', 11, 'x', 11, 'x', 19],
        [13, 'x', 17, 1, 'x', 14, 'x', 'x', 'x', 'x', 16, 'x', 2, 'x', 'x'],
        [3, 16, 'x', 'x', 3, 11, 'x', 15, 'x', 'x', 'x', 'x', 16, 'x']
    ]

    num_rows = 15
    num_cols = 15
    districts = [(0, 3), (4, 8), (9, 14)]
    start = (9, 3)
    end = (4, 14)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(path).intersection(range(start, end+1))) > 0 for start, end in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += city_map[end[0]][end[1]]
                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    h = heuristic(new_row, new_col, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

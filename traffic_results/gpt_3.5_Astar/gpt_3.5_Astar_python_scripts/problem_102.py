
import heapq
import math


def a_star():
    # Define the city map as a 2D list
    city_map = [[0, 13, 0, 0, 0, 0, 3, 4, 0, 0, 9, 0, 18, 7, 2],
                [1, 10, 17, 0, 0, 0, 11, 13, 0, 10, 0, 9, 13, 0, 0],
                [0, 0, 7, 18, 0, 0, 0, 0, 7, 0, 0, 0, 1, 0, 16],
                [10, 0, 0, 0, 13, 0, 2, 9, 0, 0, 8, 0, 0, 5, 0],
                [0, 7, 12, 0, 1, 18, 14, 0, 7, 0, 0, 16, 0, 0, 19],
                [5, 1, 13, 17, 11, 14, 16, 0, 14, 0, 18, 5, 0, 18, 0],
                [0, 15, 19, 4, 0, 13, 0, 5, 0, 0, 18, 0, 17, 0, 0],
                [3, 7, 0, 0, 0, 12, 0, 0, 17, 4, 0, 13, 19, 3, 10],
                [11, 0, 0, 0, 0, 2, 2, 19, 13, 4, 7, 17, 16, 0, 17],
                [12, 5, 4, 0, 0, 0, 0, 12, 8, 11, 0, 17, 14, 19, 2],
                [4, 10, 0, 0, 6, 11, 16, 17, 0, 0, 18, 0, 17, 0, 0],
                [0, 0, 0, 0, 11, 9, 18, 17, 12, 0, 0, 0, 0, 0, 1],
                [18, 13, 7, 0, 0, 5, 4, 13, 0, 0, 19, 12, 1, 18, 0],
                [15, 0, 17, 0, 0, 0, 17, 0, 0, 0, 10, 0, 15, 16, 0],
                [0, 0, 11, 15, 0, 0, 12, 16, 12, 13, 18, 0, 17, 8, 15]]

    num_rows = 15
    num_cols = 15
    districts = {1: (0, 5), 2: (6, 6), 3: (7, 14)}
    start = (5, 0)
    end = (7, 13)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(path).intersection(range(districts[i][0], districts[i][1] + 1))) > 0 for i in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 0:
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_row, new_col, end), new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

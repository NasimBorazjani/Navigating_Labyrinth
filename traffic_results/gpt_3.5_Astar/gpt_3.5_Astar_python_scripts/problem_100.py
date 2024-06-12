
import heapq
import math


def a_star():
    # Define the city map as a 2D list
    city_map = [[0, 2, 16, 0, 9, 0, 14, 0, 8, 0, 16, 0, 0, 4, 8],
                [9, 0, 4, 0, 0, 7, 11, 0, 0, 13, 0, 0, 6, 11, 0],
                [0, 0, 10, 14, 0, 0, 18, 0, 0, 0, 0, 0, 6, 16, 0],
                [0, 14, 0, 1, 0, 7, 5, 16, 0, 19, 0, 0, 10, 7, 0],
                [1, 3, 0, 19, 7, 2, 17, 0, 0, 6, 0, 0, 0, 10, 14],
                [14, 0, 0, 0, 12, 0, 16, 5, 8, 12, 17, 2, 19, 0, 5],
                [9, 9, 8, 15, 18, 0, 16, 0, 10, 0, 0, 14, 0, 0, 0],
                [18, 20, 0, 0, 11, 2, 17, 6, 0, 18, 8, 0, 6, 16, 0],
                [12, 0, 0, 0, 0, 7, 14, 4, 8, 12, 3, 0, 15, 13, 2],
                [16, 0, 0, 0, 12, 0, 8, 1, 7, 7, 12, 17, 2, 2, 7],
                [0, 13, 3, 3, 1, 0, 6, 14, 20, 8, 0, 4, 10, 17, 0],
                [1, 8, 0, 16, 0, 0, 0, 9, 0, 0, 10, 0, 0, 5, 8],
                [0, 0, 1, 0, 0, 6, 0, 0, 0, 7, 16, 0, 0, 0, 0],
                [14, 0, 0, 10, 18, 0, 6, 13, 0, 0, 0, 0, 0, 15, 0],
                [0, 8, 2, 0, 17, 0, 12, 16, 11, 4, 4, 0, 17, 0, 0]]

    num_rows = 15
    num_cols = 15
    districts = {1: (0, 4), 2: (5, 9), 3: (10, 14)}
    start = (4, 0)
    end = (9, 11)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [city_map[i][j] for j in range(districts[d][0], districts[d][1] + 1)] for d in districts for i in range(districts[d][0], districts[d][1] + 1)):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 0:
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += city_map[end[0]][end[1]]
                if new_row in range(districts[1][0], districts[1][1] + 1) or new_row in range(districts[2][0], districts[2][1] + 1) or new_row in range(districts[3][0], districts[3][1] + 1):
                    if new_row == end[0] and new_col == end[1]:
                        new_cost += city_map[end[0]][end[1]]
                    if new_cost < visited_costs.get((new_row, new_col), math.inf):
                        visited_costs[(new_row, new_col)] = new_cost
                        heapq.heappush(queue, (new_cost, g + city_map[new_row][new_col], new_path, (new_row, new_col)))

    return None


print(a_star())

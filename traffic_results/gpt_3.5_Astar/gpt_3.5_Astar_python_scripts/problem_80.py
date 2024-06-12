
import heapq
import math

def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 8, 16, 3, 0, 15, 17, 2, 0, 0, 5, 0, 0],
                [0, 0, 17, 0, 13, 0, 4, 0, 13, 3, 3, 6, 11, 0],
                [0, 0, 8, 0, 14, 1, 15, 11, 0, 18, 12, 0, 0, 0],
                [0, 13, 19, 4, 13, 2, 13, 3, 0, 1, 20, 18, 0, 15],
                [13, 0, 1, 0, 11, 0, 8, 14, 4, 11, 3, 0, 0, 0],
                [12, 11, 16, 1, 1, 0, 5, 1, 0, 9, 0, 0, 1, 0],
                [8, 0, 6, 15, 0, 7, 19, 13, 2, 0, 3, 3, 0, 2],
                [18, 0, 19, 15, 2, 0, 0, 18, 2, 0, 10, 0, 0, 1],
                [3, 4, 0, 19, 0, 6, 0, 7, 0, 0, 0, 0, 15, 0],
                [0, 0, 0, 16, 7, 17, 11, 0, 7, 0, 0, 0, 0, 15],
                [0, 9, 0, 0, 0, 19, 19, 7, 3, 12, 14, 11, 16, 7],
                [8, 19, 15, 1, 0, 14, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 14, 0, 0, 0, 0, 0, 18, 0, 0, 2, 11, 7, 0],
                [0, 0, 0, 0, 0, 3, 11, 12, 0, 0, 0, 2, 6, 0]]

    num_rows = 14
    num_cols = 14
    start = (1, 10)
    end = (7, 2)
    districts = [(0, 1), (2, 6), (7, 13)]

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end:
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 0:
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set(new_path).intersection(districts[0])) == 0:
                    continue
                if new_row in range(districts[1][0], districts[1][1] + 1) and len(set(new_path).intersection(districts[1])) == 0:
                    continue
                if new_row in range(districts[2][0], districts[2][1] + 1) and len(set(new_path).intersection(districts[2])) == 0:
                    continue
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + city_map[new_row][new_col], new_cost, new_path, (new_row, new_col)))

    return None

print(a_star())

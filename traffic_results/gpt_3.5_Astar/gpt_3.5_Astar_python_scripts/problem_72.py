
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 0, 0, 9, 1, 14, 0, 0, 0, 11, 15, 12],
                [2, 0, 18, 0, 14, 0, 11, 3, 0, 0, 0, 0, 0],
                [10, 0, 3, 0, 0, 0, 8, 6, 0, 10, 9, 7, 0],
                [1, 18, 2, 6, 0, 0, 1, 5, 0, 0, 6, 0, 0],
                [4, 14, 12, 3, 2, 2, 15, 8, 19, 3, 18, 0, 0],
                [5, 6, 2, 2, 13, 0, 7, 3, 12, 0, 16, 10, 5],
                [0, 2, 13, 0, 0, 9, 5, 0, 0, 0, 7, 10, 11],
                [17, 10, 3, 11, 4, 0, 0, 19, 0, 5, 0, 0, 9],
                [13, 0, 0, 0, 0, 9, 13, 4, 7, 0, 13, 10, 0],
                [0, 0, 0, 9, 0, 8, 8, 14, 0, 0, 19, 0, 0],
                [6, 0, 0, 0, 0, 0, 1, 11, 0, 4, 13, 0, 0],
                [0, 0, 0, 11, 11, 0, 9, 16, 12, 0, 6, 0, 5],
                [16, 19, 14, 0, 5, 13, 0, 0, 0, 0, 0, 13, 0]]

    num_rows = 13
    num_cols = 13
    districts = {1: (0, 3), 2: (4, 5), 3: (6, 12)}
    start = (6, 12)
    end = (5, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [city_map[i][j] for j in range(num_cols)] for i in range(num_rows)):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < num_rows and 0 <= new_j < num_cols and city_map[new_i][new_j] != 0:
                new_cost = g + city_map[new_i][new_j]
                new_path = path + [(new_i, new_j)]
                if districts[1][0] <= new_i <= districts[1][1] and 1 not in [city_map[i][j] for i, j in new_path]:
                    new_cost += 1
                if districts[2][0] <= new_i <= districts[2][1] and 2 not in [city_map[i][j] for i, j in new_path]:
                    new_cost += 1
                if districts[3][0] <= new_i <= districts[3][1] and 3 not in [city_map[i][j] for i, j in new_path]:
                    new_cost += 1

                if new_cost < visited_costs.get((new_i, new_j), math.inf):
                    visited_costs[(new_i, new_j)] = new_cost
                    heapq.heappush(queue, (new_cost + abs(new_i - end[0]) + abs(new_j - end[1]), new_cost, new_path, (new_i, new_j)))

    return None


print(a_star())

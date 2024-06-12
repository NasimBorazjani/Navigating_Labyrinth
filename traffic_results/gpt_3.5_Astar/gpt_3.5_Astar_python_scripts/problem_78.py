
import heapq
import math

def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 0, 16, 11, 12, 0, 0, 17, 3, 0, 0, 4, 6],
                [4, 17, 0, 0, 3, 0, 0, 1, 9, 11, 12, 4, 0, 0],
                [5, 0, 0, 7, 14, 4, 5, 7, 13, 4, 7, 0, 0, 0],
                [6, 6, 19, 3, 15, 0, 0, 0, 0, 4, 10, 19, 2, 4],
                [3, 16, 8, 0, 5, 0, 12, 17, 16, 0, 9, 5, 6, 0],
                [17, 2, 0, 0, 16, 0, 5, 0, 0, 5, 17, 7, 2, 5],
                [19, 0, 0, 0, 0, 2, 15, 15, 0, 3, 11, 0, 4, 0],
                [0, 0, 11, 0, 0, 17, 5, 0, 5, 0, 0, 19, 6, 0],
                [16, 17, 16, 0, 12, 0, 2, 18, 9, 7, 0, 13, 0, 0],
                [18, 11, 0, 0, 19, 5, 0, 0, 18, 4, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 5, 4, 12, 3, 0, 4, 14, 7, 19],
                [18, 0, 0, 0, 7, 17, 0, 0, 3, 15, 0, 16, 0, 10],
                [0, 11, 15, 0, 0, 0, 0, 0, 2, 13, 0, 0, 0, 3],
                [4, 8, 0, 0, 0, 0, 12, 13, 0, 0, 19, 0, 6, 0]]

    num_rows = 14
    num_cols = 14
    start = (7, 12)
    end = (2, 0)
    districts = [(0, 2), (3, 6), (7, 13)]

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
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set(new_path)) >= 2:
                    new_cost += 10
                elif new_row in range(districts[1][0], districts[1][1] + 1) and len(set(new_path)) >= 2:
                    new_cost += 10
                elif new_row in range(districts[2][0], districts[2][1] + 1) and len(set(new_path)) >= 2:
                    new_cost += 10

                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (new_cost + abs(new_row - end[0]) + abs(new_col - end[1]), new_cost, new_path, (new_row, new_col)))

    return None

print(a_star())

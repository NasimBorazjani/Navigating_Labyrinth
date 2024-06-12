
import heapq
import math

def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 0, 0, 2, 19, 0, 0, 15, 0, 0, 2, 17, 18, 18],
                [0, 0, 2, 18, 3, 17, 1, 0, 0, 0, 6, 0, 0, 7, 9],
                [0, 0, 2, 10, 3, 0, 6, 11, 5, 7, 8, 17, 0, 12, 6],
                [0, 14, 13, 9, 3, 0, 18, 0, 17, 16, 14, 8, 9, 0, 13],
                [0, 0, 0, 17, 0, 16, 9, 3, 1, 0, 5, 20, 2, 2, 6],
                [8, 0, 8, 0, 5, 19, 12, 19, 7, 1, 5, 4, 11, 13, 16],
                [0, 6, 19, 17, 20, 0, 0, 14, 14, 0, 0, 3, 20, 13, 3],
                [12, 14, 7, 1, 15, 0, 8, 8, 0, 0, 0, 15, 0, 0, 0],
                [0, 9, 0, 0, 4, 7, 7, 0, 0, 13, 7, 7, 0, 6, 0],
                [0, 0, 0, 11, 10, 0, 0, 0, 5, 0, 7, 14, 0, 19, 0],
                [0, 11, 18, 0, 19, 0, 1, 18, 1, 8, 0, 0, 12, 15, 0],
                [19, 0, 7, 0, 9, 3, 0, 7, 12, 13, 19, 13, 0, 9, 0],
                [0, 17, 9, 0, 6, 0, 6, 0, 0, 11, 0, 19, 0, 0, 0],
                [4, 17, 5, 0, 7, 5, 17, 12, 0, 16, 8, 0, 0, 17, 0],
                [15, 2, 13, 0, 14, 0, 0, 17, 0, 0, 1, 0, 19, 1, 17]]

    num_rows = 15
    num_cols = 15
    districts = {1: (0, 4), 2: (5, 6), 3: (7, 14)}
    start = (4, 14)
    end = (7, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(visited_costs[workshop] for workshop in [start, end]):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < num_rows and 0 <= new_j < num_cols and city_map[new_i][new_j] != 0:
                new_workshop = (new_i, new_j)
                new_path = path + [new_workshop]
                new_cost = g + city_map[new_i][new_j]

                if districts[1][0] <= new_i <= districts[1][1] and visited_costs.get(new_workshop, math.inf) > new_cost:
                    visited_costs[new_workshop] = new_cost
                    heapq.heappush(queue, (g + 1 + heuristic(new_workshop, end), g + 1, new_path, new_workshop))
                elif districts[2][0] <= new_i <= districts[2][1] and visited_costs.get(new_workshop, math.inf) > new_cost:
                    visited_costs[new_workshop] = new_cost
                    heapq.heappush(queue, (g + 1 + heuristic(new_workshop, end), g + 1, new_path, new_workshop))
                elif districts[3][0] <= new_i <= districts[3][1] and visited_costs.get(new_workshop, math.inf) > new_cost:
                    visited_costs[new_workshop] = new_cost
                    heapq.heappush(queue, (g + 1 + heuristic(new_workshop, end), g + 1, new_path, new_workshop))

    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between two workshops
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())

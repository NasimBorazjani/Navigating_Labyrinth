
import heapq
import math


def a_star():
    # Define the city map as a 2D list
    city_map = [[0, 0, 0, 0, 9, 0, 14, 17, 0, 13, 3, 0, 13, 10, 18],
                [1, 0, 11, 12, 14, 13, 8, 0, 5, 7, 0, 0, 0, 0, 0],
                [3, 0, 0, 18, 11, 16, 0, 0, 0, 0, 1, 0, 15, 12, 10],
                [0, 10, 0, 3, 2, 15, 14, 0, 0, 0, 17, 0, 6, 1, 0],
                [8, 10, 0, 0, 0, 0, 1, 19, 6, 0, 17, 2, 0, 0, 0],
                [0, 6, 15, 2, 17, 2, 11, 5, 9, 0, 12, 15, 0, 0, 16],
                [0, 0, 8, 0, 14, 0, 13, 20, 17, 12, 19, 9, 0, 0, 0],
                [13, 10, 1, 4, 11, 3, 15, 0, 0, 3, 14, 20, 0, 6, 0],
                [0, 11, 16, 9, 19, 18, 12, 2, 0, 0, 1, 10, 0, 0, 0],
                [0, 13, 18, 18, 7, 0, 0, 0, 0, 18, 5, 6, 0, 7, 3],
                [0, 0, 0, 18, 6, 16, 10, 18, 9, 19, 0, 3, 5, 3, 4],
                [14, 18, 4, 1, 17, 0, 7, 0, 3, 16, 11, 0, 17, 11, 1],
                [0, 0, 12, 16, 0, 14, 9, 0, 0, 0, 13, 1, 0, 0, 19],
                [19, 0, 3, 0, 8, 0, 0, 0, 3, 0, 0, 0, 17, 9, 8],
                [15, 0, 2, 8, 9, 13, 0, 14, 0, 6, 0, 19, 0, 0, 5]]

    num_rows = 15
    num_cols = 15
    districts = {1: (0, 4), 2: (5, 9), 3: (10, 14)}
    start = (5, 2)
    end = (9, 13)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [city_map[i][j] for j in range(districts[d][0], districts[d][1] + 1)] for d in districts):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (current[0] + i, current[1] + j)
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and city_map[new_pos[0]][new_pos[1]] != 0:
                new_path = path + [new_pos]
                new_cost = g + city_map[new_pos[0]][new_pos[1]]

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_pos, end), new_cost, new_path, new_pos))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

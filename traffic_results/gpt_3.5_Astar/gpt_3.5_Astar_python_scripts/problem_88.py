
import heapq
import math

def a_star():
    # Define the city map as a 2D list
    city_map = [[0, 7, 0, 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, 0],
                [0, 6, 19, 17, 5, 13, 15, 2, 11, 5, 0, 0, 9, 8],
                [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, 0, 0, 12],
                [0, 1, 19, 20, 0, 3, 4, 18, 0, 0, 10, 1, 12, 2],
                [0, 1, 4, 1, 1, 10, 4, 0, 12, 0, 5, 10, 3, 8],
                [0, 0, 0, 7, 0, 0, 16, 12, 0, 0, 0, 13, 6, 10],
                [0, 0, 11, 12, 13, 15, 8, 0, 12, 1, 16, 14, 8, 15],
                [0, 11, 0, 15, 0, 0, 0, 0, 0, 0, 5, 0, 0, 14],
                [1, 0, 0, 8, 0, 13, 17, 0, 3, 12, 0, 0, 0, 0],
                [14, 3, 0, 4, 0, 0, 0, 12, 0, 7, 0, 0, 0, 0],
                [0, 5, 15, 0, 10, 17, 0, 0, 6, 9, 2, 0, 0, 0],
                [1, 7, 17, 1, 0, 0, 0, 0, 11, 0, 0, 0, 0, 12],
                [0, 0, 14, 18, 8, 19, 19, 16, 0, 6, 5, 16, 17, 7],
                [0, 0, 0, 0, 0, 0, 19, 17, 0, 0, 2, 12, 0, 0]]

    num_rows = 14
    num_cols = 14
    start = (3, 1)
    end = (5, 13)
    districts = [(0, 3), (4, 5), (6, 13)]

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
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set([pos for pos in new_path if pos[0] in range(districts[0][0], districts[0][1] + 1)])) >= 2:
                    if new_row in range(districts[1][0], districts[1][1] + 1) and len(set([pos for pos in new_path if pos[0] in range(districts[1][0], districts[1][1] + 1)])) >= 2:
                        if new_row in range(districts[2][0], districts[2][1] + 1) and len(set([pos for pos in new_path if pos[0] in range(districts[2][0], districts[2][1] + 1)])) >= 2:
                            if new_cost < visited_costs.get((new_row, new_col), math.inf):
                                visited_costs[(new_row, new_col)] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_row, new_col, end), new_cost, new_path, (new_row, new_col)))

    return None

def heuristic(row, col, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(row - end[0]) + abs(col - end[1])

print(a_star())


import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 0, 0, 9, 0, 20, 3, 9],
                [17, 11, 17, 0, 9, 2, 7, 0, 15],
                [0, 4, 2, 19, 12, 6, 0, 4, 17],
                [15, 0, 0, 15, 11, 19, 0, 9, 5],
                [3, 9, 19, 15, 2, 0, 0, 18, 0],
                [19, 5, 9, 11, 9, 0, 0, 3, 0],
                [0, 0, 2, 8, 8, 0, 0, 0, 19],
                [0, 0, 14, 0, 0, 0, 18, 0, 18],
                [0, 14, 18, 7, 8, 0, 10, 15, 0]]

    num_rows = 9
    num_cols = 9
    districts = {1: (0, 3), 2: (4, 4), 3: (5, 8)}
    start = (3, 7)
    end = (5, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get(district) for district in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 0:
                new_cost = g + city_map[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                new_district = get_district(new_row, districts)
                if new_district and (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_row, new_col, end), new_cost, new_path, (new_row, new_col)))

    return None


def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def get_district(row, districts):
    # Helper function to determine which district a given row belongs to
    for district, (start_row, end_row) in districts.items():
        if start_row <= row <= end_row:
            return district
    return None


print(a_star())

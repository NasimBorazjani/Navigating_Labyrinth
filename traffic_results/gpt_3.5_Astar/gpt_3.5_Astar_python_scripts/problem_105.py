
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[18, 15, 'x', 'x', 1, 'x', 'x', 5, 8, 18, 18, 2, 'x', 11, 8],
                ['x', 17, 'x', 'x', 2, 'x', 16, 9, 7, 13, 16, 17, 'x', 'x', 'x'],
                [10, 'x', 1, 14, 1, 10, 15, 4, 'x', 'x', 8, 11, 10, 'x', 'x'],
                [19, 'x', 'x', 9, 8, 18, 5, 2, 12, 'x', 13, 'x', 'x', 15, 11],
                [1, 'x', 14, 6, 6, 6, 'x', 'x', 'x', 13, 13, 'x', 'x', 'x', 'x'],
                [2, 3, 8, 5, 7, 'x', 'x', 'x', 19, 'x', 16, 'x', 'x', 'x', 'x'],
                ['x', 'x', 17, 18, 'x', 19, 'x', 'x', 'x', 7, 8, 17, 'x', 'x', 'x'],
                [4, 'x', 4, 14, 17, 6, 'x', 2, 'x', 'x', 15, 6, 'x', 18, 10],
                [7, 'x', 3, 11, 10, 'x', 'x', 12, 'x', 'x', 8, 'x', 'x', 10, 'x'],
                [4, 16, 2, 11, 'x', 'x', 14, 'x', 13, 'x', 'x', 'x', 'x', 'x', 'x'],
                [14, 20, 7, 14, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 10, 16, 'x'],
                [1, 14, 'x', 'x', 'x', 4, 14, 19, 'x', 18, 'x', 'x', 17, 15, 14],
                ['x', 'x', 15, 'x', 4, 5, 19, 18, 'x', 19, 11, 3, 12, 'x', 10],
                [1, 'x', 1, 'x', 'x', 13, 'x', 16, 4, 'x', 'x', 8, 'x', 9, 'x'],
                ['x', 'x', 12, 11, 7, 'x', 8, 14, 3, 'x', 11, 'x', 14, 13, 'x']]

    num_rows = 15
    num_cols = 15
    start = (1, 11)
    end = (7, 2)
    districts = [(0, 1), (2, 9), (10, 14)]

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(any(city_map[i][j] != 'x' for j in range(num_cols)) for i in range(num_rows)):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (current[0] + i, current[1] + j)
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and city_map[new_pos[0]][new_pos[1]] != 'x':
                new_path = path + [new_pos]
                new_cost = g + city_map[new_pos[0]][new_pos[1]]

                if all(new_pos not in district or any(city_map[i][j] != 'x' for j in range(num_cols) for i in range(district[0], district[1] + 1)) for district in districts) and (new_pos not in visited_costs or new_cost < visited_costs[new_pos]):
                    visited_costs[new_pos] = new_cost
                    h = heuristic(new_pos, end)
                    heapq.heappush(queue, (g + h, new_cost, new_path, new_pos))

    return None


def heuristic(current, end):
    # The heuristic is the Manhattan distance between the current position and the end position
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())

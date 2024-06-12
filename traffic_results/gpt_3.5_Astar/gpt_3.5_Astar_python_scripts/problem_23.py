
import heapq
import math

def a_star():
    # Define the city map as a 2D list
    city_map = [[math.inf, math.inf, math.inf, math.inf, math.inf, 8, math.inf, 15, 18, 10],
                [4, 5, 10, 6, 20, 2, 12, math.inf, math.inf, math.inf],
                [19, 6, 19, 7, 6, 2, math.inf, 15, math.inf, 14],
                [16, 17, math.inf, 2, 3, 7, 4, math.inf, 18, 6],
                [math.inf, 2, 1, 19, 7, 10, 18, 5, 3, 19],
                [8, 5, math.inf, 1, math.inf, 10, 17, math.inf, 13, 5],
                [18, 1, 3, 4, math.inf, math.inf, 8, math.inf, 5, math.inf],
                [15, math.inf, math.inf, 13, math.inf, 11, math.inf, 2, math.inf, math.inf],
                [4, math.inf, math.inf, 4, 1, math.inf, math.inf, math.inf, math.inf, math.inf],
                [math.inf, 10, 8, math.inf, math.inf, 7, 19, math.inf, math.inf, math.inf]]

    # Define the districts
    districts = {1: (0, 2), 2: (3, 4), 3: (5, 9)}

    # Define the start and end points
    start = (5, 8)
    end = (3, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = []
    heapq.heappush(queue, (0, 0, [start], start))

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(visited_costs[workshop] != math.inf for workshop in districts.values()):
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current[0] + i, current[1] + j
            if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != math.inf:
                new_cost = g + city_map[new_x][new_y]
                new_path = path + [(new_x, new_y)]
                new_district = get_district(new_x, new_y, districts)
                if new_cost < visited_costs.get((new_x, new_y), math.inf) and new_district:
                    visited_costs[(new_x, new_y)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_x, new_y, end), new_cost, new_path, (new_x, new_y)))

    return None

def heuristic(x, y, end):
    # A heuristic function that calculates the Manhattan distance from the current position to the end position
    return abs(x - end[0]) + abs(y - end[1])

def get_district(x, y, districts):
    # Check which district the current position belongs to
    for district, (start, end) in districts.items():
        if start <= x <= end:
            return district
    return None

print(a_star())

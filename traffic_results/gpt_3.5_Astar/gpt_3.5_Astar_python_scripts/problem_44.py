
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[math.inf, 16, 5, 13, math.inf, math.inf, 2, math.inf, 6, math.inf, math.inf],
                [math.inf, math.inf, 17, math.inf, 15, math.inf, 10, math.inf, 5, 17, math.inf],
                [math.inf, math.inf, math.inf, math.inf, 15, 3, 10, 2, 4, 13, 14],
                [math.inf, math.inf, math.inf, math.inf, 17, 2, 4, math.inf, 1, 4, 5],
                [2, math.inf, math.inf, 2, 6, 17, math.inf, math.inf, math.inf, 4, 19],
                [19, 5, math.inf, math.inf, math.inf, math.inf, 10, 12, 1, 18, 10],
                [math.inf, 3, math.inf, 12, math.inf, 10, 15, 11, math.inf, 4, 15],
                [2, math.inf, 11, 9, math.inf, 12, 11, math.inf, 15, 10, 6],
                [19, math.inf, 16, 5, math.inf, math.inf, math.inf, 11, math.inf, 11, 8],
                [12, 2, math.inf, 3, math.inf, 4, math.inf, math.inf, 15, math.inf, math.inf],
                [math.inf, math.inf, 18, 16, math.inf, math.inf, 4, math.inf, 12, 13, math.inf]]

    # Define the districts in the city
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 10)}

    # Define the start and end workshops
    start_workshop = (8, 10)
    end_workshop = (3, 4)

    visited_costs = {}
    visited_costs[start_workshop] = 0

    queue = [(0, 0, [start_workshop], start_workshop)]

    while queue:
        _, g, path, current_workshop = heapq.heappop(queue)

        # Check if Ben has visited at least one workshop in each district
        visited_districts = set()
        for workshop in path:
            for district, (start, end) in districts.items():
                if start <= workshop[0] <= end:
                    visited_districts.add(district)
                    break

        if len(visited_districts) == 3 and current_workshop == end_workshop:
            return path

        for neighbor in get_neighbors(current_workshop, city_map):
            new_path = path + [neighbor]
            new_cost = g + city_map[neighbor[0]][neighbor[1]]

            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                h = heuristic(neighbor, end_workshop)
                heapq.heappush(queue, (g + h, new_cost, new_path, neighbor))

    return None


def get_neighbors(workshop, city_map):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = workshop[0] + dx, workshop[1] + dy
        if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != 'x':
            neighbors.append((new_x, new_y))

    return neighbors


def heuristic(current_workshop, end_workshop):
    # Calculate the Manhattan distance between the current workshop and the end workshop
    return abs(current_workshop[0] - end_workshop[0]) + abs(current_workshop[1] - end_workshop[1])


print(a_star())

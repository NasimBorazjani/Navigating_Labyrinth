
from queue import PriorityQueue

def a_star_search(city_map, start, end):
    queue = PriorityQueue()
    queue.put((0, [start]))
    visited = set()

    while not queue.empty():
        cost, path = queue.get()
        current = path[-1]

        if current == end and has_visited_all_districts(path):
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in get_neighbors(city_map, current):
                if neighbor not in visited:
                    total_cost = cost + city_map[neighbor[0]][neighbor[1]]
                    queue.put((total_cost, path + [neighbor]))

    return None

def get_neighbors(city_map, workshop):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_workshop = (workshop[0] + dx, workshop[1] + dy)

        if (0 <= new_workshop[0] < len(city_map) and
            0 <= new_workshop[1] < len(city_map[0]) and
            city_map[new_workshop[0]][new_workshop[1]] != 'x'):
            neighbors.append(new_workshop)

    return neighbors

def has_visited_all_districts(path):
    districts = {1: False, 2: False, 3: False}

    for workshop in path:
        if 0 <= workshop[0] <= 5:
            districts[1] = True
        elif 6 <= workshop[0] <= 8:
            districts[2] = True
        elif 9 <= workshop[0] <= 14:
            districts[3] = True

    return all(districts.values())

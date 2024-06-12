
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
                total_cost = cost + city_map[neighbor[0]][neighbor[1]]
                new_path = list(path)
                new_path.append(neighbor)
                queue.put((total_cost, new_path))

    return None

def get_neighbors(city_map, workshop):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direction in directions:
        neighbor = (workshop[0] + direction[0], workshop[1] + direction[1])

        if (0 <= neighbor[0] < len(city_map) and
            0 <= neighbor[1] < len(city_map[0]) and
            city_map[neighbor[0]][neighbor[1]] != 'x'):
            neighbors.append(neighbor)

    return neighbors

def has_visited_all_districts(path):
    districts = set()

    for workshop in path:
        if 0 <= workshop[0] <= 3:
            districts.add(1)
        elif 4 <= workshop[0] <= 5:
            districts.add(2)
        elif 6 <= workshop[0] <= 12:
            districts.add(3)

    return len(districts) == 3

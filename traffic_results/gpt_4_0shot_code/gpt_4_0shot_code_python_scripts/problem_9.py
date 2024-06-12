
from queue import PriorityQueue

def a_star_search(city_map, start, end):
    queue = PriorityQueue()
    queue.put((0, [start], {get_district(start)}))
    visited = set()

    while not queue.empty():
        cost, path, districts = queue.get()
        current = path[-1]

        if current == end and len(districts) == 3:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in get_neighbors(city_map, current):
                if neighbor not in visited:
                    new_cost = cost + city_map[neighbor[0]][neighbor[1]]
                    new_path = path + [neighbor]
                    new_districts = districts | {get_district(neighbor)}
                    queue.put((new_cost, new_path, new_districts))

    return None

def get_neighbors(city_map, workshop):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        nx, ny = workshop[0] + dx, workshop[1] + dy

        if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
            neighbors.append((nx, ny))

    return neighbors

def get_district(workshop):
    if 0 <= workshop[0] <= 1:
        return 1
    elif 2 <= workshop[0] <= 4:
        return 2
    else:
        return 3

city_map = [
    [6, 9, 19, 'x', 5, 9, 'x', 15, 'x'],
    [8, 10, 16, 'x', 'x', 'x', 5, 11, 4],
    [5, 11, 20, 1, 14, 16, 7, 1, 5],
    [10, 5, 3, 5, 12, 8, 'x', 'x', 2],
    [16, 15, 15, 14, 'x', 13, 10, 'x', 10],
    [6, 4, 7, 13, 'x', 'x', 'x', 'x', 13],
    ['x', 1, 6, 3, 'x', 'x', 17, 9, 5],
    ['x', 11, 'x', 9, 'x', 5, 7, 'x', 'x'],
    ['x', 'x', 'x', 18, 'x', 2, 'x', 'x', 12]
]

start = (1, 8)
end = (4, 0)

print(a_star_search(city_map, start, end))

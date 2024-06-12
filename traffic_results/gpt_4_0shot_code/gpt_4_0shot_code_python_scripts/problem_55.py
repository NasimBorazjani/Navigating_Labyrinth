
from queue import PriorityQueue

def a_star_search(city_map, start, end):
    queue = PriorityQueue()
    queue.put((0, [start]))
    visited = set()
    while not queue.empty():
        (cost, path) = queue.get()
        current = path[-1]
        if current == end and visited_districts(path):
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in neighbors(city_map, current):
                total_cost = cost + city_map[neighbor[0]][neighbor[1]]
                new_path = list(path)
                new_path.append(neighbor)
                queue.put((total_cost, new_path))
    return None

def visited_districts(path):
    districts = set()
    for (x, y) in path:
        if x < 4:
            districts.add(1)
        elif x < 9:
            districts.add(2)
        else:
            districts.add(3)
    return len(districts) == 3

def neighbors(city_map, current):
    (x, y) = current
    results = [(nx, ny) for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x']
    return results

city_map = [[9, 4, 16, 7, 'x', 2, 'x', 'x', 14, 'x', 'x', 'x'], ['x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18], [12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7], [10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'], [11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7], ['x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20], ['x', 3, 17, 17, 'x', 'x', 18, 4, 'x', 'x', 9, 4], ['x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11], ['x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2], ['x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12], ['x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'], ['x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x']]
start = (3, 9)
end = (7, 1)
print(a_star_search(city_map, start, end))

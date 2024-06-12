
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

def neighbors(city_map, node):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if (0 <= neighbor[0] < len(city_map) and
            0 <= neighbor[1] < len(city_map[0]) and
            city_map[neighbor[0]][neighbor[1]] != 'x'):
            result.append(neighbor)
    return result

def visited_districts(path):
    districts = [0, 0, 0]
    for node in path:
        if 0 <= node[0] <= 4:
            districts[0] = 1
        elif 5 <= node[0] <= 9:
            districts[1] = 1
        elif 10 <= node[0] <= 14:
            districts[2] = 1
    return sum(districts) == 3

city_map = [
    ['x', 2, 16, 'x', 9, 'x', 14, 'x', 8, 'x', 16, 'x', 'x', 4, 8],
    [9, 'x', 4, 'x', 'x', 7, 11, 'x', 'x', 13, 'x', 'x', 6, 11, 'x'],
    ['x', 'x', 10, 14, 'x', 'x', 18, 'x', 'x', 'x', 'x', 'x', 6, 16, 'x'],
    ['x', 14, 'x', 1, 'x', 7, 5, 16, 'x', 19, 'x', 'x', 10, 7, 'x'],
    [1, 3, 'x', 19, 7, 2, 17, 'x', 'x', 6, 'x', 'x', 'x', 10, 14],
    [14, 'x', 'x', 'x', 12, 'x', 16, 5, 8, 12, 17, 2, 19, 'x', 5],
    [9, 9, 8, 15, 18, 'x', 16, 'x', 10, 'x', 'x', 14, 'x', 'x', 'x'],
    [18, 20, 'x', 'x', 11, 2, 17, 6, 'x', 18, 8, 'x', 6, 16, 'x'],
    [12, 'x', 'x', 'x', 'x', 7, 14, 4, 8, 12, 3, 'x', 15, 13, 2],
    [16, 'x', 'x', 'x', 12, 'x', 8, 1, 7, 7, 12, 17, 2, 2, 7],
    ['x', 13, 3, 3, 1, 'x', 6, 14, 20, 8, 'x', 4, 10, 17, 'x'],
    [1, 8, 'x', 16, 'x', 'x', 'x', 9, 'x', 'x', 10, 'x', 'x', 5, 8],
    ['x', 'x', 1, 'x', 'x', 6, 'x', 'x', 'x', 7, 16, 'x', 'x', 'x', 'x'],
    [14, 'x', 'x', 10, 18, 'x', 6, 13, 'x', 'x', 'x', 'x', 'x', 15, 'x'],
    ['x', 8, 2, 'x', 17, 'x', 12, 16, 11, 4, 4, 'x', 'x', 17, 'x']
]

start = (4, 0)
end = (9, 11)
print(a_star_search(city_map, start, end))

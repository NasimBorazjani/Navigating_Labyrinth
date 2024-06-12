
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
                queue.put((total_cost, path + [neighbor]))

    return None

def neighbors(city_map, workshop):
    (x, y) = workshop
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx >= 0 and ny >= 0 and nx < len(city_map) and ny < len(city_map[0]) and city_map[nx][ny] != 'x':
            result.append((nx, ny))

    return result

def visited_districts(path):
    districts = [0, 0, 0]

    for (x, y) in path:
        if x <= 1:
            districts[0] = 1
        elif x <= 9:
            districts[1] = 1
        else:
            districts[2] = 1

    return sum(districts) == 3

city_map = [
    [18, 15, 'x', 'x', 1, 'x', 'x', 5, 8, 18, 18, 2, 'x', 11, 8],
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
    ['x', 'x', 12, 11, 7, 'x', 8, 14, 3, 'x', 11, 'x', 14, 13, 'x']
]

start = (1, 11)
end = (7, 2)

print(a_star_search(city_map, start, end))

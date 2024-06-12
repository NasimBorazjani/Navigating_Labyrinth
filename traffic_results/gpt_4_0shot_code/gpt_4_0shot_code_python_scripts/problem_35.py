
from heapq import heappop, heappush

def shortest_path(city_map, start, end):
    rows, cols = len(city_map), len(city_map[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = [(0, start, [start])]
    while queue:
        cost, (x, y), path = heappop(queue)
        if (x, y) == end:
            return path
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and city_map[nx][ny] != 'x':
                new_cost = cost + city_map[nx][ny]
                new_path = path + [(nx, ny)]
                if valid_path(new_path):
                    heappush(queue, (new_cost, (nx, ny), new_path))
    return None

def valid_path(path):
    districts = set()
    for x, y in path:
        if x < 3:
            districts.add(1)
        elif x < 8:
            districts.add(2)
        else:
            districts.add(3)
    return len(districts) == 3

city_map = [
    ['x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'],
    ['x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2],
    ['x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'],
    [9, 3, 13, 8, 'x', 7, 'x', 'x', 4, 2, 'x'],
    [11, 17, 'x', 10, 'x', 'x', 'x', 'x', 17, 15, 11],
    ['x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7],
    ['x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9],
    [11, 'x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x'],
    ['x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7],
    [11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5],
    [9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10]
]

start = (7, 8)
end = (2, 1)
print(shortest_path(city_map, start, end))

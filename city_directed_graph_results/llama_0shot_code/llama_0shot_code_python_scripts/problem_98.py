
from collections import deque

def bfs(graph, start, destinations):
    matrix_to_city = {0: 'B', 1: 'X', 2: 'F', 3: 'Q', 4: 'V', 5: 'D', 6: 'A', 7: 'J', 8: 'N', 9: 'M', 10: 'G', 11: 'H', 12: 'K', 13: 'T', 14: 'S'}
    city_to_matrix = {'B': 0, 'X': 1, 'F': 2, 'Q': 3, 'V': 4, 'D': 5, 'A': 6, 'J': 7, 'N': 8, 'M': 9, 'G': 10, 'H': 11, 'K': 12, 'T': 13, 'S': 14}
    graph = {matrix_to_city[i]: [matrix_to_city[j] for j in range(len(graph[i])) if graph[i][j] == 1] for i in range(len(graph))}
    queue = deque([(start, [start], set())])
    visited = set()
    destinations_visited = {city: 0 for city in destinations}
    while queue:
        city, path, visited_cities = queue.popleft()
        if city in visited_cities:
            continue
        visited_cities.add(city)
        path = path + [city]
        if city in destinations_visited:
            destinations_visited[city] += 1
        if city == start or len(visited_cities) > 1 and all(visited_count == 2 for visited_count in destinations_visited.values()):
            return path
        for neighbor in graph[city]:
            if neighbor not in visited_cities or (neighbor in destinations and destinations_visited[neighbor] < 2):
                queue.append((neighbor, path, visited_cities))

destinations = ['J', 'X']
graph = [
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

print(bfs(graph, 'D', destinations))

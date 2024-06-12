
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 7, 'x', 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, 'x'],
    ['x', 6, 19, 17, 5, 13, 15, 2, 11, 5, 'x', 'x', 9, 8],
    [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, 'x', 'x', 12],
    ['x', 1, 19, 20, 'x', 3, 4, 18, 'x', 'x', 10, 1, 12, 2],
    ['x', 1, 4, 1, 1, 10, 4, 'x', 12, 'x', 5, 10, 3, 8],
    ['x', 'x', 'x', 7, 'x', 'x', 16, 12, 'x', 'x', 'x', 13, 6, 10],
    ['x', 'x', 11, 12, 13, 15, 8, 'x', 12, 1, 16, 14, 8, 15],
    ['x', 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 'x', 14],
    [1, 'x', 'x', 8, 'x', 13, 17, 'x', 3, 12, 'x', 'x', 'x', 'x'],
    [14, 3, 'x', 4, 'x', 'x', 'x', 12, 'x', 7, 'x', 'x', 'x', 'x'],
    ['x', 5, 15, 'x', 10, 17, 'x', 'x', 6, 9, 2, 'x', 'x', 'x'],
    [1, 7, 17, 1, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 12],
    ['x', 'x', 14, 18, 8, 19, 19, 16, 'x', 6, 5, 16, 17, 7],
    ['x', 'x', 'x', 'x', 'x', 'x', 19, 17, 'x', 'x', 2, 12, 'x', 'x']
]

# Convert 'x' to a large number to represent closed workshops
for i in range(len(city_map)):
    city_map[i] = [1000 if x == 'x' else x for x in city_map[i]]

# Convert the city map to a numpy array for easier manipulation
city_map = np.array(city_map)

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 5),
    3: (6, 13)
}

# Define the starting and destination workshops
start_workshop = (3, 1)
dest_workshop = (5, 13)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, dest):
    n = len(city_map)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min((dist[i], i) for i in range(n) if not visited[i])[1]
        visited[u] = True
        for v in range(n):
            if not visited[v] and city_map[u][v] != 1000 and dist[u] + city_map[u][v] < dist[v]:
                dist[v] = dist[u] + city_map[u][v]

    path = [dest]
    while dest != start:
        for i in range(n):
            if city_map[i][dest] != 1000 and dist[dest] == dist[i] + city_map[i][dest]:
                path.append(i)
                dest = i
                break

    return path[::-1]

# Find the shortest path from start to destination visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    district_path = dijkstra(city_map, start_workshop[0]*14 + start_workshop[1], district[0]*14)
    shortest_path += district_path
    start_workshop = (district[0]//14, district[0]%14)

shortest_path += dijkstra(city_map, start_workshop[0]*14 + start_workshop[1], dest_workshop[0]*14 + dest_workshop[1])

# Convert the indices to tuples
shortest_path = [(index//14, index%14) for index in shortest_path]

print(shortest_path)


import numpy as np

# Define the matrix map of the city
city_map = np.array([[16, 10, -1, 16, 1, 12, 6, 12, 3, 7, -1],
                      [-1, 16, 10, 9, 12, 19, 7, 10, 12, 13, 7],
                      [5, -1, 9, -1, 5, 16, 16, 8, -1, 16, 8],
                      [-1, 4, 14, -1, -1, -1, -1, -1, -1, 7, 18],
                      [13, 12, 16, 14, -1, 2, 4, 2, -1, 6, 3],
                      [-1, 11, 20, -1, -1, -1, 1, -1, -1, 9, -1],
                      [-1, -1, 8, 10, -1, -1, 3, 1, -1, -1, 6],
                      [-1, 2, 9, -1, 8, 13, -1, -1, -1, 12, 11],
                      [12, -1, 2, -1, -1, 1, 6, -1, 15, -1, 1],
                      [3, -1, -1, -1, 17, -1, 18, 4, 1, -1, -1],
                      [-1, -1, 6, -1, -1, 12, -1, -1, -1, 15, 12]])

# Define the districts
districts = {1: (0, 1), 2: (2, 4), 3: (5, 10)}

# Define the destination and starting workshops
destination = (5, 2)
start = (2, 10)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(range(len(graph)))
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    unvisited = nodes.copy()

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if current == end:
            path = []
            while prev[current] is not None:
                path.insert(0, current)
                current = prev[current]
            path.insert(0, start)
            return path

        for neighbor, weight in enumerate(graph[current]):
            if weight != -1:
                alt = dist[current] + weight
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current

    return None

# Find the shortest path from start to destination visiting at least one workshop in each district
path = []
for district in districts.values():
    district_path = dijkstra_shortest_path(city_map, start[0]*11 + start[1], end[0]*11 + end[1])
    path.extend(district_path)
    start = (district[1], district[1])

print([(p // 11, p % 11) for p in path])

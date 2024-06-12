
import numpy as np

# Define the matrix map of the city
city_map = np.array([
    [np.inf, np.inf, np.inf, 6, 9, np.inf, np.inf, 10, 14, 7, 3, 12],
    [np.inf, 11, np.inf, 3, 14, 16, 17, 1, 4, 14, 8, 16],
    [3, np.inf, np.inf, np.inf, 6, 1, 18, 16, np.inf, 6, 3, 11],
    [np.inf, np.inf, 11, 4, 8, np.inf, np.inf, 1, 3, 9, 8, 7],
    [np.inf, np.inf, 3, np.inf, np.inf, np.inf, 8, 14, 18, np.inf, np.inf, 18],
    [4, 1, np.inf, np.inf, np.inf, 14, np.inf, np.inf, np.inf, 3, 4, 20],
    [1, np.inf, np.inf, np.inf, 14, 19, 15, np.inf, np.inf, 3, 16, 15],
    [np.inf, np.inf, 6, 18, np.inf, np.inf, 16, 1, np.inf, 3, np.inf, 11],
    [np.inf, 3, np.inf, 15, np.inf, 19, 10, np.inf, np.inf, np.inf, np.inf, np.inf],
    [np.inf, 9, np.inf, np.inf, np.inf, np.inf, 17, 17, np.inf, 16, np.inf, 13],
    [np.inf, np.inf, 8, np.inf, np.inf, 1, np.inf, np.inf, np.inf, 19, 19, 1],
    [np.inf, 3, 9, np.inf, np.inf, np.inf, 1, np.inf, 10, 11, 8, np.inf]
])

# Define the districts
districts = {
    1: [0, 1],
    2: [2, 3, 4, 5],
    3: [6, 7, 8, 9, 10, 11]
}

# Define the start and end workshops
start_workshop = (1, 3)
end_workshop = (6, 10)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    n = len(graph)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = set()
    
    while len(visited) < n:
        u = min((v for v in range(n) if v not in visited), key=lambda x: dist[x])
        visited.add(u)
        
        for v in range(n):
            if graph[u][v] < np.inf:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    
    path = []
    u = end
    while u is not None:
        path.insert(0, u)
        u = prev[u]
    
    return path

# Find the shortest path from start to end workshop visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    for workshop in district:
        path1 = dijkstra_shortest_path(city_map, start_workshop[0]*12 + start_workshop[1], workshop)
        path2 = dijkstra_shortest_path(city_map, workshop, end_workshop[0]*12 + end_workshop[1])
        
        if path1 and path2:
            shortest_path = path1[:-1] + path2
    
print([(p // 12, p % 12) for p in shortest_path])

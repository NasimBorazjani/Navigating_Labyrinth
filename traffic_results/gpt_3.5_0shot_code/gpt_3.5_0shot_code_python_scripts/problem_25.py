
import numpy as np

# Define the matrix map of the city
city_map = np.array([
    [np.inf, np.inf, 6, np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf],
    [np.inf, 17, 13, 13, np.inf, 12, np.inf, 3, 10, 2],
    [np.inf, 5, 13, 15, 4, np.inf, np.inf, 20, 6, 2],
    [np.inf, 9, np.inf, 6, 2, 16, 18, 9, 13, np.inf],
    [np.inf, np.inf, 15, 17, np.inf, 10, 11, np.inf, np.inf, np.inf],
    [3, np.inf, 3, 17, 8, np.inf, 1, np.inf, 16, np.inf],
    [np.inf, np.inf, 13, 15, np.inf, np.inf, 11, np.inf, np.inf, 4],
    [np.inf, np.inf, 12, 1, np.inf, np.inf, np.inf, 14, 11, np.inf],
    [np.inf, 14, np.inf, np.inf, 19, 13, 4, np.inf, np.inf, np.inf],
    [1, np.inf, np.inf, 14, 11, 19, 2, 17, 2, 5]
])

# Define the districts
districts = {
    1: [0, 1, 2],
    2: [3, 4],
    3: [5, 6, 7, 8, 9]
}

# Define the start and end workshops
start_workshop = (2, 9)
end_workshop = (5, 2)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = city_map.shape[0]
    dist = np.full((n, n), np.inf)
    dist[start] = 0
    visited = set()
    
    while len(visited) < n * n:
        min_dist = np.inf
        min_node = None
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited and dist[i, j] < min_dist:
                    min_dist = dist[i, j]
                    min_node = (i, j)
        
        if min_node == end:
            break
        
        visited.add(min_node)
        
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = min_node[0] + i, min_node[1] + j
            if 0 <= new_i < n and 0 <= new_j < n and city_map[new_i, new_j] != np.inf:
                new_dist = dist[min_node] + city_map[new_i, new_j]
                if new_dist < dist[new_i, new_j]:
                    dist[new_i, new_j] = new_dist
    
    path = [end]
    current_node = end
    while current_node != start:
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = current_node[0] + i, current_node[1] + j
            if 0 <= new_i < n and 0 <= new_j < n and city_map[new_i, new_j] != np.inf:
                if dist[new_i, new_j] + city_map[current_node] == dist[current_node]:
                    path.append((new_i, new_j))
                    current_node = (new_i, new_j)
                    break
    
    return path[::-1]

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra(city_map, start_workshop, (workshop1 // 10, workshop1 % 10))
            path2 = dijkstra(city_map, (workshop1 // 10, workshop1 % 10), (workshop2 // 10, workshop2 % 10))
            path3 = dijkstra(city_map, (workshop2 // 10, workshop2 % 10), (workshop3 // 10, workshop3 % 10))
            path4 = dijkstra(city_map, (workshop3 // 10, workshop3 % 10), end_workshop)
            
            if shortest_path is None or len(path1) + len(path2) + len(path3) + len(path4) < len(shortest_path):
                shortest_path = path1 + path2[1:] + path3[1:] + path4

print(shortest_path)

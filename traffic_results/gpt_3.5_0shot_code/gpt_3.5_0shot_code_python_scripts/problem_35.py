
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[np.inf, 18, np.inf, 5, np.inf, 6, 5, np.inf, 6, 17, np.inf],
                      [np.inf, np.inf, 1, 5, 9, 13, np.inf, 2, np.inf, np.inf, 2],
                      [np.inf, 17, 12, np.inf, np.inf, np.inf, 5, np.inf, np.inf, 17, np.inf],
                      [9, 3, 13, 8, np.inf, 7, np.inf, np.inf, 4, 2, np.inf],
                      [11, 17, np.inf, 10, np.inf, np.inf, np.inf, np.inf, 17, 15, 11],
                      [np.inf, 10, 10, 14, 9, 7, 1, 5, np.inf, np.inf, 7],
                      [np.inf, 5, 6, 12, 8, 9, 4, np.inf, np.inf, 4, 9],
                      [11, np.inf, 4, 13, 14, np.inf, 12, 17, 13, np.inf, np.inf],
                      [np.inf, 8, np.inf, 19, 11, 7, 7, 19, 15, 14, 7],
                      [11, 8, np.inf, 11, 10, 16, np.inf, np.inf, 9, np.inf, 5],
                      [9, 4, np.inf, np.inf, 1, 11, 14, np.inf, np.inf, np.inf, 10]])

# Define the districts
districts = {1: range(3), 2: range(3, 8), 3: range(8, 11)}

# Define the starting and ending workshops
start = (7, 8)
end = (2, 1)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = city_map.shape[0]
    dist = np.full((n, n), np.inf)
    dist[start] = 0
    visited = set()
    path = {}

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
                    path[(new_i, new_j)] = min_node

    path_list = [end]
    while path_list[-1] != start:
        path_list.append(path[path_list[-1]])
    path_list.reverse()

    return path_list

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra(city_map, start, (workshop1, workshop1))
            path2 = dijkstra(city_map, (workshop1, workshop1), (workshop2, workshop2))
            path3 = dijkstra(city_map, (workshop2, workshop2), (workshop3, workshop3))
            if shortest_path is None or len(path1) + len(path2) + len(path3) < len(shortest_path):
                shortest_path = path1[:-1] + path2[:-1] + path3

print(shortest_path)

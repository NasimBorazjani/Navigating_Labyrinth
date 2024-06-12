
import numpy as np

# Define the matrix map of the city
city_map = np.array([[np.inf, np.inf, np.inf, 16, 1, 13, 17, 7, 14, np.inf],
                      [np.inf, 10, np.inf, 12, np.inf, 13, np.inf, 8, 19, 4],
                      [9, 13, np.inf, 13, np.inf, np.inf, 15, np.inf, np.inf, 16],
                      [3, 8, np.inf, 16, 12, np.inf, np.inf, np.inf, np.inf, 13],
                      [13, np.inf, 1, 15, 18, 8, np.inf, 10, np.inf, np.inf],
                      [8, 1, 2, 14, np.inf, 8, np.inf, 4, np.inf, 11],
                      [14, 13, 15, np.inf, 16, np.inf, 13, 2, np.inf, 19],
                      [np.inf, 4, 10, np.inf, np.inf, 16, np.inf, 11, np.inf, np.inf],
                      [np.inf, 14, np.inf, np.inf, np.inf, np.inf, np.inf, 18, 6, 18],
                      [np.inf, 3, 2, 6, 7, np.inf, np.inf, 9, 8, 5]])

# Define the districts
districts = {1: [0, 1, 2, 3], 2: [4, 5], 3: [6, 7, 8, 9]}

# Define the start and end workshops
start_workshop = (5, 1)
end_workshop = (3, 9)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = city_map.shape[0]
    dist = [np.inf] * n
    dist[start[0]*10 + start[1]] = 0
    visited = [False] * n

    for _ in range(n):
        u = min((i for i in range(n) if not visited[i]), key=lambda x: dist[x])
        visited[u] = True
        for v in range(n):
            if not visited[v] and city_map[u//10, u%10] != np.inf and city_map[v//10, v%10] != np.inf:
                new_dist = dist[u] + city_map[v//10, v%10]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    path = [end[0]*10 + end[1]]
    while path[-1] != start[0]*10 + start[1]:
        u = path[-1]
        for v in range(n):
            if city_map[u//10, u%10] != np.inf and city_map[v//10, v%10] != np.inf:
                if dist[u] == dist[v] + city_map[u//10, u%10]:
                    path.append(v)
                    break

    return [(p//10, p%10) for p in reversed(path)]

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra(city_map, start_workshop, (workshop1//10, workshop1%10))
            path2 = dijkstra(city_map, (workshop1//10, workshop1%10), (workshop2//10, workshop2%10))
            path3 = dijkstra(city_map, (workshop2//10, workshop2%10), (workshop3//10, workshop3%10))
            path4 = dijkstra(city_map, (workshop3//10, workshop3%10), end_workshop)
            if shortest_path is None or len(path1) + len(path2) + len(path3) + len(path4) < len(shortest_path):
                shortest_path = path1 + path2[1:] + path3[1:] + path4

print(shortest_path)

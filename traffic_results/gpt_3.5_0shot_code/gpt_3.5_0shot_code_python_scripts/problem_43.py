
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14],
    ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 'x'],
    [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15],
    ['x', 4, 'x', 'x', 18, 9, 'x', 15, 'x', 1, 9],
    [3, 2, 7, 'x', 'x', 17, 2, 14, 'x', 4, 2],
    [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7],
    ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4],
    ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'],
    ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'],
    ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'],
    ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]
]

# Convert 'x' to a large number to represent infinity
for i in range(len(city_map)):
    city_map[i] = [float('inf') if x == 'x' else x for x in city_map[i]]

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 5),
    3: (6, 10)
}

# Define the start and end workshops
start_workshop = (3, 10)
end_workshop = (6, 2)

# Define a function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    distances = np.full((len(city_map), len(city_map[0])), fill_value=float('inf'))
    distances[start[0]][start[1]] = 0
    visited = set()
    while True:
        min_distance = float('inf')
        min_node = None
        for i in range(len(city_map)):
            for j in range(len(city_map[0])):
                if (i, j) not in visited and distances[i][j] < min_distance:
                    min_distance = distances[i][j]
                    min_node = (i, j)
        if min_node is None:
            break
        visited.add(min_node)
        neighbors = [(min_node[0]+1, min_node[1]), (min_node[0]-1, min_node[1]), (min_node[0], min_node[1]+1), (min_node[0], min_node[1]-1)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(city_map) and 0 <= neighbor[1] < len(city_map[0]):
                new_distance = distances[min_node[0]][min_node[1]] + city_map[neighbor[0]][neighbor[1]]
                if new_distance < distances[neighbor[0]][neighbor[1]]:
                    distances[neighbor[0]][neighbor[1]] = new_distance
    path = [end]
    current = end
    while current != start:
        neighbors = [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(city_map) and 0 <= neighbor[1] < len(city_map[0]):
                if distances[neighbor[0]][neighbor[1]] + city_map[current[0]][current[1]] == distances[current[0]][current[1]]:
                    path.append(neighbor)
                    current = neighbor
                    break
    return path[::-1]

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = None
for district in districts.values():
    for i in range(district[0], district[1]+1):
        for j in range(len(city_map[0]):
            if city_map[i][j] != float('inf'):
                path = dijkstra(city_map, start_workshop, (i, j)) + dijkstra(city_map, (i, j), end_workshop)[1:]
                if shortest_path is None or sum(city_map[node[0]][node[1]] for node in path) < sum(city_map[node[0]][node[1]] for node in shortest_path):
                    shortest_path = path

print(shortest_path)

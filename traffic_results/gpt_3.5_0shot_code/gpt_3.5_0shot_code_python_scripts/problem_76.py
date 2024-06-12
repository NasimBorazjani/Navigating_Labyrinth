
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16],
    [2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12],
    ['x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x', 'x'],
    [2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x', 'x'],
    [19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17],
    ['x', 'x', 'x', 'x', 'x', 1, 'x', 'x', 4, 'x', 'x', 'x', 8, 19],
    [6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 3, 2, 'x'],
    [19, 'x', 3, 11, 'x', 6, 11, 'x', 12, 14, 10, 'x', 11, 18],
    [13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 'x', 10, 5],
    [19, 'x', 'x', 16, 'x', 'x', 18, 'x', 8, 'x', 2, 11, 'x', 12],
    ['x', 14, 'x', 6, 'x', 18, 'x', 11, 'x', 'x', 14, 11, 2, 'x'],
    ['x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x', 19],
    ['x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 19, 'x', 5, 'x'],
    [8, 'x', 17, 'x', 'x', 5, 15, 'x', 'x', 16, 1, 'x', 'x', 17]
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 7),
    3: (8, 13)
}

# Define the start and end workshops
start_workshop = (4, 3)
end_workshop = (8, 13)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    rows, cols = len(city_map), len(city_map[0])
    distances = np.full((rows, cols), np.inf)
    distances[start[0]][start[1]] = 0
    visited = set()
    path = {}

    while len(visited) < rows * cols:
        min_dist = np.inf
        current = None
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and distances[i][j] < min_dist:
                    min_dist = distances[i][j]
                    current = (i, j)

        if current == end:
            break

        visited.add(current)

        neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), 
                     (current[0], current[1] + 1), (current[0], current[1] - 1)]
        
        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and city_map[neighbor[0]][neighbor[1]] != 'x':
                new_dist = distances[current[0]][current[1]] + city_map[neighbor[0]][neighbor[1]]
                if new_dist < distances[neighbor[0]][neighbor[1]]:
                    distances[neighbor[0]][neighbor[1]] = new_dist
                    path[neighbor] = current

    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

# Find the shortest path that satisfies the conditions
final_path = []
for district in districts.values():
    path = dijkstra(city_map, start_workshop, end_workshop)
    final_path.extend(path)
    start_workshop = path[-1]

print(final_path)

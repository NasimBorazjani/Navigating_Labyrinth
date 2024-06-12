
import numpy as np

# Define the matrix map of the city
city_map = [
    [14, 'x', 11, 'x', 'x', 8, 15, 17, 18, 'x', 11],
    [13, 9, 2, 7, 9, 12, 7, 'x', 'x', 'x', 12],
    ['x', 2, 8, 13, 5, 'x', 'x', 7, 18, 'x', 'x'],
    [19, 6, 1, 6, 19, 13, 14, 'x', 'x', 17, 'x'],
    ['x', 9, 6, 'x', 'x', 14, 10, 'x', 'x', 5, 'x'],
    [12, 'x', 'x', 'x', 7, 17, 11, 'x', 'x', 1, 'x'],
    ['x', 16, 'x', 2, 11, 15, 6, 'x', 14, 14, 4],
    ['x', 15, 14, 11, 'x', 17, 20, 18, 4, 16, 8],
    ['x', 3, 6, 4, 1, 5, 'x', 'x', 3, 7, 9],
    [18, 14, 3, 4, 'x', 'x', 'x', 12, 15, 10, 'x'],
    ['x', 8, 'x', 1, 18, 'x', 'x', 'x', 'x', 'x', 'x']
]

# Define the districts
districts = {
    1: [0, 1, 2, 3],
    2: [4, 5],
    3: [6, 7, 8, 9, 10]
}

# Define the start and end workshops
start_workshop = (6, 10)
end_workshop = (3, 2)

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

        neighbors = [(current[0]-1, current[1]), (current[0]+1, current[1]), 
                     (current[0], current[1]-1), (current[0], current[1]+1)]
        
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
    for workshop in district:
        path = dijkstra(city_map, start_workshop, (workshop // len(city_map[0]), workshop % len(city_map[0]))
        if path[-1] == (workshop // len(city_map[0]), workshop % len(city_map[0]):
            final_path.extend(path)

final_path.extend(dijkstra(city_map, final_path[-1], end_workshop))

print(final_path)

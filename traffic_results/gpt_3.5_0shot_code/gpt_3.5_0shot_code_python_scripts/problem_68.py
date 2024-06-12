
from collections import deque

# Define the city map
city_map = [
    [18, 'x', 'x', 'x', 19, 'x', 'x', 8, 6, 3, 'x', 'x', 'x'],
    ['x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 4, 6, 4],
    [1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'],
    [3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 10, 'x', 'x'],
    [17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'],
    ['x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10],
    [16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'],
    [5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 8, 'x', 1],
    [10, 'x', 1, 'x', 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 'x', 12, 13, 'x'],
    ['x', 'x', 18, 14, 'x', 'x', 5, 'x', 'x', 13, 1, 'x', 'x'],
    ['x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'],
    ['x', 'x', 'x', 16, 1, 'x', 19, 'x', 'x', 'x', 'x', 14, 'x']
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (1, 3), (1, 4)],
    2: [(2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)],
    3: [(5, 0), (5, 1), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 0), (7, 1), (7, 2), (7, 3), (8, 0), (8, 1), (8, 2), (8, 3), (9, 4), (9, 5), (10, 2), (10, 3), (10, 4), (10, 5), (11, 2), (11, 3), (11, 4), (12, 2), (12, 3), (12, 5)]
}

# Define the start and end workshops
start_workshop = (5, 12)
end_workshop = (1, 2)

# Perform breadth-first search
def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None

# Get valid neighbors for a given workshop
def get_neighbors(workshop):
    row, col = workshop
    neighbors = []

    if row > 0 and city_map[row - 1][col] != 'x':
        neighbors.append((row - 1, col))
    if row < len(city_map) - 1 and city_map[row + 1][col] != 'x':
        neighbors.append((row + 1, col))
    if col > 0 and city_map[row][col - 1] != 'x':
        neighbors.append((row, col - 1))
    if col < len(city_map[0]) - 1 and city_map[row][col + 1] != 'x':
        neighbors.append((row, col + 1))

    return neighbors

# Find the shortest path while visiting at least one workshop in each district
path = None
for district in districts.values():
    for workshop in district:
        temp_path = bfs(start_workshop, workshop)
        if temp_path:
            remaining_districts = set(districts.keys()) - set([key for key, value in districts.items() if workshop in value])
            for remaining_district in remaining_districts:
                for remaining_workshop in districts[remaining_district]:
                    end_path = bfs(workshop, remaining_workshop)
                    if end_path:
                        temp_path += end_path[1:]
                        if not path or len(temp_path) < len(path):
                            path = temp_path

# Print the shortest path
print(path)


from collections import deque

# Define the matrix map of the city
city_map = [
    [None, None, 8, 16, 3, None, 15, 17, 2, None, None, 5, None, None],
    [None, None, 17, None, 13, None, 4, None, 13, 3, 3, 6, 11, None],
    [None, None, 8, None, 14, 1, 15, 11, None, 18, 12, None, None, None],
    [13, 19, 4, 13, 2, 13, 3, None, 1, 20, 18, None, 15],
    [13, None, 1, None, 11, None, 8, 14, 4, 11, 3, None, None, None],
    [12, 11, 16, 1, 1, None, 5, 1, None, 9, None, None, 1, None],
    [8, None, 6, 15, None, 7, 19, 13, 2, None, 3, 3, None, 2],
    [18, None, 19, 15, 2, None, None, 18, 2, None, 10, None, None, 1],
    [3, 4, None, 19, None, 6, None, 7, None, None, None, None, 15, None],
    [None, None, None, 16, 7, 17, 11, None, 7, None, None, None, None, 15],
    [None, 9, None, None, None, 19, 19, 7, 3, 12, 14, 11, 16, 7],
    [8, 19, 15, 1, None, 14, None, 1, None, None, None, None, None, None],
    [None, 14, None, None, None, None, None, 18, None, None, 2, 11, 7, None],
    [None, None, None, None, None, 3, 11, 12, None, None, None, 2, 6, None]
]

# Define the districts
districts = {
    1: (0, 1),
    2: (2, 6),
    3: (7, 13)
}

# Define the start and end workshops
start_workshop = (1, 10)
end_workshop = (7, 2)

# Perform breadth-first search to find the shortest path
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

# Get neighboring workshops that Ben can travel to
def get_neighbors(workshop):
    row, col = workshop
    neighbors = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < len(city_map) and 0 <= new_col < len(city_map[0]) and city_map[new_row][new_col] is not None:
            neighbors.append((new_row, new_col))

    return neighbors

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for workshop in district:
        path = bfs(start_workshop, workshop)

        if path:
            remaining_districts = set(districts.keys()) - set([k for k, v in districts.items() if workshop in v])

            for remaining_district in remaining_districts:
                for remaining_workshop in districts[remaining_district]:
                    new_path = bfs(workshop, remaining_workshop)

                    if new_path:
                        path += new_path

                        if bfs(remaining_workshop, end_workshop):
                            if shortest_path is None or len(path) < len(shortest_path):
                                shortest_path = path

# Print the shortest path
print(shortest_path)

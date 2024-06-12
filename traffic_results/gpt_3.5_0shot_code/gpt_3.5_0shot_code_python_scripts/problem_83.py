
from collections import deque

# Define the matrix map of the city
city_map = [
    [None, None, 14, None, 3, None, 18, None, 4, 4, None, None, 16, None],
    [None, None, 1, 15, None, 18, None, 18, None, None, None, None, 14, None],
    [None, None, 7, 14, None, None, 16, None, None, None, None, 5, 19, 15],
    [None, 13, 18, None, 17, None, 6, 8, None, 8, None, None, 13, None],
    [12, None, 15, None, None, None, None, 18, None, None, None, 8, 6, 7],
    [5, 11, 14, 14, 11, 5, 13, 7, None, None, 10, 12, 17, 17],
    [14, None, 3, 15, 3, None, None, 17, 12, 7, 19, 15, 4, 5],
    [None, 2, 14, None, 8, None, 9, 19, 16, 14, 17, 12, None, 13],
    [None, None, 2, 15, None, None, None, 2, 14, 17, 3, 4, None, 12],
    [2, None, 11, None, None, 14, None, None, 16, None, 11, 13, None, None],
    [17, None, None, 2, 9, 14, 8, None, 11, 5, None, 10, 5, None],
    [4, None, 8, 8, 11, None, 16, None, None, None, 15, None, 2, 16],
    [None, 16, None, None, 9, None, None, None, None, 19, 6, 9, None, None],
    [None, 14, 9, None, 6, 1, 7, None, 10, 4, None, None, None, None]
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 5),
    3: (6, 13)
}

# Define the start and end workshops
start_workshop = (2, 13)
end_workshop = (5, 1)

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
    for i in range(district[0], district[1] + 1):
        path_to_district = bfs(start_workshop, (i, 0))
        if path_to_district:
            remaining_path = bfs((i, 0), end_workshop)
            if remaining_path:
                shortest_path = path_to_district + remaining_path
                break
    if shortest_path:
        break

print(shortest_path)

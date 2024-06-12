
from collections import deque

# Define the city map as a 2D list
city_map = [
    [16, 'x', 5, 6, 'x', 14, 12, 'x', 'x', 'x', 6, 'x'],
    [17, 'x', 'x', 'x', 5, 'x', 5, 7, 'x', 'x', 8, 'x'],
    [3, 19, 'x', 'x', 'x', 'x', 18, 'x', 13, 7, 'x', 'x'],
    [13, 'x', 4, 'x', 'x', 8, 7, 4, 'x', 15, 'x', 'x'],
    [5, 17, 18, 12, 3, 'x', 14, 2, 4, 18, 'x', 1],
    [4, 10, 1, 19, 10, 'x', 'x', 17, 'x', 17, 16, 4],
    [7, 'x', 16, 'x', 'x', 1, 3, 'x', 13, 13, 'x', 'x'],
    ['x', 'x', 9, 1, 7, 18, 16, 3, 'x', 4, 'x', 'x'],
    [2, 'x', 13, 10, 'x', 4, 'x', 'x', 'x', 'x', 12],
    ['x', 'x', 'x', 18, 8, 4, 'x', 11, 'x', 14, 18, 'x'],
    ['x', 19, 2, 'x', 2, 6, 5, 18, 'x', 5, 'x', 'x'],
    ['x', 2, 'x', 7, 'x', 'x', 8, 7, 'x', 11, 16, 'x']
]

# Define the districts
districts = {
    1: [(0, 0), (3, 11)],
    2: [(4, 0), (8, 11)],
    3: [(9, 0), (11, 11)]
}

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to check if a position is valid
def is_valid_position(pos):
    x, y = pos
    return 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x'

# Function to find the shortest path using breadth-first search
def find_shortest_path(start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for dx, dy in directions:
            new_pos = (current[0] + dx, current[1] + dy)

            if is_valid_position(new_pos) and new_pos not in visited:
                new_path = path + [new_pos]
                queue.append((new_pos, new_path))
                visited.add(new_pos)

    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for start in district:
        for end in district:
            if start != end:
                path = find_shortest_path(start, end)
                if path and (not shortest_path or len(path) < len(shortest_path)):
                    shortest_path = path

# Print the shortest path
print(shortest_path)

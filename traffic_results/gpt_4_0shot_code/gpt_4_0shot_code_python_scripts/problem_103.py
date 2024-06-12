
from collections import deque

# Define the city map
city_map = [
    [6, 6, 2, 'x', 13, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 3, 'x'],
    [6, 11, 'x', 14, 'x', 'x', 'x', 1, 5, 6, 1, 19, 2, 7, 14],
    [16, 4, 12, 13, 17, 4, 'x', 'x', 'x', 14, 'x', 'x', 9, 9, 13],
    ['x', 11, 6, 14, 'x', 16, 'x', 1, 10, 18, 11, 'x', 'x', 13, 'x'],
    ['x', 'x', 14, 4, 19, 1, 2, 16, 15, 'x', 15, 'x', 'x', 'x', 'x'],
    [13, 6, 16, 13, 5, 9, 'x', 6, 10, 3, 1, 14, 'x', 17, 'x'],
    ['x', 'x', 19, 8, 'x', 2, 4, 'x', 'x', 4, 9, 13, 13, 11, 5],
    ['x', 11, 17, 19, 11, 18, 'x', 8, 'x', 'x', 17, 17, 13, 9, 15],
    [11, 4, 'x', 3, 3, 8, 5, 'x', 'x', 'x', 20, 19, 'x', 'x', 12],
    [2, 'x', 'x', 'x', 'x', 16, 7, 13, 4, 'x', 7, 16, 'x', 5, 1],
    [14, 9, 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 14, 20, 11, 16, 'x'],
    [3, 'x', 1, 'x', 13, 'x', 9, 'x', 15, 19, 4, 'x', 'x', 'x', 2],
    ['x', 8, 'x', 'x', 'x', 6, 'x', 16, 'x', 'x', 'x', 'x', 2, 17, 18],
    ['x', 'x', 11, 'x', 'x', 14, 6, 'x', 15, 'x', 'x', 18, 'x', 'x', 'x'],
    [8, 'x', 5, 1, 7, 14, 'x', 'x', 'x', 'x', 14, 7, 'x', 8, 'x']
]

# Define the start and end points
start = (2, 0)
end = (6, 14)

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define the BFS function
def bfs(start, end, city_map):
    queue = deque([start])
    visited = {start: None}
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for direction in directions:
            next_node = (node[0] + direction[0], node[1] + direction[1])
            if (0 <= next_node[0] < len(city_map) and
                0 <= next_node[1] < len(city_map[0]) and
                city_map[next_node[0]][next_node[1]] != 'x' and
                next_node not in visited):
                queue.append(next_node)
                visited[next_node] = node
    return None

# Print the quickest route
print(bfs(start, end, city_map))

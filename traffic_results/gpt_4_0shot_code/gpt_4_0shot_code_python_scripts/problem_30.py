
from queue import PriorityQueue

# Define the city map
city_map = [
    [8, 'x', 'x', 9, 15, 13, 11, 2, 'x', 'x'],
    [13, 'x', 'x', 'x', 5, 'x', 'x', 7, 'x', 'x'],
    [12, 3, 'x', 'x', 'x', 'x', 'x', 10, 'x', 'x'],
    [12, 'x', 'x', 9, 15, 9, 11, 5, 17, 'x'],
    [3, 5, 12, 'x', 11, 5, 'x', 15, 1, 18],
    [14, 3, 'x', 'x', 18, 14, 19, 19, 12, 15],
    ['x', 20, 17, 15, 11, 'x', 'x', 'x', 'x', 'x'],
    [12, 13, 18, 'x', 'x', 5, 'x', 2, 'x', 13],
    ['x', 'x', 13, 19, 4, 'x', 12, 'x', 'x', 8],
    ['x', 'x', 10, 'x', 'x', 'x', 15, 'x', 4, 16]
]

# Define the start and end points
start = (4, 9)
end = (6, 1)

# Define the directions that Ben can move in
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define a priority queue for the paths
queue = PriorityQueue()
queue.put((0, [start]))

# Define a set to keep track of visited nodes
visited = set()

while not queue.empty():
    # Get the path with the lowest cost from the queue
    cost, path = queue.get()

    # Get the last node in the path
    node = path[-1]

    # If the node has been visited, skip it
    if node in visited:
        continue

    # If the node is the end point and the path has visited a workshop in each district, return the path
    if node == end and {1, 2, 3}.issubset({1 if 0 <= i <= 3 else 2 if 4 <= i <= 5 else 3 for i, j in path}):
        print(path)
        break

    # Mark the node as visited
    visited.add(node)

    # Add the neighboring nodes to the queue
    for dx, dy in directions:
        x, y = node
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and city_map[nx][ny] != 'x':
            queue.put((cost + city_map[nx][ny], path + [(nx, ny)]))

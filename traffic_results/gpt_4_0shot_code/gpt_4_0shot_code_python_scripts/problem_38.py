
from queue import PriorityQueue

# Define the city map
city_map = [
    ['x', 'x', 'x', 3, 'x', 'x', 16, 'x', 2, 16, 3],
    [8, 'x', 8, 5, 'x', 'x', 10, 'x', 19, 4, 'x'],
    ['x', 'x', 18, 1, 16, 'x', 9, 15, 'x', 'x', 11],
    ['x', 'x', 17, 16, 4, 19, 2, 'x', 1, 11, 'x'],
    [9, 'x', 5, 16, 18, 'x', 'x', 7, 'x', 18, 6],
    ['x', 15, 7, 'x', 'x', 'x', 19, 8, 9, 17, 'x'],
    ['x', 15, 19, 'x', 'x', 'x', 6, 2, 6, 'x', 5],
    ['x', 12, 11, 3, 11, 4, 'x', 'x', 'x', 3, 'x'],
    [18, 12, 4, 'x', 3, 10, 'x', 3, 'x', 7, 14],
    [15, 11, 12, 'x', 13, 2, 'x', 'x', 5, 14, 'x'],
    ['x', 'x', 15, 'x', 16, 4, 10, 13, 'x', 'x', 4]
]

# Define the start and end points
start = (3, 6)
end = (8, 0)

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

    # Mark the node as visited
    visited.add(node)

    # If the node is the end point, return the path
    if node == end and all(any(0 <= workshop[0] < 4 for workshop in path),
                            any(4 <= workshop[0] < 8 for workshop in path),
                            any(8 <= workshop[0] < 11 for workshop in path)):
        print(path)
        break

    # Add the neighboring nodes to the queue
    for direction in directions:
        next_node = (node[0] + direction[0], node[1] + direction[1])

        # If the next node is within the city map and is not a closed workshop, add it to the queue
        if (0 <= next_node[0] < len(city_map) and
                0 <= next_node[1] < len(city_map[0]) and
                city_map[next_node[0]][next_node[1]] != 'x'):
            next_cost = cost + city_map[next_node[0]][next_node[1]]
            queue.put((next_cost, path + [next_node]))

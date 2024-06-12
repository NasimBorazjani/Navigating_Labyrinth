
from queue import PriorityQueue

# Define the city map
city_map = [
    ['x', 14, 15, 10, 'x', 14, 'x', 'x', 18, 6, 'x', 'x', 4],
    [6, 'x', 'x', 'x', 1, 'x', 15, 'x', 'x', 2, 'x', 17, 'x'],
    ['x', 4, 'x', 17, 3, 14, 4, 2, 'x', 3, 'x', 11, 'x'],
    [6, 6, 'x', 19, 'x', 13, 'x', 11, 13, 6, 3, 'x', 'x'],
    [3, 10, 11, 'x', 'x', 4, 4, 1, 19, 'x', 'x', 'x', 17],
    [8, 'x', 'x', 8, 11, 18, 17, 19, 18, 'x', 1, 1, 'x'],
    [14, 14, 1, 19, 6, 'x', 19, 19, 18, 9, 'x', 12, 18],
    [17, 6, 8, 'x', 1, 14, 19, 13, 'x', 'x', 9, 'x', 3],
    [16, 4, 'x', 'x', 'x', 9, 5, 'x', 'x', 'x', 18, 'x', 'x'],
    ['x', 'x', 10, 'x', 18, 'x', 1, 'x', 'x', 12, 9, 8, 3],
    ['x', 13, 17, 'x', 'x', 'x', 5, 8, 1, 'x', 1, 10, 'x'],
    [10, 11, 'x', 12, 'x', 6, 11, 'x', 9, 9, 15, 'x', 10],
    [5, 15, 1, 'x', 8, 5, 'x', 6, 'x', 9, 18, 'x', 'x']
]

# Define the start and end points
start = (3, 8)
end = (8, 0)

# Define the directions that Ben can move in
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define a priority queue for the paths
queue = PriorityQueue()
queue.put((0, [start]))

# Define a set to keep track of visited nodes
visited = set()

# Run the A* search algorithm
while not queue.empty():
    # Get the path with the lowest cost from the queue
    cost, path = queue.get()

    # Get the last node in the path
    node = path[-1]

    # If the node has been visited, skip it
    if node in visited:
        continue

    # If the node is the end point and the path has visited a workshop in each district, return the path
    if node == end and all(any(0 <= workshop[0] <= 3 for workshop in path),
                            any(4 <= workshop[0] <= 7 for workshop in path),
                            any(8 <= workshop[0] <= 12 for workshop in path)):
        print(path)
        break

    # Mark the node as visited
    visited.add(node)

    # Add the neighboring nodes to the queue
    for direction in directions:
        next_node = (node[0] + direction[0], node[1] + direction[1])
        if (0 <= next_node[0] < len(city_map) and 0 <= next_node[1] < len(city_map[0]) and
                city_map[next_node[0]][next_node[1]] != 'x'):
            next_cost = cost + city_map[next_node[0]][next_node[1]]
            queue.put((next_cost, path + [next_node]))


from queue import PriorityQueue

# Define the city map
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

# Define the start and end points
start = (6, 10)
end = (3, 2)

# Define the districts
districts = [(0, 3), (4, 5), (6, 10)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts):
    # Define the priority queue
    queue = PriorityQueue()
    queue.put((0, [start]))

    # Define the set of visited nodes
    visited = set()

    # While the queue is not empty
    while not queue.empty():
        # Get the path with the lowest cost
        cost, path = queue.get()

        # Get the last node in the path
        node = path[-1]

        # If the node has been visited, skip it
        if node in visited:
            continue

        # If the node is the end node, return the path
        if node == end and all(any(d[0] <= workshop[0] <= d[1] for workshop in path) for d in districts):
            return path

        # Mark the node as visited
        visited.add(node)

        # Get the neighbors of the node
        neighbors = [(node[0] + dx, node[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        # For each neighbor
        for neighbor in neighbors:
            # If the neighbor is within the city map and is not a closed workshop
            if 0 <= neighbor[0] < len(city_map) and 0 <= neighbor[1] < len(city_map[0]) and city_map[neighbor[0]][neighbor[1]] != 'x':
                # Add the neighbor to the queue with the cost of the path plus the cost to the neighbor
                queue.put((cost + city_map[neighbor[0]][neighbor[1]], path + [neighbor]))

# Print the shortest path
print(a_star_search(start, end, city_map, districts))

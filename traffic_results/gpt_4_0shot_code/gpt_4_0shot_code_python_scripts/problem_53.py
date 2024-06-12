
from queue import PriorityQueue

# Define the city map
city_map = [
    [18, 'x', 'x', 14, 5, 'x', 'x', 5, 18, 'x', 3, 'x'],
    ['x', 'x', 'x', 9, 2, 2, 'x', 15, 14, 12, 'x', 18],
    ['x', 'x', 3, 16, 3, 9, 'x', 16, 'x', 14, 'x', 17],
    ['x', 'x', 'x', 19, 7, 20, 'x', 'x', 11, 4, 'x', 4],
    [7, 'x', 8, 11, 'x', 1, 15, 5, 'x', 'x', 11, 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 6, 11, 'x', 'x', 'x', 8],
    ['x', 15, 2, 'x', 'x', 18, 'x', 1, 16, 15, 6, 5],
    ['x', 4, 18, 8, 9, 'x', 'x', 17, 20, 13, 'x', 10],
    ['x', 16, 'x', 'x', 19, 'x', 17, 'x', 13, 11, 14, 2],
    [12, 'x', 11, 'x', 3, 'x', 5, 3, 'x', 13, 17, 6],
    [14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 16],
    [12, 'x', 'x', 'x', 12, 'x', 10, 'x', 18, 14, 8, 'x']
]

# Define the start and end points
start = (3, 3)
end = (7, 11)

# Define the districts
districts = [(0, 3), (4, 6), (7, 11)]

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

        # For each neighbor of the node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = node
            nx, ny = x + dx, y + dy

            # If the neighbor is within the city map and is not a closed workshop
            if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                # Add the neighbor to the queue with the cost of the path plus the cost to the neighbor
                queue.put((cost + city_map[nx][ny], path + [(nx, ny)]))

    # If no path is found, return None
    return None

# Print the shortest path
print(a_star_search(start, end, city_map, districts))

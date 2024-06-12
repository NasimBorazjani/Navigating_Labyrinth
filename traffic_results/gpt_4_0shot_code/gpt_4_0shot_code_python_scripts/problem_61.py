
from queue import PriorityQueue

# Define the city map
city_map = [
    [13, 13, 16, 8, 'x', 19, 1, 18, 13, 8, 'x', 7, 'x'],
    ['x', 13, 'x', 15, 'x', 12, 20, 1, 13, 19, 4, 17, 'x'],
    ['x', 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8],
    ['x', 12, 18, 19, 'x', 7, 'x', 12, 3, 2, 'x', 16, 11],
    ['x', 7, 'x', 'x', 8, 13, 15, 3, 1, 'x', 15, 15, 'x'],
    [11, 9, 'x', 16, 2, 10, 1, 2, 16, 1, 'x', 10, 12],
    ['x', 'x', 9, 9, 7, 'x', 6, 'x', 'x', 10, 7, 2, 'x'],
    ['x', 13, 10, 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [11, 14, 'x', 'x', 'x', 'x', 4, 8, 'x', 'x', 18, 'x', 'x'],
    [13, 14, 'x', 10, 'x', 'x', 16, 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 16, 'x', 10, 'x', 17, 'x', 12, 'x', 10, 'x', 5],
    [9, 'x', 10, 'x', 19, 16, 'x', 14, 16, 12, 15, 7, 'x'],
    [1, 'x', 8, 10, 14, 'x', 6, 9, 'x', 'x', 8, 11, 11]
]

# Define the start and end points
start = (3, 12)
end = (6, 2)

# Define the districts
districts = [(0, 1), (2, 5), (6, 12)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts):
    # Initialize the priority queue
    queue = PriorityQueue()
    queue.put((0, [start]))

    # While the queue is not empty
    while not queue.empty():
        # Get the path with the lowest cost
        cost, path = queue.get()

        # Get the last node in the path
        node = path[-1]

        # If the node is the end point
        if node == end:
            # If the path visits at least one workshop in each district
            if all(any(d[0] <= workshop[0] <= d[1] for workshop in path) for d in districts):
                # Return the path
                return path

        # For each neighbor of the node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Calculate the new coordinates
            x, y = node[0] + dx, node[1] + dy

            # If the new coordinates are valid
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x':
                # Add the new path to the queue
                queue.put((cost + city_map[x][y], path + [(x, y)]))

# Print the result
print(a_star_search(start, end, city_map, districts))

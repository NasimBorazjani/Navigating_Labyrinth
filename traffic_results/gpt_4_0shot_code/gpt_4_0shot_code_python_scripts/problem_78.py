
from queue import PriorityQueue

# Define the city map
city_map = [
    ['x', 'x', 'x', 16, 11, 12, 'x', 'x', 17, 3, 'x', 'x', 4, 6],
    [4, 17, 'x', 'x', 3, 'x', 'x', 1, 9, 11, 12, 4, 'x', 'x'],
    [5, 'x', 'x', 7, 14, 4, 5, 7, 13, 4, 7, 'x', 'x', 'x'],
    [6, 6, 19, 3, 15, 'x', 'x', 'x', 'x', 4, 10, 19, 2, 4],
    [3, 16, 8, 'x', 5, 'x', 12, 17, 16, 'x', 9, 5, 6, 'x'],
    [17, 2, 'x', 'x', 16, 'x', 5, 'x', 'x', 5, 17, 7, 2, 5],
    [19, 'x', 'x', 'x', 'x', 2, 15, 15, 'x', 3, 11, 'x', 4, 'x'],
    ['x', 'x', 11, 'x', 'x', 17, 5, 'x', 5, 'x', 'x', 19, 6, 'x'],
    [16, 17, 16, 'x', 12, 'x', 2, 18, 9, 7, 'x', 13, 'x', 'x'],
    [18, 11, 'x', 'x', 19, 5, 'x', 'x', 18, 4, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 2, 5, 4, 12, 3, 'x', 4, 14, 7, 19],
    [18, 'x', 'x', 'x', 7, 17, 'x', 'x', 3, 15, 'x', 16, 'x', 10],
    ['x', 11, 15, 'x', 'x', 'x', 'x', 'x', 2, 13, 'x', 'x', 'x', 3],
    [4, 8, 'x', 'x', 'x', 'x', 12, 13, 'x', 'x', 19, 'x', 6, 'x']
]

# Define the start and end points
start = (7, 12)
end = (2, 0)

# Define the districts
districts = [(0, 2), (3, 6), (7, 13)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts):
    # Define the priority queue
    queue = PriorityQueue()
    queue.put((0, [start]))

    # Define the set of visited nodes
    visited = set()

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

        # Add the neighboring nodes to the queue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_node = (node[0] + dx, node[1] + dy)

            # If the next node is within the city map and is not a closed workshop, add it to the queue
            if (0 <= next_node[0] < len(city_map) and 0 <= next_node[1] < len(city_map[0]) and
                    city_map[next_node[0]][next_node[1]] != 'x'):
                next_cost = cost + city_map[next_node[0]][next_node[1]]
                queue.put((next_cost, path + [next_node]))

    # If no path is found, return None
    return None

# Find the shortest path
path = a_star_search(start, end, city_map, districts)
print(path)

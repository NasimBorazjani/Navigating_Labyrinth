
from queue import PriorityQueue

# Define the city map
city_map = [
    [19, 14, 16, 4, 15, 16, 15, 'x', 9, 'x', 'x', 'x'],
    ['x', 7, 12, 6, 'x', 12, 'x', 3, 'x', 14, 5, 9],
    [1, 12, 'x', 'x', 12, 'x', 'x', 'x', 'x', 'x', 10, 1],
    ['x', 1, 15, 14, 'x', 2, 13, 'x', 'x', 'x', 10, 9],
    [7, 'x', 13, 'x', 14, 1, 14, 8, 'x', 'x', 8, 5],
    [18, 'x', 8, 13, 12, 13, 'x', 12, 3, 'x', 14, 'x'],
    ['x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 10],
    ['x', 5, 'x', 4, 'x', 'x', 'x', 3, 5, 6, 6, 11],
    ['x', 15, 6, 'x', 4, 18, 'x', 'x', 14, 10, 2, 8],
    [13, 10, 13, 7, 3, 6, 'x', 'x', 10, 17, 10, 15],
    [4, 'x', 'x', 7, 19, 4, 13, 13, 12, 'x', 'x', 13],
    [5, 'x', 'x', 9, 19, 18, 'x', 'x', 16, 'x', 2, 'x']
]

# Define the start and end points
start = (4, 11)
end = (9, 2)

# Define the districts
districts = [(0, 3), (4, 8), (9, 11)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts):
    # Define the priority queue
    queue = PriorityQueue()
    queue.put((0, [start]))

    # Define the set of visited nodes
    visited = set()

    # While the queue is not empty
    while not queue.empty():
        # Get the node with the lowest cost
        cost, path = queue.get()

        # Get the current node
        current = path[-1]

        # If the current node is the end node
        if current == end:
            # If the path visits at least one workshop in each district
            if all(any(district[0] <= workshop[0] <= district[1] for workshop in path) for district in districts):
                # Return the path
                return path

        # If the current node has not been visited
        if current not in visited:
            # Add the current node to the set of visited nodes
            visited.add(current)

            # For each neighbor of the current node
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Calculate the coordinates of the neighbor
                nx, ny = current[0] + dx, current[1] + dy

                # If the neighbor is within the city map and is not a closed workshop
                if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                    # Calculate the cost to reach the neighbor
                    new_cost = cost + city_map[nx][ny]

                    # Add the neighbor to the queue
                    queue.put((new_cost, path + [(nx, ny)]))

# Print the quickest route
print(a_star_search(start, end, city_map, districts))

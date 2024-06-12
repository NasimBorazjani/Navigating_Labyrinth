
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'Q': {'D': 1},
        'O': {'F': 1},
        'P': {'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        'T': {'E': 1, 'H': 1},
        'W': {'B': 1, 'F': 1, 'J': 1},
        'E': {'G': 1},
        'X': {'C': 1, 'J': 1},
        'M': {'B': 1, 'G': 1, 'J': 1},
        'D': {'B': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1},
        'V': {'A': 1, 'B': 1, 'C': 1, 'F': 1}
    }

    # Define the start city, the two destination cities, and the number of times we need to visit each destination
    start_city = 'Q'
    destination_cities = ['P', 'E']
    num_visits = 2

    # Initialize a priority queue to store the paths to explore, with the initial path as the first element
    queue = []
    heapq.heappush(queue, (0, [start_city], {start_city: 1}))

    # While there are paths to explore
    while queue:
        _, path, visited = heapq.heappop(queue)
        current_city = path[-1]

        # Check if we have visited both destination cities the required number of times
        if visited.get(destination_cities[0], 0) == num_visits and visited.get(destination_cities[1], 0) == num_visits:
            return path

        # Explore all possible connections from the current city
        for neighbor, _ in adjacency_matrix.get(current_city, {}).items():
            # Check if we have not visited the neighbor city before
            if neighbor not in visited:
                # Create a new path by extending the current path
                new_path = path + [neighbor]
                # Create a new visited dictionary with the updated visit count for the neighbor city
                new_visited = visited.copy()
                new_visited[neighbor] = new_visited.get(neighbor, 0) + 1
                # Calculate the cost of the new path (in this case, the length of the path)
                new_cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, new_path, new_visited))

    return None


print(a_star())

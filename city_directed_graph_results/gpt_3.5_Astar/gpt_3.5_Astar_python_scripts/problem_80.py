
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'S': {'E': 1, 'P': 1, 'M': 1},
        'X': {'E': 1, 'O': 1, 'C': 1, 'T': 1, 'W': 1},
        'G': {'S': 1, 'O': 1, 'M': 1},
        'E': {'X': 1, 'P': 1, 'B': 1, 'C': 1, 'L': 1},
        'P': {'G': 1, 'O': 1, 'C': 1, 'L': 1, 'J': 1},
        'B': {'G': 1, 'O': 1, 'C': 1, 'L': 1, 'J': 1},
        'O': {'X': 1, 'C': 1},
        'C': {'E': 1, 'P': 1, 'L': 1, 'J': 1},
        'L': {'X': 1, 'C': 1, 'J': 1},
        'J': {'X': 1, 'P': 1, 'L': 1, 'M': 1, 'W': 1},
        'M': {'E': 1, 'P': 1, 'J': 1},
        'Y': {'P': 1, 'W': 1},
        'T': {'S': 1, 'E': 1, 'C': 1, 'J': 1},
        'W': {'E': 1, 'C': 1, 'J': 1}
    }

    # Define the start city and the two destination cities we need to visit twice
    start_city = 'Y'
    destinations = ['M', 'B']

    # Initialize a priority queue to store the paths to explore, with the initial path containing only the start city
    queue = [(0, [start_city])]

    while queue:
        _, path = heapq.heappop(queue)
        current_city = path[-1]

        # Check if we have visited both destination cities twice and return the path if we have
        if path.count(destinations[0]) == 2 and path.count(destinations[1]) == 2:
            return path

        # Explore all possible connections from the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            # Check if the neighbor city has not been visited before
            if neighbor not in path:
                # Calculate the cost of the path (number of cities visited) and add it to the priority queue
                cost = len(path)
                heapq.heappush(queue, (cost, path + [neighbor]))

    return None


print(a_star())

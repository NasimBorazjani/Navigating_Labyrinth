
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'E': {'V': 1, 'F': 1},
        'V': {'G': 1, 'N': 1},
        'G': {'W': 1, 'F': 1, 'L': 1},
        'W': {'E': 1, 'V': 1, 'B': 1},
        'U': {'E': 1, 'F': 1},
        'F': {'S': 1, 'H': 1, 'Z': 1, 'N': 1, 'J': 1},
        'S': {'V': 1, 'H': 1, 'Z': 1, 'L': 1},
        'H': {'E': 1, 'S': 1, 'K': 1},
        'K': {'E': 1, 'V': 1, 'G': 1, 'S': 1},
        'B': {'H': 1, 'Z': 1, 'J': 1},
        'Z': {'V': 1, 'G': 1, 'S': 1, 'N': 1, 'L': 1},
        'N': {'V': 1, 'F': 1, 'Z': 1, 'J': 1},
        'L': {'F': 1, 'Z': 1, 'N': 1},
        'J': {'B': 1, 'Z': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_city = 'K'
    goal_cities = ['F', 'Z']
    num_visits = {city: 2 for city in goal_cities}
    visited = {city: 0 for city in goal_cities}
    path = [initial_city]

    # Initialize a priority queue to store the cities to visit, with the initial city as the first element
    queue = [(0, initial_city, path)]

    while queue:
        _, current_city, path = heapq.heappop(queue)

        # Check if the current city is one of the goal cities and if we need to visit it again
        if current_city in goal_cities and visited[current_city] < num_visits[current_city]:
            visited[current_city] += 1

            # If we have visited all goal cities the required number of times, return the path
            if all(visited[city] == num_visits[city] for city in goal_cities):
                return path

        # Explore the neighbors of the current city
        for neighbor, connection in adjacency_matrix[current_city].items():
            new_path = path + [neighbor]
            # Calculate the cost of the new path based on the number of connections
            new_cost = len(new_path)

            # Add the new path to the priority queue
            heapq.heappush(queue, (new_cost, neighbor, new_path))

    return None


print(a_star())

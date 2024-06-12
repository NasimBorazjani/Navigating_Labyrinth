
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'O': {'M': 1},
        'T': {'O': 1, 'G': 1, 'K': 1},
        'F': {'T': 1, 'C': 1},
        'C': {'K': 1, 'X': 1},
        'K': {'O': 1, 'F': 1, 'A': 1, 'M': 1},
        'U': {'G': 1},
        'X': {'F': 1, 'U': 1, 'K': 1},
        'G': {'C': 1, 'K': 1, 'Y': 1},
        'A': {'T': 1},
        'M': {'A': 1, 'W': 1, 'Y': 1},
        'W': {'O': 1, 'G': 1},
        'Y': {'T': 1, 'F': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'O'
    goal_state = ['M', 'K']
    num_visits = {city: 2 for city in goal_state}
    visited = {city: 0 for city in goal_state}

    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, initial_state, [])]

    # While there are states to visit
    while queue:
        _, current_city, path = heapq.heappop(queue)

        # If we reach one of the goal cities, increment the visit count and update the path
        if current_city in goal_state:
            visited[current_city] += 1
            path.append(current_city)

            # If we have visited both goal cities twice, return the path
            if visited == num_visits:
                return path

        # Explore the neighbors of the current city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if visiting the neighbor is valid based on the constraints
            if visited[neighbor] < num_visits[neighbor]:
                # Calculate the cost of the path so far
                new_cost = len(path) + cost
                # Add the neighbor to the queue with the updated path
                heapq.heappush(queue, (new_cost, neighbor, path + [current_city]))

    return None


print(a_star())

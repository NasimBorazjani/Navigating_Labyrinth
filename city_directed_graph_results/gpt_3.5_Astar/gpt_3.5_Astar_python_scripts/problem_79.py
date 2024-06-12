
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'Z': {'N': 1},
        'G': {'R': 1, 'V': 1, 'K': 1},
        'K': {'N': 1, 'S': 1, 'W': 1},
        'N': {'S': 1},
        'S': {'X': 1},
        'X': {'G': 1, 'I': 1, 'F': 1},
        'I': {'R': 1},
        'F': {'K': 1, 'E': 1, 'W': 1},
        'E': {'C': 1, 'V': 1, 'W': 1},
        'C': {'G': 1},
        'R': {'K': 1},
        'V': {'K': 1, 'X': 1, 'W': 1},
        'L': {'G': 1},
        'W': {'E': 1, 'F': 1, 'V': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'I'
    goal_state = ['S', 'W']
    num_visits = {city: 0 for city in goal_state}
    path = [initial_state]

    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, initial_state, path, num_visits)]

    # While there are states to visit
    while queue:
        _, current_city, current_path, current_visits = heapq.heappop(queue)

        # If we have visited both destination cities twice, return the path
        if all(value == 2 for value in current_visits.values()):
            return current_path

        # Check the connections from the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            # If we haven't visited the neighbor city twice yet
            if current_visits[neighbor] < 2:
                # Update the number of visits to the neighbor city
                new_visits = current_visits.copy()
                new_visits[neighbor] += 1
                # Add the neighbor city to the path
                new_path = current_path + [neighbor]
                # Calculate the cost of the new path (length of the path)
                new_cost = len(new_path)
                # Add the new state to the priority queue
                heapq.heappush(queue, (new_cost, neighbor, new_path, new_visits))

    return None


print(a_star())

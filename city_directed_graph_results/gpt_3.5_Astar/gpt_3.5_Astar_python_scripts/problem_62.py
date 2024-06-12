
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'Z': {'M': 0, 'X': 0, 'N': 0, 'A': 1, 'B': 1, 'L': 0, 'U': 1, 'K': 1, 'G': 1, 'Y': 0, 'O': 0},
        'C': {'Z': 1, 'M': 0, 'X': 1, 'N': 1, 'A': 0, 'B': 1, 'L': 0, 'U': 0, 'K': 0, 'G': 0, 'Y': 1, 'O': 1},
        'M': {'Z': 0, 'C': 0, 'X': 0, 'N': 0, 'A': 1, 'B': 1, 'L': 1, 'U': 0, 'K': 0, 'G': 0, 'Y': 1, 'O': 0},
        'X': {'Z': 0, 'C': 0, 'M': 1, 'N': 0, 'A': 0, 'B': 0, 'L': 0, 'U': 1, 'K': 0, 'G': 0, 'Y': 1, 'O': 1},
        'N': {'Z': 1, 'C': 1, 'M': 0, 'X': 0, 'A': 0, 'B': 0, 'L': 1, 'U': 0, 'K': 0, 'G': 0, 'Y': 0, 'O': 0},
        'A': {'Z': 1, 'C': 0, 'M': 1, 'X': 0, 'N': 0, 'B': 0, 'L': 1, 'U': 0, 'K': 0, 'G': 0, 'Y': 0, 'O': 0},
        'B': {'Z': 0, 'C': 1, 'M': 0, 'X': 0, 'N': 0, 'A': 0, 'L': 0, 'U': 1, 'K': 0, 'G': 1, 'Y': 0, 'O': 1},
        'L': {'Z': 0, 'C': 0, 'M': 0, 'X': 0, 'N': 0, 'A': 0, 'B': 0, 'U': 0, 'K': 1, 'G': 0, 'Y': 0, 'O': 0},
        'U': {'Z': 1, 'C': 0, 'M': 1, 'X': 0, 'N': 0, 'A': 0, 'B': 0, 'L': 0, 'K': 1, 'G': 0, 'Y': 0, 'O': 1},
        'K': {'Z': 0, 'C': 0, 'M': 0, 'X': 1, 'N': 1, 'A': 1, 'B': 0, 'L': 0, 'U': 0, 'G': 0, 'Y': 0, 'O': 0},
        'G': {'Z': 1, 'C': 0, 'M': 0, 'X': 1, 'N': 1, 'A': 1, 'B': 1, 'L': 1, 'U': 0, 'K': 0, 'Y': 1, 'O': 0},
        'Y': {'Z': 0, 'C': 0, 'M': 0, 'X': 0, 'N': 1, 'A': 0, 'B': 1, 'L': 0, 'U': 0, 'K': 0, 'G': 1, 'O': 0},
        'O': {'Z': 1, 'C': 1, 'M': 0, 'X': 0, 'N': 0, 'A': 0, 'B': 1, 'L': 0, 'U': 1, 'K': 0, 'G': 1, 'Y': 0}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'K'
    goal_state = ['U', 'Y']
    num_visits = {city: 0 for city in goal_state}
    path = [initial_state]

    # Initialize a priority queue to store the cities to visit, with the initial state as the first element
    queue = [(0, initial_state, path, num_visits)]

    while queue:
        _, current_city, current_path, current_visits = heapq.heappop(queue)

        # If we have visited both U and Y twice, return the current path
        if current_visits['U'] == 2 and current_visits['Y'] == 2:
            return current_path

        # Check all possible next cities to visit
        for next_city in adjacency_matrix[current_city]:
            # Check if we can visit the next city and if we haven't visited it twice already
            if adjacency_matrix[current_city][next_city] == 1 and current_visits[next_city] < 2:
                # Update the number of visits to the next city
                new_visits = current_visits.copy()
                new_visits[next_city] += 1
                # Add the next city to the path
                new_path = current_path + [next_city]
                # Calculate the cost of the new path (length of the path)
                new_cost = len(new_path)
                # Add the new path to the priority queue
                heapq.heappush(queue, (new_cost, next_city, new_path, new_visits))

    return None


print(a_star())


import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'K': {'P': 1, 'O': 1, 'U': 1, 'Q': 0, 'D': 0, 'G': 0, 'R': 0, 'C': 0, 'B': 0, 'J': 0, 'X': 0, 'S': 0, 'E': 0, 'I': 1},
        'P': {'K': 0, 'O': 0, 'U': 0, 'Q': 0, 'D': 1, 'G': 0, 'R': 0, 'C': 0, 'B': 0, 'J': 0, 'X': 0, 'S': 0, 'E': 1, 'I': 0},
        'O': {'K': 1, 'P': 0, 'U': 0, 'Q': 0, 'D': 1, 'G': 0, 'R': 0, 'C': 0, 'B': 1, 'J': 0, 'X': 0, 'S': 1, 'E': 0, 'I': 1},
        'U': {'K': 0, 'P': 0, 'O': 0, 'Q': 0, 'D': 0, 'G': 1, 'R': 0, 'C': 0, 'B': 1, 'J': 0, 'X': 0, 'S': 0, 'E': 0, 'I': 1},
        'Q': {'K': 1, 'P': 1, 'O': 0, 'U': 0, 'D': 0, 'G': 0, 'R': 1, 'C': 1, 'B': 1, 'J': 0, 'X': 0, 'S': 0, 'E': 0, 'I': 0},
        'D': {'K': 0, 'P': 0, 'O': 1, 'U': 0, 'Q': 0, 'G': 0, 'R': 1, 'C': 0, 'B': 0, 'J': 0, 'X': 1, 'S': 1, 'E': 0, 'I': 0},
        'G': {'K': 1, 'P': 0, 'O': 0, 'U': 1, 'Q': 0, 'D': 0, 'R': 0, 'C': 0, 'B': 0, 'J': 0, 'X': 1, 'S': 1, 'E': 0, 'I': 0},
        'R': {'K': 0, 'P': 0, 'O': 1, 'U': 0, 'Q': 0, 'D': 1, 'G': 0, 'C': 0, 'B': 1, 'J': 1, 'X': 0, 'S': 0, 'E': 0, 'I': 0},
        'C': {'K': 1, 'P': 1, 'O': 1, 'U': 1, 'Q': 0, 'D': 0, 'G': 1, 'R': 1, 'B': 0, 'J': 0, 'X': 1, 'S': 0, 'E': 0, 'I': 0},
        'B': {'K': 1, 'P': 0, 'O': 0, 'U': 0, 'Q': 0, 'D': 0, 'G': 0, 'R': 0, 'C': 0, 'J': 0, 'X': 0, 'S': 1, 'E': 0, 'I': 0},
        'J': {'K': 0, 'P': 1, 'O': 0, 'U': 0, 'Q': 0, 'D': 0, 'G': 1, 'R': 0, 'C': 0, 'B': 0, 'X': 1, 'S': 0, 'E': 1, 'I': 0},
        'X': {'K': 0, 'P': 0, 'O': 1, 'U': 1, 'Q': 0, 'D': 0, 'G': 1, 'R': 0, 'C': 0, 'B': 0, 'J': 0, 'S': 0, 'E': 0, 'I': 0},
        'S': {'K': 0, 'P': 0, 'O': 0, 'U': 1, 'Q': 1, 'D': 0, 'G': 0, 'R': 0, 'C': 0, 'B': 0, 'J': 1, 'X': 0, 'E': 0, 'I': 0},
        'E': {'K': 0, 'P': 0, 'O': 0, 'U': 0, 'Q': 1, 'D': 1, 'G': 0, 'R': 0, 'C': 0, 'B': 0, 'J': 1, 'X': 1, 'S': 0, 'I': 0},
        'I': {'K': 0, 'P': 0, 'O': 0, 'U': 0, 'Q': 1, 'D': 1, 'G': 0, 'R': 1, 'C': 1, 'B': 1, 'J': 0, 'X': 0, 'S': 0, 'E': 0}
    }

    # Define the initial state as the starting city 'B'
    initial_state = 'B'
    # Define the goal state as visiting cities 'Q' and 'I' twice each
    goal_state = ['Q', 'Q', 'I', 'I']

    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], initial_state)]

    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # Check if the current path satisfies the goal state
        if path == goal_state:
            return path

        # Generate all possible actions from the current state, which are the cities connected to the current city
        for city, connected in adjacency_matrix[current_city].items():
            if connected == 1 and city not in path:
                new_path = path + [city]
                new_cost = g + 1
                # Calculate the heuristic cost as the number of cities left to visit
                h = len(goal_state) - len(new_path)
                # Add the new state to the priority queue
                heapq.heappush(queue, (new_cost + h, new_cost, new_path, city))

    return None


print(a_star())

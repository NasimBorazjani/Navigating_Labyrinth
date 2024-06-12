
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'E': {'N': 1, 'R': 1, 'W': 1, 'M': 1, 'B': 1, 'H': 1, 'Q': 1},
        'K': {'A': 1, 'J': 1, 'R': 1},
        'G': {'A': 1, 'O': 1, 'N': 1},
        'C': {'K': 1, 'U': 1, 'J': 1},
        'U': {'E': 1, 'A': 1},
        'A': {'C': 1, 'U': 1, 'J': 1, 'O': 1},
        'J': {'A': 1, 'C': 1, 'O': 1, 'H': 1},
        'O': {'N': 1, 'H': 1},
        'N': {'E': 1, 'G': 1, 'U': 1, 'R': 1, 'W': 1},
        'R': {'N': 1, 'W': 1, 'M': 1, 'B': 1, 'H': 1, 'Q': 1},
        'W': {'E': 1, 'N': 1, 'R': 1, 'M': 1, 'H': 1},
        'M': {'A': 1, 'W': 1},
        'B': {'N': 1, 'M': 1},
        'H': {'E': 1, 'A': 1, 'R': 1, 'M': 1},
        'Q': {'E': 1, 'G': 1, 'H': 1}
    }

    # Define the initial state, which is the starting city 'C'
    initial_state = 'C'
    # Define the goal state, which is to visit cities 'E' and 'Q' twice each
    goal_state = ['E', 'E', 'Q', 'Q']

    # Initialize a priority queue to store the states to be visited, with the initial state as the first element
    queue = [(0, initial_state, [])]

    # While there are states to visit
    while queue:
        _, current_city, path = heapq.heappop(queue)

        # If the current city is one of the goal cities, remove it from the list of goal cities
        if current_city in goal_state:
            goal_state.remove(current_city)
            # If all goal cities have been visited twice, return the path
            if not goal_state:
                return path

        # Explore the neighbors of the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            # Add the neighbor to the path and calculate the cost of the path
            new_path = path + [neighbor]
            new_cost = len(new_path)

            # Add the neighbor to the priority queue with the cost of the path
            heapq.heappush(queue, (new_cost, neighbor, new_path))

    return None


print(a_star())

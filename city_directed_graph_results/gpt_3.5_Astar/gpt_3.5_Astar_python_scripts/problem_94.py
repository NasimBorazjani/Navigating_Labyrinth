
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'X': {'M': 1, 'O': 1, 'P': 1},
        'T': {'J': 1, 'P': 1},
        'R': {'O': 1, 'U': 1, 'I': 1},
        'O': {'X': 1, 'M': 1, 'Q': 1},
        'M': {'X': 1, 'O': 1, 'F': 1},
        'U': {'R': 1},
        'I': {'O': 1, 'H': 1, 'B': 1},
        'P': {'T': 1, 'J': 1, 'Z': 1},
        'Z': {'P': 1, 'J': 1},
        'F': {'M': 1, 'V': 1},
        'V': {'F': 1, 'Z': 1},
        'H': {'I': 1, 'Q': 1, 'B': 1},
        'Q': {'P': 1, 'J': 1},
        'J': {'T': 1, 'P': 1, 'Q': 1, 'B': 1},
        'B': {'I': 1, 'H': 1, 'J': 1}
    }

    # Define the initial state and the goal state
    initial_state = 'I'
    goal_state = ['H', 'R', 'H', 'R']

    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of cities not yet visited, with the initial state as the first element
    queue = [(0, initial_state, [])]

    # While there are un-visited cities
    while queue:
        _, current_city, path = heapq.heappop(queue)

        # If we have visited both 'H' and 'R' twice, return the path
        if path.count('H') == 2 and path.count('R') == 2:
            return path + [current_city]

        # Generate all possible actions from the current city, which includes moving to a connected city
        for neighbor, cost in adjacency_matrix[current_city].items():
            new_cost = visited_costs[current_city] + cost

            # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor, path + [current_city]))

    return None


print(a_star())

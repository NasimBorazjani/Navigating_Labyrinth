
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'D': {'F': 1, 'K': 1, 'L': 1},
        'Y': {'D': 1, 'H': 1, 'Q': 1, 'B': 1},
        'F': {'M': 1, 'I': 1},
        'M': {'H': 1, 'I': 1, 'L': 1},
        'W': {'F': 1, 'Q': 1},
        'H': {'Y': 1, 'W': 1, 'Q': 1, 'B': 1, 'I': 1, 'L': 1},
        'Q': {'D': 1, 'Y': 1, 'H': 1, 'B': 1},
        'B': {'F': 1, 'H': 1},
        'K': {'H': 1, 'S': 1},
        'S': {'Y': 1, 'F': 1, 'H': 1, 'I': 1},
        'V': {'K': 1, 'S': 1, 'I': 1},
        'I': {'M': 1, 'H': 1, 'S': 1, 'V': 1, 'L': 1},
        'L': {'D': 1, 'M': 1, 'I': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_city = 'K'
    goal_cities = ['D', 'L']
    num_visits = 2

    visited_costs = {}
    visited_costs[initial_city] = 0

    queue = [(0, 0, [], initial_city)]

    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # Check if we have visited the goal cities the required number of times
        if path.count('D') == num_visits and path.count('L') == num_visits:
            return path

        # Generate all possible actions from the current city, which includes moving to neighboring cities
        for neighbor, cost in adjacency_matrix[current_city].items():
            new_path = path + [neighbor]
            new_cost = g + cost

            # If the new city is not visited or we found a new path with a lower cost to reach this city, add it to the queue
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, new_path, neighbor))

    return None


print(a_star())

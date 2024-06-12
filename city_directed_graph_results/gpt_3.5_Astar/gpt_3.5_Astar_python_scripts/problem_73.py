
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'K': {'N': 1, 'I': 1, 'T': 1, 'D': 1, 'B': 1},
        'N': {'M': 1, 'R': 1},
        'S': {'O': 1, 'K': 1, 'R': 1},
        'Y': {'K': 1},
        'O': {'I': 1, 'Z': 1},
        'I': {'M': 1, 'T': 1, 'B': 1, 'E': 1},
        'T': {'S': 1, 'D': 1, 'M': 1},
        'D': {'K': 1, 'M': 1},
        'M': {'Z': 1, 'R': 1, 'B': 1},
        'Z': {'O': 1},
        'R': {'N': 1, 'B': 1, 'F': 1},
        'B': {'K': 1, 'I': 1, 'T': 1, 'E': 1},
        'E': {'M': 1, 'F': 1},
        'F': {'S': 1}
    }

    # Define the start city and the goal cities
    start_city = 'Y'
    goal_cities = ['S', 'K']

    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0

    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]

    # While there are un-visited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # If we have visited both goal cities twice, return the path
        if path.count('S') == 2 and path.count('K') == 2:
            return path

        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor, cost in adjacency_matrix[current_city].items():
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            new_cost = g + cost
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, path + [neighbor], neighbor))

    return None


print(a_star())


import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'Z': {'R': 1, 'U': 1, 'L': 1},
        'N': {'Z': 1, 'O': 1, 'P': 1, 'Q': 1, 'G': 1},
        'R': {'N': 1, 'L': 1},
        'F': {'L': 1},
        'O': {'R': 1, 'U': 1, 'J': 1, 'S': 1},
        'U': {'L': 1, 'P': 1},
        'P': {'Z': 1, 'J': 1},
        'L': {'J': 1},
        'J': {'U': 1},
        'I': {'U': 1, 'S': 1},
        'S': {'N': 1, 'I': 1, 'Q': 1},
        'Q': {'O': 1, 'G': 1},
        'G': {'U': 1}
    }

    # Define the start city and the goal cities
    start_city = 'F'
    goal_cities = ['N', 'J']

    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[start_city] = 0

    # Initialize a priority queue of cities not yet visited, with the start city as the first element
    queue = [(0, 0, [start_city], start_city)]

    # While there are un-visited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # Check if we have visited both goal cities twice
        if path.count('N') == 2 and path.count('J') == 2:
            return path

        # Generate all possible actions from the current city, which includes moving to any connected city
        for neighbor in adjacency_matrix[current_city]:
            # Check if the new city is unvisited or we found a new path with a lower cost to reach this city
            new_cost = g + 1
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, new_cost, path + [neighbor], neighbor))

    return None


print(a_star())

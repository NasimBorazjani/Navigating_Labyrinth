
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'I': {'F': 0, 'E': 0, 'Y': 1, 'A': 0, 'Z': 0, 'T': 0, 'H': 0, 'Q': 1},
        'V': {'F': 0, 'E': 0, 'Y': 0, 'A': 0, 'Z': 0, 'T': 0, 'H': 1, 'Q': 0},
        'F': {'I': 0, 'V': 0, 'E': 0, 'Y': 1, 'A': 0, 'Z': 1, 'T': 0, 'H': 0, 'Q': 0},
        'E': {'I': 0, 'V': 0, 'F': 0, 'Y': 0, 'A': 1, 'Z': 0, 'T': 0, 'H': 0, 'Q': 0},
        'Y': {'I': 1, 'V': 0, 'F': 1, 'E': 0, 'A': 0, 'Z': 0, 'T': 0, 'H': 0, 'Q': 1},
        'A': {'I': 1, 'V': 1, 'F': 0, 'E': 0, 'Y': 0, 'Z': 0, 'T': 0, 'H': 0, 'Q': 0},
        'Z': {'I': 1, 'V': 0, 'F': 1, 'E': 1, 'Y': 0, 'A': 0, 'T': 0, 'H': 0, 'Q': 1},
        'T': {'I': 0, 'V': 1, 'F': 1, 'E': 1, 'Y': 1, 'A': 1, 'Z': 1, 'H': 0, 'Q': 0},
        'H': {'I': 1, 'V': 0, 'F': 0, 'E': 0, 'Y': 0, 'A': 0, 'Z': 0, 'T': 1, 'Q': 0},
        'Q': {'I': 0, 'V': 0, 'F': 0, 'E': 0, 'Y': 0, 'A': 0, 'Z': 1, 'T': 1, 'H': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'V'
    goal_state = ['I', 'Y']
    num_visits = 2

    # Initialize a dictionary to store the cost of reaching each visited city
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of cities not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], initial_state)]

    # While there are unvisited cities
    while queue:
        _, g, path, current_city = heapq.heappop(queue)

        # If we have visited the goal cities the required number of times, return the path
        if path.count(goal_state[0]) == num_visits and path.count(goal_state[1]) == num_visits:
            return path

        # Generate all possible actions from the current city, which includes moving to any city connected by a road
        for neighbor, cost in adjacency_matrix[current_city].items():
            new_path = path + [neighbor]
            new_cost = g + cost

            # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost + heuristic(new_path, goal_state), new_cost, new_path, neighbor))

    return None


def heuristic(path, goal_state):
    # The heuristic function calculates the number of times we need to visit the goal cities minus the number of times we have already visited them
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as we need to visit the goal cities exactly twice
    # The heuristic is consistent because the estimated cost of the next node is higher if we need to visit the goal cities more times, and the cost of the goal state is 0
    return max(0, 2 * goal_state.count(path[-1]) - path.count(path[-1]))


print(a_star())

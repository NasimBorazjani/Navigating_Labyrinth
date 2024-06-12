
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'I': ['S'],
        'P': ['G', 'S', 'A', 'D', 'E', 'Z'],
        'G': ['I', 'P', 'W', 'H', 'X'],
        'S': ['D', 'V'],
        'Y': ['I'],
        'A': ['I', 'H'],
        'D': ['A', 'H'],
        'U': ['G', 'S', 'E', 'W'],
        'E': ['A', 'U', 'Z'],
        'W': ['D', 'X'],
        'V': ['I', 'P', 'G', 'A', 'X'],
        'H': ['Y', 'A', 'E', 'W', 'V'],
        'Z': ['I', 'A', 'U', 'E'],
        'X': ['I', 'P', 'G', 'E', 'W', 'V']
    }

    # Define the initial state and the goal state
    initial_state = ('Y', ['H', 'H', 'X', 'X'], ['Y'])
    goal_state = ('Y', [], ['Y', 'H', 'X', 'H', 'X'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]

    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path taken to reach the goal state
        if state == goal_state:
            return state[2]

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, remaining_cities, path = state
        for next_city in graph[current_city]:
            # If the next city is a destination city and it is still remaining to be visited, or it is not a destination city and it has not been visited yet
            if (next_city in remaining_cities) or (next_city not in ['H', 'X'] and next_city not in path):
                # Generate the new state
                new_remaining_cities = remaining_cities[:]
                if next_city in new_remaining_cities:
                    new_remaining_cities.remove(next_city)
                new_path = path + [next_city]
                new_state = (next_city, new_remaining_cities, new_path)

                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of remaining destination cities to be visited
                    h = len(new_remaining_cities)
                    heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None

print(a_star())

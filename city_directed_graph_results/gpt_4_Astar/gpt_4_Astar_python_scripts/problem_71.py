
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'E': ['V', 'F', 'B', 'J'],
        'V': ['G', 'J'],
        'G': ['U', 'F', 'N'],
        'W': ['E', 'V', 'U', 'F', 'B'],
        'U': ['E', 'V', 'F'],
        'F': ['W', 'H', 'B', 'N', 'L'],
        'S': ['G', 'H', 'B', 'L'],
        'H': ['E', 'J'],
        'K': ['E', 'V', 'G', 'S'],
        'B': ['H', 'K', 'N'],
        'Z': ['V', 'G', 'S', 'H', 'N', 'J'],
        'N': ['V', 'S', 'K', 'B', 'Z', 'J'],
        'L': ['V', 'W'],
        'J': ['Z']
    }

    # Define the initial state and the goal state
    initial_state = ('K', ['F', 'F', 'Z', 'Z'], ['E', 'V', 'G', 'W', 'U', 'S', 'H', 'B', 'N', 'L', 'J'])
    goal_state = ('K', [], [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [initial_state[0]])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path = heapq.heappop(queue)
        current_city, destinations, cities = path[-1], path[-2], path[-3]

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if (current_city, destinations, cities) == goal_state:
            return path

        # Generate all valid actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[current_city]:
            # Check if the move is valid, ie if the city is a destination city or if it has not been visited before
            if neighbor in destinations or neighbor in cities:
                # The action is valid, generate the new state
                new_destinations = destinations[:]
                new_cities = cities[:]
                if neighbor in new_destinations:
                    new_destinations.remove(neighbor)
                else:
                    new_cities.remove(neighbor)
                new_state = (neighbor, new_destinations, new_cities)

                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]]))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities that have not been visited yet
    # The heuristic relaxes the constraint that a city can only be visited once and presumes we can visit the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited in the goal state.
    return len(state[1])

print(a_star())

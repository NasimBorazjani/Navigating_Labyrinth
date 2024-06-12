
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'D': ['E', 'Z', 'R', 'G', 'L', 'B'],
        'E': ['Z'],
        'Z': ['N'],
        'R': ['D', 'Z', 'B'],
        'N': ['E', 'I', 'K', 'G'],
        'I': ['D', 'N', 'K', 'L'],
        'K': ['Z', 'N'],
        'G': ['Z', 'R', 'I'],
        'L': ['Z', 'G'],
        'B': ['E', 'I', 'K']
    }
    # Define the initial state and the goal state
    initial_state = ('L', ['D', 'D', 'N', 'N'], ['D', 'E', 'Z', 'R', 'N', 'I', 'K', 'G', 'B'])
    goal_state = ('L', [], ['L'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, ['L'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path taken to reach the goal state
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, destinations, unvisited_cities = state
        for city in graph[current_city]:
            # Check if the new state would be valid, ie the city must be unvisited or a destination city
            if city in unvisited_cities or city in destinations:
                # Generate the new state
                new_destinations = destinations[:]
                if city in new_destinations:
                    new_destinations.remove(city)
                new_unvisited_cities = unvisited_cities[:]
                if city in new_unvisited_cities:
                    new_unvisited_cities.remove(city)
                new_state = (city, new_destinations, new_unvisited_cities)

                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of destination cities left to visit, if the city is a destination city
    return len(state[1])

print(a_star())

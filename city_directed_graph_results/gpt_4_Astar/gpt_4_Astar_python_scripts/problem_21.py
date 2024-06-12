
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'I': ['M', 'H', 'C', 'V'],
        'K': ['M'],
        'D': ['R', 'W'],
        'M': ['I'],
        'Y': ['K', 'D'],
        'H': ['K', 'D', 'M', 'C', 'V', 'Q'],
        'C': ['K', 'M', 'Y', 'H', 'V'],
        'R': ['M', 'V', 'Q'],
        'V': ['Y', 'R'],
        'W': ['I', 'M', 'Y'],
        'Q': ['K', 'D', 'Y', 'C', 'R', 'W']
    }

    # Define the initial state and the goal state
    initial_state = ('Y', ['I', 'I', 'Q', 'Q'], ['Y'])
    goal_state = ('Y', [], ['Y', 'I', 'Q', 'I', 'Q', 'Y'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, destinations, visited_cities = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city
            if next_city not in visited_cities or next_city in destinations:
                # Generate the new state
                new_destinations = destinations[:]
                if next_city in new_destinations:
                    new_destinations.remove(next_city)
                new_visited_cities = visited_cities + [next_city]
                new_state = (next_city, new_destinations, new_visited_cities)

                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return len(state[1])

print(a_star())

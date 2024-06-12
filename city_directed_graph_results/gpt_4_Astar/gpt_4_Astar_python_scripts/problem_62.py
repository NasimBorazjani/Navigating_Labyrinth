
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'Z': ['X', 'N', 'B', 'L', 'U', 'K'],
        'C': ['Z', 'M', 'X', 'A', 'Y', 'O'],
        'M': ['N', 'A', 'B', 'Y'],
        'X': ['M', 'L', 'G', 'O'],
        'N': ['Z', 'C'],
        'A': ['Z', 'M', 'B'],
        'B': ['C', 'L', 'K', 'Y', 'O'],
        'L': ['U', 'G'],
        'U': ['Z', 'M', 'K', 'O'],
        'K': ['X', 'N', 'A'],
        'G': ['Z', 'X', 'N', 'A', 'B', 'L', 'Y', 'O'],
        'Y': ['N', 'B'],
        'O': ['Z', 'C', 'B', 'U', 'G', 'Y']
    }

    # Define the initial state and the goal state
    initial_state = ('K', ['U', 'U', 'Y', 'Y'], ['Z', 'C', 'M', 'X', 'N', 'A', 'B', 'L', 'U', 'K', 'G', 'Y', 'O'])
    goal_state = ('K', [], ['Z', 'C', 'M', 'X', 'N', 'A', 'B', 'L', 'G', 'O'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, destinations, unvisited_cities = state
        for next_city in graph[current_city]:
            # Check if the next city is a valid destination, ie it is either a required destination or an unvisited city
            if next_city in destinations or next_city in unvisited_cities:
                # Generate the new state
                new_destinations = destinations[:]
                if next_city in new_destinations:
                    new_destinations.remove(next_city)
                new_unvisited_cities = unvisited_cities[:]
                if next_city in new_unvisited_cities:
                    new_unvisited_cities.remove(next_city)
                new_state = (next_city, new_destinations, new_unvisited_cities)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of required destinations left to visit
    # The heuristic relaxes the constraint that we can only move to neighboring cities and presumes we can move to any of the required destinations directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of required destinations left to visit, if the next city is a required destination, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no required destinations left to visit in the goal state.
    return len(state[1])

print(a_star())

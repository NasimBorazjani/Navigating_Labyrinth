
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {'S': {'E': 1},
                        'A': {'U': 1, 'B': 1, 'L': 1, 'F': 1},
                        'J': {'B': 1, 'L': 1},
                        'U': {'S': 1, 'N': 1, 'P': 1},
                        'E': {'A': 1},
                        'B': {'E': 1, 'N': 1, 'P': 1, 'X': 1},
                        'N': {'A': 1, 'U': 1, 'E': 1, 'B': 1, 'X': 1, 'F': 1},
                        'P': {'S': 1, 'N': 1, 'L': 1},
                        'L': {'J': 1, 'B': 1, 'X': 1, 'F': 1},
                        'X': {'J': 1, 'U': 1, 'L': 1},
                        'F': {'A': 1, 'U': 1, 'L': 1}}

    # Define the initial state as a tuple with the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('J', frozenset(['J']), frozenset())

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

        # Check if the current state is the goal state
        # The goal state is where we have visited both U and E twice
        if state[2].count('U') == 2 and state[2].count('E') == 2:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we can only visit each city once, except for U and E which can be visited twice
            if (next_city not in state[1] or (next_city in ['U', 'E'] and state[2].count(next_city) < 2)):
                # Generate the new state
                new_state = (next_city, state[1].union([next_city]), state[2] + (next_city,))
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic is the number of destination cities (U and E) that have not been visited twice
    # The heuristic relaxes the constraint that we can only visit each city once and presumes we can visit the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited twice in the goal state.
    return 2 - state[2].count('U') - state[2].count('E')

print(a_star())

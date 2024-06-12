
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {'R': {'E': 1, 'G': 1, 'Z': 1},
                        'L': {'G': 1, 'A': 1},
                        'F': {'Q': 1},
                        'E': {'Q': 1, 'U': 1},
                        'D': {'R': 1, 'E': 1, 'H': 1, 'A': 1},
                        'Q': {'R': 1, 'L': 1, 'U': 1, 'H': 1},
                        'G': {'L': 1, 'F': 1, 'E': 1, 'D': 1, 'U': 1, 'H': 1},
                        'U': {'D': 1, 'H': 1, 'Z': 1},
                        'H': {'R': 1, 'F': 1},
                        'T': {'L': 1, 'D': 1, 'H': 1, 'Z': 1},
                        'Z': {'R': 1, 'F': 1, 'D': 1, 'Q': 1, 'H': 1},
                        'A': {'D': 1, 'Q': 1, 'T': 1}}

    # Define the initial state as a tuple with the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('F', frozenset(['F']), frozenset())

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
        # The goal state is where we have visited both destination cities twice
        if len(state[2]) == 4:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we can only visit each city once, except for the destination cities
            if (next_city not in state[1] or (state[1].count(next_city) < 2 and next_city in ['A', 'R'])):
                # Generate the new state
                new_state = (next_city, state[1] | {next_city}, (state[2] | {next_city}) if next_city in ['A', 'R'] else state[2])
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the minimum number of cities that need to be visited to reach the goal state, which is the number of destination cities left to visit
                    h = 4 - len(new_state[2])
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None

print(a_star())

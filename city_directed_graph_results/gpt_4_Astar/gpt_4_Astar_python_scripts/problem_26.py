
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {'L': {'Z': 1, 'R': 1, 'K': 1},
                        'T': {'L': 1, 'P': 1, 'I': 1, 'X': 1},
                        'W': {'R': 1, 'C': 1},
                        'P': {'L': 1, 'K': 1},
                        'Z': {'L': 1, 'T': 1, 'P': 1, 'R': 1},
                        'H': {'L': 1, 'T': 1, 'W': 1, 'K': 1},
                        'I': {'T': 1, 'Z': 1, 'C': 1},
                        'X': {'W': 1, 'H': 1},
                        'R': {'T': 1, 'W': 1, 'P': 1, 'Z': 1, 'I': 1, 'X': 1},
                        'C': {'L': 1, 'T': 1, 'P': 1, 'R': 1},
                        'K': {'H': 1, 'R': 1}}

    # Define the initial state as a tuple with the current city, the set of visited cities, and the count of visits to the destination cities
    initial_state = ('I', frozenset(['I']), {'L': 0, 'W': 0})

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
        # The goal state is where we have visited cities L and W twice
        if state[2]['L'] == 2 and state[2]['W'] == 2:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we can only visit each city once, except for L and W which must be visited twice
            if (next_city not in state[1] or (next_city in ['L', 'W'] and state[2][next_city] < 2)):
                # Generate the new state
                new_state = (next_city, state[1].union([next_city]), state[2].copy())
                new_state[2][next_city] = new_state[2].get(next_city, 0) + 1
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return 2 - state[2]['L'] - state[2]['W']

print(a_star())

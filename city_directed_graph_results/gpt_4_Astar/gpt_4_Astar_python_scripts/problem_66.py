
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city (1 for all cities as the travel time between any two directly connected cities is the same)
    adjacency_matrix = {
        'L': {'F': 1},
        'A': {'L': 1, 'U': 1, 'P': 1},
        'J': {'A': 1, 'Y': 1, 'M': 1},
        'U': {'E': 1, 'R': 1, 'K': 1, 'M': 1},
        'E': {'Q': 1, 'M': 1},
        'P': {'Q': 1, 'K': 1, 'M': 1},
        'Q': {'J': 1, 'U': 1, 'R': 1, 'K': 1, 'L': 1},
        'Y': {'L': 1, 'A': 1, 'U': 1, 'R': 1},
        'H': {'L': 1, 'J': 1, 'U': 1, 'P': 1, 'Y': 1, 'R': 1, 'L': 1},
        'R': {'E': 1, 'K': 1},
        'K': {'A': 1, 'E': 1, 'P': 1, 'R': 1, 'F': 1},
        'M': {'P': 1, 'Q': 1, 'H': 1},
        'F': {'A': 1, 'E': 1, 'P': 1, 'Y': 1, 'K': 1}
    }

    # Define the initial state as a tuple with the current city, the cities visited so far, and the number of times the destination cities have been visited
    initial_state = ('L', ['L'], {'J': 0, 'K': 0})

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
        # The goal state is where we have visited both J and K twice and all other cities at most once
        if state[2]['J'] == 2 and state[2]['K'] == 2 and all(city not in state[1] for city in adjacency_matrix if city not in ['J', 'K']):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we can only visit each city once, except for J and K which we can visit twice
            if (city not in state[1] and city not in ['J', 'K']) or (city in ['J', 'K'] and state[2][city] < 2):
                # Generate the new state
                new_state = (city, state[1] + [city], state[2].copy())
                new_state[2][city] = new_state[2].get(city, 0) + 1
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic is the number of destination cities not yet visited twice
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of visiting a city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return 2 - state[2]['J'] + 2 - state[2]['K']

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city
    adjacency_matrix = {
        'D': {'G': 1, 'Q': 1, 'R': 1, 'N': 1, 'K': 1},
        'M': {'D': 1, 'E': 1},
        'F': {'X': 1, 'O': 1},
        'X': {'M': 1, 'K': 1, 'E': 1},
        'G': {'R': 1, 'N': 1},
        'A': {'G': 1, 'N': 1},
        'Q': {'F': 1, 'G': 1},
        'O': {'D': 1, 'M': 1, 'X': 1, 'A': 1, 'U': 1},
        'U': {'D': 1, 'F': 1, 'X': 1, 'G': 1},
        'R': {'E': 1},
        'N': {'U': 1, 'R': 1, 'K': 1},
        'K': {'M': 1, 'F': 1, 'U': 1},
        'E': {'D': 1, 'O': 1, 'U': 1}
    }

    # Define the initial state as a tuple with the current city, the cities visited so far, and the number of times the destination cities have been visited
    initial_state = ('A', frozenset(['A']), {'D': 0, 'E': 0})

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
        # The goal state is where we have visited cities D and E twice and all other cities once
        if state[2]['D'] == 2 and state[2]['E'] == 2 and len(state[1]) == len(adjacency_matrix):
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we have not visited the next city yet or it is one of the destination cities and we have visited it less than 2 times
            if (next_city not in state[1] or (state[2][next_city] < 2 and next_city in ['D', 'E'])):
                # Generate the new state
                new_visited_cities = state[1].union([next_city])
                new_visited_counts = state[2].copy()
                new_visited_counts[next_city] = new_visited_counts.get(next_city, 0) + 1
                new_state = (next_city, new_visited_cities, new_visited_counts)

                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as we need to visit each destination city at least once
    # The heuristic is consistent because the cost of moving to a destination city is always 1, which is exactly the decrease in the heuristic value, if we move to a destination city
    return 2 - state[2]['D'] + 2 - state[2]['E']

print(a_star())

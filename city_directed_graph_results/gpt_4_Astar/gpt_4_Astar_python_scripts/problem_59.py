
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities as the nodes and the roads as the edges
    # The adjacency matrix is represented as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries that represent the cities that can be reached from the key city, with the travel time as the value
    graph = {
        'D': {'F': 1, 'S': 1, 'I': 1},
        'Y': {'D': 1, 'M': 1, 'Q': 1, 'B': 1},
        'F': {'M': 1, 'K': 1, 'I': 1},
        'M': {'K': 1, 'S': 1, 'I': 1, 'L': 1},
        'W': {'F': 1, 'L': 1},
        'H': {'F': 1, 'B': 1, 'L': 1},
        'Q': {'D': 1, 'M': 1, 'H': 1, 'B': 1, 'V': 1},
        'B': {'F': 1, 'W': 1, 'H': 1},
        'K': {'H': 1, 'B': 1, 'V': 1},
        'S': {'Y': 1, 'F': 1, 'W': 1, 'B': 1},
        'V': {'B': 1, 'S': 1, 'I': 1},
        'I': {'Y': 1, 'W': 1, 'H': 1, 'Q': 1},
        'L': {'F': 1, 'K': 1, 'S': 1, 'V': 1}
    }

    # Define the initial state and the goal state of the problem
    # The initial state is a tuple of the current city, the cities visited so far, and the number of times the destination cities have been visited
    initial_state = ('K', frozenset(['K']), {'D': 0, 'L': 0})

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
        if state[2]['D'] == 2 and state[2]['L'] == 2:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in graph[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has been visited less than 2 times
            if (next_city not in state[1] or (next_city in ['D', 'L'] and state[2][next_city] < 2)):
                # Generate the new state
                new_state = (next_city, state[1].union([next_city]), state[2].copy())
                # Increment the visit count of the destination cities
                if next_city in ['D', 'L']:
                    new_state[2][next_city] += 1
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of destination cities that have not been visited twice yet
                    h = 4 - new_state[2]['D'] - new_state[2]['L']
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None

print(a_star())

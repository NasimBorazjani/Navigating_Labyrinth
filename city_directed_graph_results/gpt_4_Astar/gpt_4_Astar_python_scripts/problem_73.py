
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city
    adjacency_matrix = {
        'K': {'N': 1, 'I': 1, 'D': 1, 'R': 1, 'F': 1},
        'N': {'K': 1, 'M': 1, 'B': 1},
        'S': {'O': 1, 'R': 1, 'B': 1},
        'Y': {'R': 1},
        'O': {'K': 1, 'Z': 1},
        'I': {'K': 1, 'O': 1, 'T': 1, 'E': 1},
        'T': {'Y': 1, 'I': 1, 'D': 1, 'Z': 1, 'F': 1},
        'D': {'K': 1, 'I': 1, 'T': 1, 'Z': 1},
        'M': {'K': 1, 'S': 1, 'Y': 1, 'I': 1, 'Z': 1},
        'Z': {'O': 1, 'I': 1, 'E': 1},
        'R': {'K': 1, 'D': 1, 'E': 1},
        'B': {'K': 1, 'Y': 1, 'O': 1, 'I': 1, 'T': 1, 'Z': 1, 'F': 1},
        'E': {'K': 1, 'T': 1, 'M': 1, 'Z': 1, 'F': 1},
        'F': {'S': 1, 'Y': 1, 'I': 1, 'B': 1}
    }
    # Define the initial state as a tuple with the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('Y', frozenset(['Y']), {'K': 0, 'S': 0})
    # Define the goal state as visiting the destination cities twice
    goal_state = {'K': 2, 'S': 2}

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
        if state[2] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city has not been visited before or it is one of the destination cities
            if next_city not in state[1] or next_city in goal_state:
                # Generate the new state
                new_visited_cities = set(state[1])
                new_visited_cities.add(next_city)
                new_visited_destinations = dict(state[2])
                if next_city in goal_state:
                    new_visited_destinations[next_city] += 1
                new_state = (next_city, frozenset(new_visited_cities), new_visited_destinations)
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal_state):
    # An admissible and consistent heuristic is the number of destination cities that have not been visited twice
    # The heuristic relaxes the constraint that a city can only be visited once and presumes we can visit the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited twice in the goal state.
    return sum(goal_state[city] - state[2][city] for city in goal_state)

print(a_star())

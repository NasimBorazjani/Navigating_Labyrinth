
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the key city of the outer dictionary and values as the travel time (1 for all cities)
    adjacency_matrix = {'C': {'Z': 1, 'R': 1},
                        'Z': {'C': 1, 'Y': 1, 'R': 1, 'I': 1},
                        'F': {'P': 1, 'B': 1},
                        'U': {'C': 1, 'F': 1, 'H': 1, 'Y': 1, 'O': 1, 'A': 1, 'B': 1},
                        'W': {'C': 1, 'Z': 1, 'F': 1, 'Y': 1, 'R': 1, 'G': 1},
                        'T': {'Y': 1, 'A': 1, 'R': 1, 'G': 1},
                        'H': {'F': 1, 'W': 1, 'T': 1, 'P': 1, 'O': 1, 'R': 1, 'I': 1, 'G': 1},
                        'Y': {'Z': 1, 'F': 1, 'G': 1},
                        'P': {'B': 1},
                        'O': {'F': 1, 'A': 1, 'R': 1, 'G': 1},
                        'A': {'Y': 1, 'P': 1, 'O': 1, 'B': 1},
                        'R': {'C': 1, 'Z': 1, 'U': 1, 'H': 1, 'P': 1, 'I': 1, 'G': 1, 'B': 1},
                        'I': {'C': 1, 'U': 1, 'Y': 1, 'O': 1},
                        'G': {'C': 1, 'U': 1, 'T': 1, 'H': 1, 'R': 1, 'I': 1},
                        'B': {'T': 1, 'R': 1}}

    # Define the initial state and the goal state of the problem
    initial_state = ('F', ['R', 'R', 'G', 'G'], ['F'])
    goal_state = ('F', [], ['F', 'R', 'G', 'R', 'G'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        current_city, destinations, visited_cities = state
        for next_city in adjacency_matrix[current_city]:
            # Check if the new state would be valid, ie the next city must not have been visited before, unless it is one of the destination cities
            if next_city not in visited_cities or next_city in destinations:
                # Generate the new state
                new_destinations = destinations[:]
                if next_city in new_destinations:
                    new_destinations.remove(next_city)
                new_visited_cities = visited_cities + [next_city]
                new_state = (next_city, new_destinations, new_visited_cities)
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic relaxes the constraint that we can only visit each city once and presumes we can move directly to the destination cities
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of destination cities left to visit, if the next city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no destination cities left to visit in the goal state.
    return len(state[1])


print(a_star())

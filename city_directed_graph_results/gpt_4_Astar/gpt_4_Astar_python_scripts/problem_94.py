
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'I'
    goal_state = ['H', 'R', 'H', 'R']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'X': {'M': 1, 'J': 1, 'B': 1},
        'T': {'I': 1, 'B': 1},
        'R': {'O': 1, 'I': 1, 'Z': 1, 'V': 1, 'H': 1},
        'O': {'M': 1, 'V': 1, 'B': 1},
        'M': {'T': 1, 'O': 1, 'U': 1, 'H': 1},
        'U': {'T': 1, 'P': 1},
        'I': {'M': 1, 'V': 1, 'B': 1},
        'P': {'R': 1, 'O': 1, 'U': 1, 'I': 1},
        'Z': {'T': 1, 'O': 1, 'I': 1},
        'F': {'T': 1, 'R': 1, 'P': 1, 'Z': 1},
        'V': {'O': 1, 'I': 1},
        'H': {'X': 1, 'M': 1, 'Z': 1, 'F': 1, 'V': 1, 'Q': 1},
        'Q': {'T': 1, 'R': 1, 'U': 1, 'P': 1, 'H': 1},
        'J': {'X': 1, 'R': 1, 'O': 1, 'M': 1, 'P': 1, 'Z': 1, 'F': 1, 'Q': 1},
        'B': {'X': 1, 'T': 1, 'U': 1, 'P': 1, 'Z': 1, 'F': 1, 'V': 1, 'H': 1, 'Q': 1}
    }

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
        if actions == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the cities connected to the current city
        for city in adjacency_matrix[state[-1]]:
            # The action is valid if the city has not been visited before or it is one of the goal cities and it has not been visited twice before
            if (city not in actions and city not in goal_state) or (actions.count(city) < 2 and city in goal_state):
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if city not in visited_costs or new_cost < visited_costs[city]:
                    visited_costs[city] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(city, goal_state), new_cost, actions + [city], city))

    return None

def heuristic(city, goal_state):
    # An admissible and consistent heuristic is the number of goal cities not yet visited
    # The heuristic relaxes the constraint that a city can only be visited if it is connected to the current city and presumes we can move to the goal cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is moved toward is a goal city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all goal cities would have been visited in the goal state.
    return goal_state.count(city)

print(a_star())

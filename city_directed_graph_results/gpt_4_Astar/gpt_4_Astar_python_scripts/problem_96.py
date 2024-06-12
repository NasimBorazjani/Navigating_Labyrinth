
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'O'
    goal_state = ['J', 'K', 'J', 'K']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'R': {'L': 1, 'K': 1, 'C': 1, 'S': 1},
        'J': {'R': 1, 'Y': 1, 'K': 1, 'B': 1, 'X': 1},
        'E': {'R': 1, 'A': 1, 'L': 1, 'K': 1, 'Z': 1},
        'Y': {'E': 1, 'N': 1},
        'A': {'R': 1, 'Y': 1, 'C': 1, 'N': 1, 'B': 1, 'Z': 1},
        'L': {'R': 1, 'J': 1, 'A': 1, 'C': 1, 'Z': 1},
        'T': {'J': 1, 'L': 1, 'C': 1},
        'K': {'X': 1, 'N': 1},
        'C': {'K': 1},
        'N': {'E': 1, 'L': 1, 'K': 1, 'C': 1},
        'B': {'R': 1, 'N': 1},
        'S': {'E': 1, 'Y': 1, 'A': 1},
        'Z': {'R': 1, 'J': 1, 'K': 1, 'C': 1, 'N': 1, 'B': 1, 'S': 1},
        'X': {'R': 1, 'J': 1, 'Y': 1, 'A': 1, 'L': 1, 'S': 1, 'Z': 1},
        'O': {'A': 1, 'T': 1, 'N': 1, 'B': 1, 'S': 1, 'Z': 1, 'X': 1}
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

        # Check if the current state is the goal state
        if actions[-4:] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        for next_city in adjacency_matrix[state]:
            # The action is valid if the next city is not visited or is one of the goal cities
            if next_city not in actions or next_city in goal_state:
                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(next_city, goal_state), new_cost, actions + [next_city], next_city))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of goal cities not yet visited
    # The heuristic relaxes the constraint that a city can only be visited once and presumes we can move to the goal cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is moved toward is a goal city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all goal cities would have been visited in the goal state.
    return sum(city not in state for city in goal)

print(a_star())

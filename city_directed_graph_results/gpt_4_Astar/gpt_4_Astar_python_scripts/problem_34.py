
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'J': ['N'],
        'S': ['W', 'Z'],
        'T': ['B'],
        'W': ['J', 'S', 'G', 'P', 'U'],
        'G': ['S', 'W', 'Z'],
        'N': ['T', 'W', 'G', 'P', 'U'],
        'M': ['W'],
        'Z': ['N', 'B', 'U'],
        'B': ['J', 'G', 'M'],
        'P': ['T', 'N', 'M'],
        'U': ['J', 'G', 'N', 'P']
    }

    # Define the initial state and the goal state
    initial_state = ('T', 0, 0)
    goal_state = (2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[1:] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # Check if the new state would be valid, ie if the city has not been visited before or is one of the destination cities
            if neighbor not in actions or neighbor in ['N', 'W']:
                # Generate the new state
                new_state = (neighbor, state[1] + (neighbor == 'N'), state[2] + (neighbor == 'W'))
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining visits to the destination cities
    # The heuristic relaxes the constraint that we can only visit each city once and presumes we can visit the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the remaining visits to the destination cities, if the neighboring city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining visits to the destination cities in the goal state
    return goal[0] - state[1] + goal[1] - state[2]

print(a_star())

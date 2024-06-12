
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = {
        'W': ['Y', 'K', 'Q'],
        'D': ['A', 'E'],
        'R': ['W', 'C'],
        'A': ['D', 'R', 'Y', 'S', 'N'],
        'Y': ['Q'],
        'F': ['W', 'R', 'S'],
        'C': ['D', 'Y', 'F', 'S', 'N', 'E', 'Q'],
        'S': ['W', 'D', 'Y', 'N'],
        'N': ['D', 'R', 'A', 'F', 'C', 'Q'],
        'E': ['K'],
        'K': ['A', 'F', 'N'],
        'Q': ['D', 'A', 'C', 'S', 'N', 'E']
    }

    # Define the initial state and the goal state
    initial_state = ('E', 'E', 0, ['D', 'D', 'R', 'R'])
    goal_state = ('E', 'E', 0, [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken to reach the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city = state[0]
        for next_city in adjacency_matrix[current_city]:
            # The new state is valid if the next city is not visited more than once, unless it is a destination city
            if actions.count(next_city) < 1 or next_city in ['D', 'R']:
                # Generate the new state
                new_state = (next_city, current_city, g + 1, [city for city in state[3] if city != next_city or state[3].count(city) > 1])
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of destination cities not yet visited
                    h = len(new_state[3])
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'A': ['Q', 'S', 'O', 'N', 'B'],
        'Q': ['A', 'N', 'B'],
        'S': ['A', 'N', 'D'],
        'O': ['A', 'N', 'X', 'D'],
        'N': ['O', 'X', 'V', 'I'],
        'V': ['A', 'Q', 'D'],
        'I': ['Y'],
        'X': ['A', 'Q', 'N', 'I', 'E'],
        'D': ['S', 'O', 'X', 'B', 'E'],
        'B': ['A', 'Q', 'S', 'O', 'N', 'V', 'X', 'I', 'D', 'E', 'Y'],
        'E': ['A', 'Q', 'S', 'V', 'I', 'X', 'D', 'B'],
        'Y': ['S', 'V', 'I', 'B']
    }

    # Define the initial state and the goal state
    initial_state = ('I', frozenset(), 0)
    goal_state = 2

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, (current_city, visited_cities, visited_destinations) = heapq.heappop(queue)

        # Check if the current state is the goal state
        if visited_destinations == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it's a destination city
            if next_city not in visited_cities or next_city in 'AX':
                # Generate the new state
                new_visited_cities = visited_cities | {next_city}
                new_visited_destinations = visited_destinations
                if next_city in 'AX':
                    new_visited_destinations += 1
                new_state = (next_city, new_visited_cities, new_visited_destinations)

                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is a destination city
    _, _, visited_destinations = state
    return goal - visited_destinations

print(a_star())

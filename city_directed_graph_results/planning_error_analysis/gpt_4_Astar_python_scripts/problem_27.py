
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'J': ['X'],
        'H': ['K', 'B', 'U'],
        'K': ['I'],
        'W': ['H', 'K', 'X'],
        'X': ['H', 'I'],
        'I': ['K', 'B', 'U', 'Z'],
        'B': ['W', 'Z', 'G'],
        'U': ['K', 'W', 'X'],
        'D': ['W', 'I', 'U'],
        'Z': ['J', 'K', 'W', 'U'],
        'G': ['J', 'X', 'Z']
    }
    # Define the initial state and the goal state
    initial_state = ('D', ['H', 'H', 'Z', 'Z'], ['J', 'H', 'K', 'W', 'X', 'I', 'B', 'U', 'D', 'Z', 'G'])
    goal_state = ('D', [], [])

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

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, destinations, remaining_cities = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the city must be in the remaining cities or be a destination city
            if next_city in remaining_cities or next_city in destinations:
                # Generate the new state
                new_destinations = destinations[:]
                new_remaining_cities = remaining_cities[:]
                if next_city in new_destinations:
                    new_destinations.remove(next_city)
                else:
                    new_remaining_cities.remove(next_city)
                new_state = (next_city, new_destinations, new_remaining_cities)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of destination cities left to visit, if the city is a destination city
    return len(state[1])

print(a_star())

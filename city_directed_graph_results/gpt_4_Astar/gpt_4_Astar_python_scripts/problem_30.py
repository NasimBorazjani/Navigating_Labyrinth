
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    # Define the cities
    cities = ['S', 'V', 'U', 'W', 'G', 'E', 'H', 'P', 'T', 'Q', 'Z']
    # Define the initial state and the goal state
    initial_state = ('G', ['H', 'H', 'P', 'P'], ['S', 'V', 'U', 'W', 'E', 'T', 'Q', 'Z'])
    goal_state = ('G', [], [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city = state[0]
        remaining_destinations = state[1]
        remaining_cities = state[2]
        for i in range(len(cities)):
            # Check if there is a road from the current city to the city at index i
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                # Check if the next city is a destination city
                if next_city in remaining_destinations:
                    new_destinations = remaining_destinations[:]
                    new_destinations.remove(next_city)
                    new_state = (next_city, new_destinations, remaining_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
                # Check if the next city is a non-destination city
                elif next_city in remaining_cities:
                    new_cities = remaining_cities[:]
                    new_cities.remove(next_city)
                    new_state = (next_city, remaining_destinations, new_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal_state):
    # The heuristic function can be the sum of the number of remaining destination cities and the number of remaining non-destination cities
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as each remaining city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a remaining city
    return len(state[1]) + len(state[2])

print(a_star())

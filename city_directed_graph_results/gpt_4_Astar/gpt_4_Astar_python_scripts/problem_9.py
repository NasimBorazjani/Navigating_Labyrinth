
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]]
    # Define the cities
    cities = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
    # Define the initial state and the goal state
    initial_state = ('C', ['F', 'W'], [])
    goal_state = ('C', [], ['F', 'W', 'F', 'W'])

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

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        current_city = state[0]
        current_city_index = cities.index(current_city)
        for i in range(len(cities)):
            if adjacency_matrix[current_city_index][i] == 1:
                next_city = cities[i]
                # Check if the next city is a destination city
                if next_city in state[1]:
                    # Remove the city from the list of destination cities to visit
                    new_destinations = state[1][:]
                    new_destinations.remove(next_city)
                    # Add the city to the list of visited destination cities
                    new_visited_destinations = state[2] + [next_city]
                    new_state = (next_city, new_destinations, new_visited_destinations)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
                # If the next city is not a destination city, we can only visit it if we have not visited it before
                elif next_city not in actions:
                    new_state = (next_city, state[1], state[2])
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function can be the number of destination cities left to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return len(state[1])

print(a_star())

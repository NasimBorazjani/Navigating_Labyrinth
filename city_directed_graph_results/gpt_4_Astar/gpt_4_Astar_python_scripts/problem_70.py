
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
    # Define the cities
    cities = ['K', 'I', 'E', 'B', 'Y', 'J', 'U', 'D', 'L', 'A', 'X', 'C', 'F', 'V']
    # Define the initial state and the goal state
    initial_state = ('V', ['E', 'E', 'U', 'U'], ['V'])
    goal_state = ('', [], ['V', 'E', 'U', 'E', 'U', 'V'])

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

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        current_city = state[0]
        remaining_cities = state[1]
        visited_cities = state[2]
        for i in range(len(cities)):
            # Check if the city is directly connected to the current city
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                # Check if the next city is one of the destination cities or has not been visited yet
                if next_city in remaining_cities or next_city not in visited_cities:
                    # Generate the new state
                    new_remaining_cities = remaining_cities[:]
                    if next_city in new_remaining_cities:
                        new_remaining_cities.remove(next_city)
                    new_visited_cities = visited_cities + [next_city]
                    new_state = (next_city, new_remaining_cities, new_visited_cities)
                    # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the number of remaining destination cities to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining destination city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining destination cities to visit in the goal state.
    return len(state[1])

print(a_star())

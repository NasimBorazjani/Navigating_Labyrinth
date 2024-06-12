
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    cities = ['J', 'U', 'X', 'R', 'L', 'Z', 'O', 'F', 'Q', 'C', 'N', 'V', 'M']
    initial_state = ('J', ['J'], ['Z', 'Z', 'M', 'M'])
    goal_state = ('J', ['J', 'Z', 'M', 'Z', 'M'], [])
    num_cities = len(cities)

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
        current_city_index = cities.index(current_city)
        for i in range(num_cities):
            if adjacency_matrix[current_city_index][i] == 1:
                next_city = cities[i]
                # Check if the new state would be valid, ie the next city must not have been visited before, unless it is one of the destination cities
                if (next_city not in state[1] or next_city in state[2]):
                    # Generate the new state
                    new_state = (next_city, state[1] + [next_city], [city for city in state[2] if city != next_city or state[2].count(city) > 1])
                    # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities left to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # It's consistent because moving to a new city reduces the heuristic cost of the successor node by a max of 1 (if the new city is a destination city), which is equal to the cost of reaching the successor node
    return len(state[2])

print(a_star())

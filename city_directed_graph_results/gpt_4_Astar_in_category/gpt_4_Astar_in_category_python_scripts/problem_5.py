
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['K', 'B', 'Z', 'S', 'X', 'H', 'O', 'E', 'U', 'V']

    # Define the initial state and goal state
    initial_state = ('H', False, False, False, False)
    goal_state = ('H', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['H'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        current_city_index = city_names.index(state[0])
        for i in range(len(city_names)):
            if adjacency_matrix[current_city_index][i] == 1:
                new_city = city_names[i]
                visited_K = state[1]
                visited_Z = state[2]
                visited_K_twice = state[3]
                visited_Z_twice = state[4]

                # Update the visited status of cities K and Z
                if new_city == 'K':
                    if visited_K:
                        visited_K_twice = True
                    visited_K = True
                elif new_city == 'Z':
                    if visited_Z:
                        visited_Z_twice = True
                    visited_Z = True

                # Generate the new state
                new_state = (new_city, visited_K, visited_Z, visited_K_twice, visited_Z_twice)

                # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities K and Z that have not been visited twice
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
    # It's consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost, if the new city is K or Z and it has not been visited twice, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all cities have been visited twice in the goal state.
    return (not goal[1]) + (not goal[2]) + (not goal[3]) + (not goal[4])

print(a_star())

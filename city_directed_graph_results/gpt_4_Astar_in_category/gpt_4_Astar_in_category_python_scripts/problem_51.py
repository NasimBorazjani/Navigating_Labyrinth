
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]]

    # Define the names of the cities
    cities = ['O', 'C', 'F', 'W', 'I', 'P', 'U', 'B', 'H', 'Q', 'G', 'S']

    # Define the initial state and goal state
    initial_state = (cities.index('G'), 0, 0)
    goal_state = (cities.index('G'), 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['G'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(cities)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before or if it is one of the destination cities
                if (cities[i] not in path and cities[i] != 'F' and cities[i] != 'U') or (cities[i] == 'F' and state[1] < 2) or (cities[i] == 'U' and state[2] < 2):
                    # Generate the new state
                    new_state = (i, state[1] + (cities[i] == 'F'), state[2] + (cities[i] == 'U'))
                    # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [cities[i]], new_state))

    return None

print(a_star())

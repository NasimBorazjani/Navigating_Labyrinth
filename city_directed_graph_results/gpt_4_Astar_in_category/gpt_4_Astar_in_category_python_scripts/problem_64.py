
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]]

    # Define the city names
    city_names = ['Z', 'J', 'T', 'D', 'W', 'L', 'P', 'Y', 'V', 'H', 'R', 'I', 'A']

    # Define the initial state and goal state
    initial_state = ('Y', False, False)
    goal_state = ('Y', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['Y'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_d = state[1] or new_city == 'D'
                visited_r = state[2] or new_city == 'R'
                new_state = (new_city, visited_d, visited_r)

                # Check if the new state is valid
                if new_city not in path or (new_city == 'D' and not visited_d) or (new_city == 'R' and not visited_r):
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [new_city], new_state))

    return None

print(a_star())

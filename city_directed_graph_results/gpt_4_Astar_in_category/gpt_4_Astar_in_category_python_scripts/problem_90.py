
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    cities = [
        ['C', 'Z', 'F', 'U', 'W', 'T', 'H', 'Y', 'P', 'O', 'A', 'R', 'I', 'G', 'B'],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    ]

    # Define the initial state and goal state
    initial_state = ('F', False, False)
    goal_state = ('F', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['F'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(1, len(cities)):
            if cities[state[0]][i] == 1:
                new_city = cities[0][i]
                visited_G = state[1] or new_city == 'G'
                visited_R = state[2] or new_city == 'R'
                new_state = (new_city, visited_G, visited_R)

                # Check if the new state is valid
                if (new_city not in path or (new_city == 'G' and not visited_G) or (new_city == 'R' and not visited_R)):
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, path + [new_city], new_state))

    return None

print(a_star())

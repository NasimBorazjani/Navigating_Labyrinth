
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    ]

    # Define the city names
    city_names = ['I', 'P', 'G', 'S', 'Y', 'A', 'D', 'U', 'E', 'W', 'V', 'H', 'Z', 'X']

    # Define the initial state and goal state
    initial_state = ('Y', False, False)
    goal_state = ('Y', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state[0]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_H = state[1] or new_city == 'H'
                visited_X = state[2] or new_city == 'X'
                new_state = (new_city, visited_H, visited_X)

                # Check if the new state is valid, ie if we have not visited the city before (unless it's H or X) and if we have visited H and X at least once before visiting Y again
                if (new_city not in path or new_city in ['H', 'X']) and (new_city != 'Y' or (new_city == 'Y' and visited_H and visited_X)):
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities we still need to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as we need to visit each city at least once
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if we move to a city we have not visited before
    return 2 - state[1] - state[2]

print(a_star())

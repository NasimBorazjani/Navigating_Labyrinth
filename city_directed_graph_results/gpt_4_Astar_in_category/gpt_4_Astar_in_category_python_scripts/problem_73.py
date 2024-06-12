
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]]

    # Define the names of the cities
    cities = ['K', 'N', 'S', 'Y', 'O', 'I', 'T', 'D', 'M', 'Z', 'R', 'B', 'E', 'F']

    # Define the initial state and the goal state
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

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                visited_S = state[1] or new_city == 'S'
                visited_K = state[2] or new_city == 'K'
                new_state = (new_city, visited_S, visited_K)

                # Check if the new state is valid, ie if we have not visited the city before (unless it is city S or K, which we must visit twice)
                if new_city not in path or (new_city == 'S' and not visited_S) or (new_city == 'K' and not visited_K):
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities we still need to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as we must visit each city at least once
    # This heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost if we move to a city we have not visited before
    h = 0
    if not state[1]:
        h += 1
    if not state[2]:
        h += 1
    return h

print(a_star())

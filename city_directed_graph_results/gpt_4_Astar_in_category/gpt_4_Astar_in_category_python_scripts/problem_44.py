
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]]

    # Define the names of the cities
    city_names = ['H', 'F', 'C', 'E', 'T', 'V', 'R', 'I', 'M', 'Z', 'L', 'D']

    # Define the initial state and the goal state
    initial_state = ('E', False, False)
    goal_state = ('E', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['E'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_map)):
            if city_map[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_T = state[1] or new_city == 'T'
                visited_D = state[2] or new_city == 'D'
                new_state = (new_city, visited_T, visited_D)

                # Check if the new state is valid, ie if we have not visited the city before (unless it's T or D)
                if new_city not in path or new_city in ['T', 'D']:
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities (T and D) that we have not visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as we must visit each of the cities at least once
    # It's consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if we move to a city that we have not visited yet
    return sum(not state[i] for i in range(1, len(state)))

print(a_star())

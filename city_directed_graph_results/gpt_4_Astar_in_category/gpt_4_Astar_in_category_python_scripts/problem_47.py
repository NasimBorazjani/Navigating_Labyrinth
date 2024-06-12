
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]

    # Define the city names
    city_names = ['Z', 'O', 'F', 'M', 'C', 'K', 'B', 'U', 'D', 'R', 'S', 'J']

    # Define the initial state and goal state
    initial_state = ('Z', False, False)
    goal_state = ('Z', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['Z'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        current_city = state[0]
        current_city_index = city_names.index(current_city)
        for i in range(len(adjacency_matrix[current_city_index])):
            if adjacency_matrix[current_city_index][i] == 1:
                new_city = city_names[i]
                visited_c = state[1] or new_city == 'C'
                visited_d = state[2] or new_city == 'D'
                new_state = (new_city, visited_c, visited_d)

                # Check if the new state is valid, ie if we have not visited the new city before (unless it's C or D)
                if new_city not in path or new_city in ['C', 'D']:
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that we still need to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as we need to visit each city at least once
    # This heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost if we move to a city that we need to visit
    h = 0
    if not state[1]:
        h += 1
    if not state[2]:
        h += 1
    return h

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]]
    # Define the city names
    city_names = ['I', 'E', 'A', 'G', 'V', 'K', 'B', 'N', 'F', 'W', 'J', 'O']
    # Define the initial state and goal state
    initial_state = ('E', False, False)
    goal_state = ('E', True, True)
    # Define the indices of the destination cities
    destination_indices = [city_names.index('N'), city_names.index('O')]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [initial_state[0]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities that are directly connected to the current city
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_N = state[1]
                visited_O = state[2]
                # If the new city is a destination city, update the visited status of the destination city
                if i == destination_indices[0]:
                    visited_N = not visited_N
                elif i == destination_indices[1]:
                    visited_O = not visited_O
                # Generate the new state
                new_state = (new_city, visited_N, visited_O)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to visit the destination cities twice
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The new city must be added to the path
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected to the current city and that we can only visit each city once (except for the destination cities); ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is equal to the decrease in the heuristic cost if the successor node is a destination city that has not been visited twice
    return (not state[1]) + (not state[2])

print(a_star())

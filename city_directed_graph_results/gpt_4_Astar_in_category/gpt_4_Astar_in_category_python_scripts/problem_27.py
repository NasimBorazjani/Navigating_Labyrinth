
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]

    # Define the city names
    city_names = ['J', 'H', 'K', 'W', 'X', 'I', 'B', 'U', 'D', 'Z', 'G']

    # Define the initial state and goal state
    initial_state = ('D', False, False)
    goal_state = ('D', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['D'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
                if city_names[i] not in path or city_names[i] in ['H', 'Z']:
                    # Generate the new state
                    new_state = (city_names[i], state[1] or city_names[i] == 'H', state[2] or city_names[i] == 'Z')
                    # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return sum([not state[1], not state[2]])

print(a_star())

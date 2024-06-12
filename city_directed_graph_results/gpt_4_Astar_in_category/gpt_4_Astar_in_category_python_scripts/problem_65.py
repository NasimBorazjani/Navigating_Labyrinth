
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['F', 'D', 'E', 'Z', 'G', 'Y', 'N', 'I', 'X', 'P', 'S', 'Q', 'C']

    # Define the initial state and goal state
    initial_state = (city_names.index('Q'), 0, 0)
    goal_state = (2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1:] == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_names)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities and has been visited less than 2 times
                if (city_names[i] not in path and city_names[i] not in ['F', 'N']) or (path.count(city_names[i]) < 2 and city_names[i] in ['F', 'N']):
                    # Generate the new state
                    new_state = (i, state[1] + (city_names[i] == 'F'), state[2] + (city_names[i] == 'N'))
                    # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of times we still need to visit each of the destination cities
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to the destination cities
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic estimate, if the city is one of the destination cities, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as we would have visited each of the destination cities twice in the goal state.
    return goal[0] - state[1] + goal[1] - state[2]

print(a_star())

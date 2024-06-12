
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['I', 'H', 'R', 'E', 'G', 'S', 'W', 'Q', 'C', 'A', 'B', 'F', 'J', 'V', 'L']

    # Define the initial state and goal state
    initial_state = (11, False, False, False, False)  # (current city, visited R once, visited S once, visited R twice, visited S twice)
    goal_state = (11, True, True, True, True)

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

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(len(city_names)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is city R or S and has not been visited twice
                if i not in path or (i == 2 and not state[3]) or (i == 5 and not state[4]):
                    # Generate the new state
                    new_state = list(state)
                    new_state[0] = i
                    if i == 2:  # If the city is R
                        if new_state[1]:  # If R has been visited once
                            new_state[3] = True  # Mark R as visited twice
                        else:
                            new_state[1] = True  # Mark R as visited once
                    if i == 5:  # If the city is S
                        if new_state[2]:  # If S has been visited once
                            new_state[4] = True  # Mark S as visited twice
                        else:
                            new_state[2] = True  # Mark S as visited once
                    new_state = tuple(new_state)
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities R and S that have not been visited twice
    # The heuristic relaxes the constraints that we can only move to directly connected cities and that we can only visit each city once (except for R and S)
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is R or S and has not been visited twice, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all cities R and S have been visited twice in the goal state.
    return 2 - state[3] - state[4]

print(a_star())

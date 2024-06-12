
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['R', 'P', 'Z', 'U', 'H', 'T', 'E', 'W', 'F', 'M', 'D', 'L', 'Y', 'C', 'G']

    # Define the initial state and goal state
    initial_state = (city_names.index('L'), False, False)
    goal_state = (city_names.index('L'), True, True)

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

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_names)):
            # Check if the new state is valid, ie if there is a road from the current city to the new city and if the new city is not already visited, unless it is a destination city
            if adjacency_matrix[state[0]][i] == 1 and (city_names[i] not in path or city_names[i] in ['P', 'W']):
                # Generate the new state
                new_state = (i, state[1] or city_names[i] == 'P', state[2] or city_names[i] == 'W')
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraints that we can only travel along the roads and that we can only visit each city once, and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, which is exactly the decrease in the heuristic cost, if the successor node is a destination city. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    return sum(goal[1:]) - sum(state[1:])

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

    # Define the city names
    city_names = ['O', 'M', 'U', 'L', 'Q', 'P', 'D', 'A', 'S', 'B', 'K', 'V', 'E', 'Z']

    # Define the initial state and goal state
    initial_state = (1, False, False, [False]*14)  # The initial state is city M, and we haven't visited city L or Z yet
    goal_state = (1, True, True, [False]*14)  # The goal state is city M, and we have visited city L and Z twice

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['M'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(14):
            if adjacency_matrix[state[0]][i] == 1:  # If there is a road from the current city to city i
                # Check if the new state would be valid, ie we can't visit a city more than once, except for city L and Z
                if (state[3][i] == False) or (i == 3 and state[1] == False) or (i == 13 and state[2] == False):
                    # Generate the new state
                    new_state = list(state)
                    new_state[0] = i
                    if i == 3:  # If the new city is L
                        new_state[1] = True
                    if i == 13:  # If the new city is Z
                        new_state[2] = True
                    new_state[3] = list(state[3])
                    new_state[3][i] = True
                    new_state = tuple(new_state)
                    # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that we still need to visit
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any city that we still need to visit
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the number of cities that we still need to visit, if we move to a city that we still need to visit, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no cities that we still need to visit in the goal state.
    h = 0
    if state[1] == False:  # If we still need to visit city L
        h += 1
    if state[2] == False:  # If we still need to visit city Z
        h += 1
    for i in range(14):  # For each city
        if state[3][i] == False and i != 3 and i != 13:  # If we still need to visit the city and it's not city L or Z
            h += 1
    return h

print(a_star())

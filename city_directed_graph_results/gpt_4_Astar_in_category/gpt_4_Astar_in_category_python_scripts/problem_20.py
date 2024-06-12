
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

    # Define the city names
    city_names = ['F', 'I', 'Y', 'R', 'X', 'Q', 'M', 'S', 'C', 'D', 'N']

    # Define the initial state and goal state
    initial_state = (0, False, False, [False]*11, 0)  # (current city, visited I, visited N, visited cities, number of cities visited)
    goal_state = (0, True, True, [False]*11, 11)  # (current city, visited I, visited N, visited cities, number of cities visited)
    goal_state[3][1] = True
    goal_state[3][10] = True

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [city_names[0]], initial_state)]  # (priority, cost so far, path, state)

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(11):
            if city_map[state[0]][i] == 1:  # If there is a direct road to city i
                # Check if the new state would be valid, ie if the city i has not been visited or if it is city I or N
                if not state[3][i] or i == 1 or i == 10:
                    # Generate the new state
                    new_state = list(state)
                    new_state[0] = i
                    new_state[3] = list(state[3])
                    new_state[3][i] = True
                    new_state[4] += 1
                    if i == 1:
                        new_state[1] = not new_state[1]
                    if i == 10:
                        new_state[2] = not new_state[2]
                    new_state = tuple(new_state)
                    # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of cities left to visit
    # The heuristic relaxes the constraint that we can only move to directly connected cities and presumes we can move directly to any unvisited city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the number of cities left to visit, if the city is unvisited, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no cities left to visit in the goal state.
    return 11 - state[4]

print(a_star())

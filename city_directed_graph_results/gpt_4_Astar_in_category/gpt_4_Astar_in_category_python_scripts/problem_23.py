
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]

    # Define the names of the cities
    cities = ['N', 'W', 'X', 'P', 'J', 'E', 'L', 'M', 'I', 'K', 'Q']

    # Define the initial state and the goal state
    initial_state = ('K', False, False, False, False)
    goal_state = ('K', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['K'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
                if (cities[i] not in path) or (cities[i] == 'P' and not state[3]) or (cities[i] == 'N' and not state[4]):
                    # Generate the new state
                    new_state = list(state)
                    new_state[0] = cities[i]
                    if cities[i] == 'P':
                        new_state[1] = True
                        new_state[3] = not new_state[3]
                    if cities[i] == 'N':
                        new_state[2] = True
                        new_state[4] = not new_state[4]
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited twice
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is one of the destination cities and has not been visited twice before, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited twice in the goal state.
    return 2 - state[1] - state[2] + 2 - state[3] - state[4]

print(a_star())

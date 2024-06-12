
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
                        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['Q', 'O', 'P', 'T', 'W', 'E', 'X', 'M', 'D', 'V']

    # Define the initial state and goal state
    initial_state = (0, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0))
    goal_state = (0, (0, 0, 2, 0, 0, 2, 0, 0, 0, 0), (0, 0))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[0]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(adjacency_matrix)):
            # Check if the city is connected to the current city and if it has not been visited yet or if it is city P or E and has been visited only once
            if adjacency_matrix[state[0]][i] == 1 and (state[1][i] == 0 or (i == 2 or i == 5) and state[1][i] == 1):
                # Generate the new state
                new_state = list(state[1])
                new_state[i] += 1
                new_state = (i, tuple(new_state), (state[2][0] + 1 if i == 2 else state[2][0], state[2][1] + 1 if i == 5 else state[2][1]))

                # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of visits remaining to city P and city E
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to city P or E
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the heuristic estimate, if the city is P or E, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as no more visits to city P or E are required in the goal state.
    return goal[2][0] - state[2][0] + goal[2][1] - state[2][1]

print(a_star())

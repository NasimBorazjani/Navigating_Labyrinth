
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]]
    # Define the names of the cities
    cities = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
    # Define the initial state and the goal state
    initial_state = (2, 0, 0)  # (current city, visited F, visited W)
    goal_state = (2, 2, 2)  # (current city, visited F twice, visited W twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [cities[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(len(cities)):
            # Check if the new state is valid, ie if there is a direct road from the current city to the new city
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new city is F or W, if so, increment the visited count
                visited_F = state[1]
                visited_W = state[2]
                if cities[i] == 'F':
                    visited_F += 1
                elif cities[i] == 'W':
                    visited_W += 1
                # Check if the new city has been visited before, if not, it is a valid state
                if (cities[i] not in path) or (cities[i] == 'F' and visited_F <= 2) or (cities[i] == 'W' and visited_W <= 2):
                    new_state = (i, visited_F, visited_W)
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [cities[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities left to visit
    # The heuristic relaxes the constraint that we can only move to directly connected cities and presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the number of cities left to visit, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no cities left to visit in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())

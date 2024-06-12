
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]]

    # Define the city names
    city_names = ['R', 'J', 'E', 'Y', 'A', 'L', 'T', 'K', 'C', 'N', 'B', 'S', 'Z', 'X', 'O']

    # Define the initial state and goal state
    initial_state = (14, False, False)  # (city index, visited J, visited K)
    goal_state = (14, True, True)  # (city index, visited J twice, visited K twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(15):
            # Check if there is a direct road from the current city to city i
            if adjacency_matrix[state[0]][i] == 1:
                # Generate the new state
                visited_j = state[1]
                visited_k = state[2]
                # If city i is J or K, update the visited status
                if i == 1:
                    visited_j = True
                elif i == 7:
                    visited_k = True
                new_state = (i, visited_j, visited_k)

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraint that we can only move to directly connected cities and presumes we can move directly to the destination cities
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city moved to is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities would have been visited in the goal state.
    return sum([not state[i] for i in range(1, 3)])


print(a_star())

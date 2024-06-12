
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]

    # Define the city names
    city_names = ['L', 'T', 'W', 'P', 'Z', 'H', 'I', 'X', 'R', 'C', 'K']

    # Define the initial state and goal state
    initial_state = (6, 0, 0)  # (current city, visited W, visited L)
    goal_state = (6, 2, 2)  # (current city, visited W twice, visited L twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for new_city in range(len(city_names)):
            # Check if the new city is connected to the current city
            if adjacency_matrix[state[0]][new_city] == 1:
                # Check if the new city is W or L, and if it has been visited less than twice
                if (new_city == 2 and state[1] < 2) or (new_city == 0 and state[2] < 2):
                    # Generate the new state
                    new_state = (new_city, state[1] + (new_city == 2), state[2] + (new_city == 0))
                    # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))

                # If the new city is not W or L, and it has not been visited before
                elif new_city not in path:
                    # Generate the new state
                    new_state = (new_city, state[1], state[2])
                    # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of times we still need to visit W and L
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected, and that we can only visit each city once (except for W and L)
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if we move to W or L, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as we don't need to visit W or L anymore in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]


print(a_star())

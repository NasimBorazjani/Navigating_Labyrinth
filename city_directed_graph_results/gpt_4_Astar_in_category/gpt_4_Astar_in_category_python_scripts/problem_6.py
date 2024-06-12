
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]]
    # Define the city names
    city_names = ['F', 'I', 'O', 'J', 'K', 'D', 'N', 'R', 'M', 'B']
    # Define the initial state and the goal state
    initial_state = (6, 0, 0)  # (current city, number of visits to D, number of visits to F)
    goal_state = (6, 2, 2)  # (current city, number of visits to D, number of visits to F)

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
        for i in range(len(adjacency_matrix)):
            # Check if the new state would be valid, ie if there is a road from the current city to the new city and if the new city is not already visited (except for D and F)
            if adjacency_matrix[state[0]][i] == 1 and (i not in path or city_names[i] in ['D', 'F']):
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                if city_names[i] == 'D':
                    new_state[1] += 1
                elif city_names[i] == 'F':
                    new_state[2] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of visits remaining to D and F
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to D or F
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic estimate, if the city is D or F, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as no more visits to D or F are required in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())

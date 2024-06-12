
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]]

    # Define the names of the cities
    city_names = ['S', 'U', 'X', 'D', 'I', 'Z', 'R', 'M', 'K', 'Q']

    # Define the initial state and goal state
    initial_state = (3, False, False, False, False, False, False, False, False, False, False, False)
    goal_state = (3, True, True, True, True, True, True, True, True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[3]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(10):
            # Check if the new state would be valid, ie if there is a road from the current city to the new city and if the new city has not been visited twice already
            if adjacency_matrix[state[0]][i] == 1 and state[i+1] < 2:
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[i+1] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited twice yet
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected to the current city and presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of cities that have not been visited twice yet, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all cities have been visited twice in the goal state.
    return sum(goal[i] - state[i] for i in range(1, 11))

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]]

    # Define the city names
    city_names = ['Z', 'C', 'M', 'X', 'N', 'A', 'B', 'L', 'U', 'K', 'G', 'Y', 'O']

    # Define the initial state and goal state
    initial_state = (city_names.index('K'), 0, 0)
    goal_state = (city_names.index('K'), 2, 2)

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
            # Check if the new state is valid, ie if there is a direct road from the current city to the new city
            if adjacency_matrix[state[0]][i] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                # If the new city is U or Y, increment the count of visits to U or Y
                if city_names[i] == 'U':
                    new_state[1] += 1
                elif city_names[i] == 'Y':
                    new_state[2] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_state[0]]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the sum of the remaining visits to U and Y
    # The heuristic relaxes the constraint that we can only visit each city once and presumes we can move directly to U or Y
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the remaining visits to U or Y, if the new city is U or Y, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining visits to U or Y in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())

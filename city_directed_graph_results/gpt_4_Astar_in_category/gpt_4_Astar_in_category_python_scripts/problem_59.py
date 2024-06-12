
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0]
    ]

    # Define the city names
    city_names = ['D', 'Y', 'F', 'M', 'W', 'H', 'Q', 'B', 'K', 'S', 'V', 'I', 'L']

    # Define the initial state and goal state
    initial_state = (city_names.index('K'), 0, 0)
    goal_state = (city_names.index('D'), 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['K'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for i in range(len(city_names)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is city D or L and has been visited less than 2 times
                if (city_names[i] not in path and city_names[i] not in ['D', 'L']) or (city_names[i] == 'D' and state[1] < 2) or (city_names[i] == 'L' and state[2] < 2):
                    # Generate the new state
                    new_state = (i, state[1] + (city_names[i] == 'D'), state[2] + (city_names[i] == 'L'))
                    # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the sum of the number of times we still need to visit city D and city L
    # The heuristic relaxes the constraints that we can only move to neighboring cities and that we can only visit each city once (except for D and L), ie it presumes we can move directly to city D or L
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is always 1, the decrease in the heuristic estimate
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
                        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['F', 'Z', 'M', 'Q', 'I', 'V', 'L', 'C', 'J', 'D', 'N', 'E', 'B', 'O']

    # Define the initial state and goal state
    initial_state = (city_names.index('Q'), 0, 0)
    goal_state = (city_names.index('L'), 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['Q'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[state[0]][i] == 1:
                # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
                if city_names[i] not in path or city_names[i] in ['L', 'M']:
                    # Generate the new state
                    new_state = (i, state[1], state[2])
                    if city_names[i] == 'L':
                        new_state = (i, state[1] + 1, state[2])
                    elif city_names[i] == 'M':
                        new_state = (i, state[1], state[2] + 1)
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities left to visit
    # The heuristic relaxes the constraints that we can only visit each city once and that we must visit the destination cities twice, and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is always 1, the decrease in the number of destination cities left to visit
    return 2 - state[1] + 2 - state[2]

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['M', 'Y', 'Q', 'T', 'E', 'A', 'J', 'S', 'V', 'F', 'W', 'N', 'Z', 'C', 'I']

    # Define the initial state and goal state
    initial_state = ('S', False, False)
    goal_state = ('S', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for i in range(len(city_names)):
            # Check if there is a road from the current city to the neighboring city
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = city_names[i]
                # If the new city is T or C, update the visited status
                if city_names[i] == 'T':
                    new_state[1] = True
                if city_names[i] == 'C':
                    new_state[2] = True
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraints that we can only visit each city once and that we have to visit T and C twice; ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is always 1, the decrease in the number of destination cities not yet visited
    return 2 - state.count(True)

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    # Define the names of the cities
    cities = ['S', 'T', 'R', 'A', 'L', 'B', 'V', 'I', 'P', 'N']
    # Define the initial state and the goal state
    initial_state = ('B', False, False)
    goal_state = ('B', True, True)
    # Define the index of the initial city
    initial_city_index = cities.index(initial_state[0])
    # Define the indices of the destination cities
    destination_city_indices = [cities.index('L'), cities.index('V')]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state[0]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        current_city_index = cities.index(state[0])
        for new_city_index in range(len(cities)):
            # Check if the new city is directly connected to the current city
            if adjacency_matrix[current_city_index][new_city_index] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = cities[new_city_index]
                # If the new city is a destination city, update the visited status of the destination city in the new state
                if new_city_index in destination_city_indices:
                    new_state[destination_city_indices.index(new_city_index) + 1] = True
                new_state = tuple(new_state)
                # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraints that we can only move to directly connected cities and that we can only visit each city once (except for the destination cities); ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the heuristic cost, if the successor node is a destination city not yet visited, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities would have been visited in the goal state
    return sum(goal[1:]) - sum(state[1:])

print(a_star())

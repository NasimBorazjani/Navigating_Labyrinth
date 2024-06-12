
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                        [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

    # Define the names of the cities
    city_names = ['R', 'Q', 'Y', 'U', 'F', 'K', 'M', 'T', 'X', 'W', 'H', 'L']

    # Define the initial state and goal state
    initial_state = (city_names.index('L'), 0, 0)
    goal_state = (city_names.index('L'), 2, 2)

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
        for new_city in range(len(city_names)):
            # Check if the new city is connected to the current city
            if adjacency_matrix[state[0]][new_city] == 1:
                # Check if the new city is one of the destination cities
                if city_names[new_city] == 'M':
                    # If we have not visited city M twice yet, we can move to city M
                    if state[1] < 2:
                        new_state = (new_city, state[1] + 1, state[2])
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
                elif city_names[new_city] == 'Q':
                    # If we have not visited city Q twice yet, we can move to city Q
                    if state[2] < 2:
                        new_state = (new_city, state[1], state[2] + 1)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
                else:
                    # If the new city is not one of the destination cities, we can move to the new city if we have not visited it before
                    if city_names[new_city] not in path:
                        new_state = (new_city, state[1], state[2])
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of times we still need to visit the destination cities
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected to the current city and that we can only visit each city once; ie It presumes we can move directly to the destination cities
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the heuristic cost if we move to a destination city
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

    # Define the city names
    city_names = ['O', 'F', 'U', 'W', 'T', 'Y', 'A', 'Z', 'S', 'G', 'X', 'H', 'D', 'M', 'Q']

    # Define the initial state and goal state
    initial_state = (6, False, False)  # (current city, visited G, visited O)
    goal_state = (6, True, True)  # (current city, visited G, visited O)

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

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for new_city in range(len(city_map)):
            # Check if the new city is directly connected to the current city
            if city_map[state[0]][new_city] == 1:
                # Check if the new city is G or O, if so, update the visited status
                visited_G = state[1] or new_city == 9
                visited_O = state[2] or new_city == 0
                # Check if the new city has been visited before, if not, update the visited status
                if (new_city != 9 and new_city != 0 and city_names[new_city] not in path) or (new_city == 9 and not visited_G) or (new_city == 0 and not visited_O):
                    # Generate the new state
                    new_state = (new_city, visited_G, visited_O)
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraints that we can only travel to directly connected cities and that we cannot visit a city more than once; ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is always 1, the decrease in the number of destination cities not yet visited
    return sum(1 for i in range(1, 3) if state[i] != goal[i])

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
                        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    # Define the city names
    city_names = ['E', 'V', 'G', 'W', 'U', 'F', 'S', 'H', 'K', 'B', 'Z', 'N', 'L', 'J']

    # Define the initial state and goal state
    initial_state = (8, False, False, [False]*14)  # The initial state is city K (index 8), and we haven't visited F or Z yet
    goal_state = (8, True, True, [False]*14)  # The goal state is city K (index 8), and we have visited F and Z twice

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; the path to the initial state is just the initial city
    queue = [(0, 0, ['K'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for new_city in range(14):
            if adjacency_matrix[state[0]][new_city] == 1:  # If there is a road from the current city to the new city
                # Check if the new city is F or Z, and if we have visited them less than twice
                visited_F = state[1] or (new_city == 5 and path.count('F') < 2)
                visited_Z = state[2] or (new_city == 10 and path.count('Z') < 2)

                # Check if we have visited the new city before (except for F and Z, which we can visit twice)
                visited_cities = state[3][:]
                if new_city != 5 and new_city != 10:
                    if visited_cities[new_city]:
                        continue
                    visited_cities[new_city] = True

                # Generate the new state
                new_state = (new_city, visited_F, visited_Z, visited_cities)

                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities (F and Z) that we still need to visit
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected and that we can only visit each city once (except for F and Z, which we can visit twice)
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if we move to a city that we need to visit, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as we have visited all the cities that we need to visit in the goal state.
    return (not state[1]) + (not state[2])

print(a_star())

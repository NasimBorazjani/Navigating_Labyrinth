
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
                        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0]]

    # Define the city names
    city_names = ['S', 'X', 'G', 'E', 'P', 'B', 'O', 'C', 'L', 'J', 'M', 'Y', 'T', 'W']

    # Define the initial state and goal state
    initial_state = ('Y', False, False)
    goal_state = ('Y', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['Y'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_M = state[1]
                visited_B = state[2]

                # If the new city is M or B, update the visited status
                if new_city == 'M':
                    visited_M = True
                elif new_city == 'B':
                    visited_B = True

                # Generate the new state
                new_state = (new_city, visited_M, visited_B)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited city must be visited at least once
    # It's consistent because the cost of moving from one city to an adjacent city is always 1, which is exactly the decrease in the heuristic cost, if the city is moved toward its goal position
    h = 0
    if not state[1]:
        h += 1
    if not state[2]:
        h += 1
    return h

print(a_star())

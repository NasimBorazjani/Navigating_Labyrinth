
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                        [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]]
    # Define the names of the cities
    cities = ['O', 'T', 'I', 'F', 'A', 'M', 'X', 'Y', 'R', 'G']
    # Define the initial state and the goal state
    initial_state = ('M', False, False, False, False)
    goal_state = ('M', True, True, True, True)
    # Define the index of the initial city
    initial_city_index = cities.index(initial_state[0])
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state[0]], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)
        # If the current state is the goal state, return the path
        if state == goal_state:
            return path
        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(len(cities)):
            # Check if there is a direct road from the current city to the city at index i
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = cities[i]
                # If the new city is 'A' or 'R', update the visited flags
                if cities[i] == 'A':
                    new_state[1] = True
                    new_state[3] = not new_state[3]
                elif cities[i] == 'R':
                    new_state[2] = True
                    new_state[4] = not new_state[4]
                new_state = tuple(new_state)
                # The cost so far is the number of moves made
                new_cost = g + 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities 'A' and 'R' that have not been visited twice
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited city must be visited at least once
    # It's consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is 'A' or 'R' and it has not been visited twice
    return 2 - state[1] - state[2]

print(a_star())

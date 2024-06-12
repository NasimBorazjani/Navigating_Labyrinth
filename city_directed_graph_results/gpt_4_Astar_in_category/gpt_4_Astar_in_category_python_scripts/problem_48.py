
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]]

    # Define the city names
    city_names = ['A', 'Q', 'S', 'O', 'N', 'V', 'I', 'X', 'D', 'B', 'E', 'Y']

    # Define the initial state and goal state
    initial_state = (6, False, False, False, False, False, True, False, False, False, False, False, 0, 0)
    goal_state = (6, True, False, False, False, False, True, True, False, False, False, False, 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[6]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(12):
            if adjacency_matrix[state[0]][i] == 1 and state[i] == False:
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[i] = True
                if i == 0 or i == 7:
                    new_state[12 + i//7] += 1
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited city must be visited at least once
    # It's consistent because the cost of moving from one city to an adjacent city is always 1, which is exactly the decrease in the heuristic cost, if the city is moved toward its goal position
    return sum(state[1:12]) - state[12] - state[13]

print(a_star())

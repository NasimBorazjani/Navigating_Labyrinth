
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]]

    # Define the city names
    city_names = ['L', 'A', 'J', 'U', 'E', 'P', 'Q', 'Y', 'H', 'R', 'K', 'M', 'F']

    # Define the initial state and goal state
    initial_state = (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)
    goal_state = (0, [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[0]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(adjacency_matrix[state[0]])):
            # Check if the city is connected to the current city and if it has not been visited yet or if it is city J or K and has been visited only once
            if adjacency_matrix[state[0]][i] == 1 and (state[1][i] == 0 or (i == 2 or i == 10) and state[1][i] == 1):
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[1][i] += 1
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
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected and that we have to visit city J and K twice; ie It presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the number of cities that have not been visited yet
    return sum([1 for i in range(len(state[1])) if state[1][i] < goal[1][i]])

print(a_star())

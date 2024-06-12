
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

    # Define the names of the cities
    city_names = ['V', 'C', 'I', 'Y', 'W', 'Q', 'X', 'K', 'Z', 'T', 'J', 'U', 'F']

    # Define the initial state and goal state
    initial_state = (9, False, False, False, False, False, False, False, False, False, False, False, False)
    goal_state = (9, True, False, True, False, False, False, False, False, False, False, False, False)

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
        for i in range(len(adjacency_matrix[state[0]])):
            # Check if the new state would be valid, ie if there is a direct road from the current city to the new city
            if adjacency_matrix[state[0]][i] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                # If the new city is city V or city I, update the state to reflect that we have visited these cities
                if i == 0:
                    new_state[1] = True
                elif i == 2:
                    new_state[3] = True
                # If we have already visited city V or city I, update the state to reflect that we have visited these cities twice
                elif new_state[1] and i == 0:
                    new_state[2] = True
                elif new_state[3] and i == 2:
                    new_state[4] = True
                # If we have visited a city other than V or I, update the state to reflect that we have visited this city
                else:
                    new_state[i+5] = True
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_state[0]]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that we have not yet visited
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected and that we have to visit city V and city I twice; ie It presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the number of cities that we have not yet visited
    return sum(state[1:]) - sum(goal[1:])

print(a_star())

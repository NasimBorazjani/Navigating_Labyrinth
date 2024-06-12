
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Define the names of the cities
    cities = ['X', 'M', 'U', 'N', 'T', 'V', 'Z', 'S', 'F', 'E', 'J']

    # Define the initial state and the goal state
    initial_state = (0, False, False, False, False, False, False, False, False, False, False, False, False)
    goal_state = (0, False, False, False, False, True, False, False, False, True, False, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [cities[0]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(len(cities)):
            # Check if the new state would be valid, ie if there is a direct road from the current city to the new city and if the new city has not been visited yet or if it is city E or T and it has been visited only once before
            if adjacency_matrix[state[0]][i] == 1 and (state[i+1] == False or (i == 4 and state[11] == False) or (i == 9 and state[12] == False)):
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[i+1] = True
                if i == 4:
                    new_state[11] = True
                if i == 9:
                    new_state[12] = True
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [cities[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # The heuristic relaxes the constraints that we can only move to directly connected cities and that we have to visit city E and city T twice; ie It presumes we can move directly to any unvisited city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the number of unvisited cities
    return sum(state[1:11]) + 2 - state[11] - state[12]

print(a_star())

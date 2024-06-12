
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]]

    # Define the names of the cities
    city_names = ['K', 'M', 'B', 'X', 'N', 'D', 'V', 'C', 'I', 'R', 'F', 'W', 'L']

    # Define the initial state and goal state
    initial_state = (7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    goal_state = (2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0)

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
        for i in range(len(city_map[state[0]])):
            # Check if the new state would be valid, ie if there is a road from the current city to the new city and if the new city is not a destination city, it must not have been visited before
            if city_map[state[0]][i] == 1 and (i == 2 or i == 12 or state[i+1] == 0):
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[i+1] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to visit the destination cities twice
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_state[0]]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice
    # The heuristic relaxes the constraints that we can only move to cities that are directly connected and that we can only visit each non-destination city once; ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to another is 1, which is exactly the decrease in the heuristic cost, if the successor node is a destination city that has not been visited twice. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    return sum(goal[i] - state[i] for i in range(1, len(state)))

print(a_star())

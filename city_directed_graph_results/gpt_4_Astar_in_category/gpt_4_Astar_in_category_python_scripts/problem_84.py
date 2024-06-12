
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]]

    # Define the names of the cities
    city_names = ['F', 'O', 'L', 'P', 'Y', 'R', 'Q', 'B', 'T', 'V', 'A', 'K', 'S', 'H']

    # Define the initial state and goal state
    initial_state = (city_names.index('T'), 0, 0)
    goal_state = (city_names.index('T'), 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the cities visited to get to each state in a list; only the initial city is visited to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        for new_city in range(len(city_map)):
            # Check if the new city is directly connected to the current city and if it has not been visited before
            if city_map[state[0]][new_city] == 1 and city_names[new_city] not in path:
                # Generate the new state
                # If the new city is H or K, increment the count of visits to H or K
                new_state = (new_city, state[1] + (city_names[new_city] == 'H'), state[2] + (city_names[new_city] == 'K'))
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of visits remaining to H and K
    # The heuristic relaxes the constraints that we can only move to directly connected cities and that we can only visit each city once; ie It presumes we can move directly to H or K
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, which is exactly the decrease in the heuristic estimate if the successor node is H or K
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    ]

    # Define the names of the cities
    city_names = ['P', 'G', 'W', 'V', 'L', 'M', 'B', 'S', 'J', 'H', 'D', 'N', 'R']

    # Define the initial state and goal state
    initial_state = (0, [False]*13, 0, 0)  # (current city, visited cities, visited G, visited J)
    goal_state = (0, [False]*13, 2, 2)  # (current city, visited cities, visited G, visited J)

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
        for next_city in range(13):
            if adjacency_matrix[state[0]][next_city] == 1 and (not state[1][next_city] or city_names[next_city] in ['G', 'J']):
                # Generate the new state
                new_state = list(state)
                new_state[0] = next_city
                new_state[1][next_city] = True
                if city_names[next_city] == 'G':
                    new_state[2] += 1
                elif city_names[next_city] == 'J':
                    new_state[3] += 1
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[next_city]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited city must be visited at least once
    # It's consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the number of unvisited cities, if the city is moved toward its goal position
    return sum(state[1]) - sum(goal[1])

print(a_star())

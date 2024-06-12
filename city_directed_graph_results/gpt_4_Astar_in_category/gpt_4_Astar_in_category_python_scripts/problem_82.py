
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['C', 'K', 'U', 'F', 'Q', 'B', 'N', 'W', 'H', 'J', 'T', 'X', 'R', 'L']

    # Define the initial state and goal state
    initial_state = (9, 0, 0, [False]*14, [0]*14)  # (current city, number of visits to F, number of visits to L, visited cities, number of visits to each city)
    goal_state = (3, 2, 2)

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
        if state[:3] == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for i in range(14):
            if adjacency_matrix[state[0]][i] == 1 and (state[3][i] == False or i == 3 or i == 13):
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[3][i] = True
                new_state[4][i] += 1
                if i == 3:
                    new_state[1] += 1
                if i == 13:
                    new_state[2] += 1
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_state[0]]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of visits remaining to F and L
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining visit must be made at least once
    # It's consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is F or L
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())

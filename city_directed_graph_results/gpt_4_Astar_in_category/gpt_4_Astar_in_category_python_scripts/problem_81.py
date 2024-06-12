
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    ]

    # Define the city names
    city_names = ['T', 'J', 'X', 'U', 'L', 'S', 'C', 'H', 'Z', 'O', 'D', 'Q', 'G', 'W']

    # Define the initial state and goal state
    initial_state = (3, False, False, False, False, False, False, False, False, False, False, False, False, False)
    goal_state = (1, False, False, False, True, False, False, True, False, False, False, False, False, False)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [city_names[3]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(14):
            if adjacency_matrix[state[0]][i] == 1 and state[i] == False:
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[i] = True
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[i]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # This heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic value
    return sum(state[1:]) - sum(goal[1:])

print(a_star())


import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    ]

    # Define the city names
    city_names = ['P', 'U', 'Q', 'G', 'E', 'K', 'M', 'J', 'N', 'T', 'Y', 'R', 'Z', 'X', 'O']

    # Define the initial state and goal state
    initial_state = ('G', False, False, False, False)
    goal_state = ('G', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['G'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_P = state[1] or new_city == 'P'
                visited_Y = state[2] or new_city == 'Y'
                visited_P_twice = state[3] or (visited_P and new_city == 'P')
                visited_Y_twice = state[4] or (visited_Y and new_city == 'Y')

                # Check if the new state is valid
                if (new_city not in path or (new_city == 'P' and not visited_P_twice) or (new_city == 'Y' and not visited_Y_twice)):
                    new_state = (new_city, visited_P, visited_Y, visited_P_twice, visited_Y_twice)
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited twice
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
    # It's consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is moved toward its goal position
    return sum(1 for i in range(1, 5) if state[i] != goal[i])

print(a_star())

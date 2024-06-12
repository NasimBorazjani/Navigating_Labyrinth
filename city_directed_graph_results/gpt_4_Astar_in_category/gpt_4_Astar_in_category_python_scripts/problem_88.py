
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
    ]

    # Define the city names
    city_names = ['T', 'W', 'Y', 'B', 'I', 'J', 'R', 'O', 'P', 'A', 'V', 'X', 'M', 'K', 'F']

    # Define the initial state and goal state
    initial_state = ('A', False, False)
    goal_state = ('A', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['A'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                new_city = city_names[i]
                visited_J = state[1] or new_city == 'J'
                visited_M = state[2] or new_city == 'M'
                new_state = (new_city, visited_J, visited_M)

                # Check if the new state is valid
                if new_state not in visited_costs or g + 1 < visited_costs[new_state]:
                    visited_costs[new_state] = g + 1
                    heapq.heappush(queue, (g + 1 + heuristic(new_state, goal_state), g + 1, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # The heuristic function can be the number of destination cities not yet visited
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
    return sum(s1 != s2 for s1, s2 in zip(state, goal))

print(a_star())

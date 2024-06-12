
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                        [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

    # Define the city names
    cities = ['S', 'A', 'J', 'U', 'E', 'B', 'N', 'P', 'L', 'X', 'F']

    # Define the initial state and goal state
    initial_state = ('J', False, False, False, False)
    goal_state = ('J', True, True, True, True)

    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Define the queue
    queue = [(0, 0, ['J'], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                visited_U = state[1] or new_city == 'U'
                visited_E = state[2] or new_city == 'E'
                visited_U_twice = state[3] or (visited_U and new_city == 'U')
                visited_E_twice = state[4] or (visited_E and new_city == 'E')

                # Check if the new state is valid
                if (new_city not in path or visited_U_twice or visited_E_twice) and (visited_U_twice <= 2 and visited_E_twice <= 2):
                    new_state = (new_city, visited_U, visited_E, visited_U_twice, visited_E_twice)
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # The heuristic function can be the number of cities that we still need to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
    return sum(goal[i] and not state[i] for i in range(1, len(goal)))

print(a_star())

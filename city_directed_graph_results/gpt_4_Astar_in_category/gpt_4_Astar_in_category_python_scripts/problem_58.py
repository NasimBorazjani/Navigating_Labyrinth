
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['B', 'K', 'S', 'X', 'T', 'P', 'Q', 'M', 'R', 'G', 'J', 'V', 'E']

    # Define the initial state and goal state
    initial_state = ('S', False, False, ['S'])
    goal_state = ('S', True, True, [])

    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Define the priority queue
    queue = [(0, 0, initial_state)]

    while queue:
        _, g, state = heapq.heappop(queue)

        # Unpack the state
        city, visited_b, visited_v, path = state

        # Check if the current state is the goal state
        if city == goal_state[0] and visited_b and visited_v and path.count('B') == 2 and path.count('V') == 2:
            return path

        # Generate all possible actions from the current state
        for i in range(len(city_names)):
            if adjacency_matrix[city_names.index(city)][i] == 1:
                new_city = city_names[i]
                new_visited_b = visited_b or new_city == 'B'
                new_visited_v = visited_v or new_city == 'V'
                new_path = path + [new_city]

                # Check if the new state is valid
                if new_path.count(new_city) <= 2 and (new_city != 'B' and new_city != 'V') or new_path.count(new_city) <= 4:
                    new_state = (new_city, new_visited_b, new_visited_v, new_path)
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, new_state))

    return None

print(a_star())
